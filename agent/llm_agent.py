from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from agents.memory import create_memory
from agents.tools import bocha, tavily, python_REPL
from agents.retriever import build_or_load_retriever, make_retriever_tool
import config

def create_llm_agent():
    llm = ChatOpenAI(
        model = config.MODEL_NAME,
        temperature = config.TEMPERATURE,
        api_key = config.OPENAI_API_KEY,
        base_url = config.OPENAI_BASE_URL,
    )

    memory = create_memory(memory_type=config.MEMORY_TYPE)
    
    tools = []
    # tools.append(bocha())
    tools.append(tavily())
    tools.append(python_REPL())
    
    retriever = build_or_load_retriever()
    retriever_tool = make_retriever_tool(retriever)
    # tools.append(retriever_tool)

    prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一名专业的知识问答助手。"
                "以下是从内部知识库检索到的相关内容，请优先基于这些资料回答：\n"
                "---------------------\n{context}\n---------------------\n"
                "当资料不足时，你可以使用可用工具（联网搜索、计算）补充信息。\n"
                "如果资料或工具都无法回答，请明确告知用户你无法确定答案，不要编造内容。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    for t in tools:
        origin = t.func
        def safe_func(*args, _f=origin, **kwargs):
            try:
                out = _f(*args, **kwargs)
            except Exception as e:
                return f"【工具执行异常：{e}】"
            return "【工具返回空结果】" if out is None else str(out)
        t.func = safe_func
    
    agent = create_tool_calling_agent(
        llm=llm, 
        tools=tools, 
        prompt=prompt,
    )

    executor = AgentExecutor.from_agent_and_tools(
        agent=agent, 
        tools=tools,
        memory=memory,
        handle_parsing_errors=True, 
        verbose=config.AGENT_VERBOSE,
        input_keys=["input", "context"],  
        output_keys=["output"],
    )

    def ask(query: str):
        docs = retriever.invoke(query)
        if not docs:
            context = "（知识库中未检索到相关内容）"
        else:
            context = "\n\n".join([d.page_content[:1000] for d in docs])
        return executor.invoke({"input": query, "context": context})

    print("✅ 已构建 对话 Agent")
    return executor, ask