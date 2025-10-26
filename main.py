from agents.llm_agent import create_llm_agent

def main():
    agent, ask = create_llm_agent()
    print("\n对话Agent已启动，输入问题开始对话（输入 exit 退出）")
    while True:
        query = input("\n你：")
        if query.lower() in ["exit", "quit"]:
            print("结束会话。")
            break
        response = ask(query)
        print("\nAgent：", response["output"])

if __name__ == "__main__":
    main()