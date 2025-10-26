import os
from dotenv import load_dotenv
from langchain.agents import agent

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

# 记忆配置
MEMORY_TYPE = "buffer_window" # buffer_window | buffer
MEMORY_K = 10 # 记忆窗口大小

# LLM配置
MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.0

# RAG配置
RAG_DATA_PATH = r"D:\desktop\ChenAgent_1.1\agents\retriever\data"  # RAG原始数据存放位置
RAG_DB_PATH = r"D:\desktop\ChenAgent_1.1\agents\retriever\chroma_db"
RAG_CHUNK_SIZE = 500
RAG_CHUNK_OVERLAP = 50
RAG_TOP_K = 3
RAG_NEED_REBUILD = True  # 是否更新RAG知识

# Tool配置
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
BOCHA_API_KEY = os.getenv("BOCHA_API_KEY")
BOCHA_BASE_URL = os.getenv("BOCHA_BASE_URL")

# Agent配置
AGENT_TYPER = "CONVERSATIONAL_REACT_DESCRIPTION"
AGENT_VERBOSE = True