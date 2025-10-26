import requests
import json
from langchain.tools import Tool
from dotenv import load_dotenv
import config

def bocha_search_run(query: str) -> str:

    api_key = config.BOCHA_API_KEY
    base_url = config.BOCHA_BASE_URL


    if not api_key:
        return " 未配置 BOCHA_API_KEY，请在 .env 中设置。"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "query": query,
        "summary": True,  # 启用摘要
        "count": 5        # 返回 5 条结果
    }

    try:
        response = requests.post(base_url, headers=headers, data=json.dumps(payload), timeout=15)
        response.raise_for_status()
        data = response.json()

        # 解析结果
        pages = data.get("data", {}).get("webPages", {}).get("value", [])
        if not pages:
            return "未检索到结果。"

        results_text = []
        for i, item in enumerate(pages[:5], 1):
            name = item.get("name", "")
            url = item.get("url", "")
            summary = item.get("summary", "")
            results_text.append(f"[{i}] {name}\n{summary}\n{url}")

        return "\n\n".join(results_text)

    except requests.exceptions.RequestException as e:
        return f"调用博查接口异常：{repr(e)}"
    except Exception as e:
        return f"解析博查结果时出错：{repr(e)}"