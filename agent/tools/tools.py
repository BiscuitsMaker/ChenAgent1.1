from langchain.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.utilities import PythonREPL
from .bocha.bocha import bocha_search_run
import config

def bocha():
    bocha_tool = Tool(
        name = "bocha_search",
        description = "使用博查AI Web Search API 进行搜索，返回摘要结果。",
        func = bocha_search_run,
    )
    return bocha_tool

def tavily():
    search = TavilySearchResults(api_key=config.TAVILY_API_KEY)
    tavily_tool = Tool(
        name = "tavily_search",
        description = "用于检索互联网上的信息",
        func = search.run
    )
    return tavily_tool

def bocha():
    def safe_bocha_search(query):
        try:
            result = bocha_search_run(query)
            if not result:
                return "【未获取到搜索结果】"
            return str(result)
        except Exception as e:
            return f"【bocha工具出错：{e}】"

    return Tool(
        name="bocha_search",
        description="使用博查AI Web Search API进行搜索，返回摘要结果。",
        func=safe_bocha_search,
    )

def python_REPL():
    python_repl = PythonREPL()
    python_REPL_tool = Tool(
        name = "Calculator",
        description = "用于数学计算，例如计算百分比变化",
        func = python_repl.run,
    )
    return python_REPL_tool


