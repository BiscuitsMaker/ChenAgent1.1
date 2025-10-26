# ChenAgent 1.1

一个基于 LangChain 的智能对话 Agent 系统，集成了多种工具和知识检索功能。
作者：Chensx
更改：在1.0的基础上，将RAG嵌入，不再作为工具调用，即默认走一遍RAG；RAG的原始数据存放位置 "agents/retriever/data",可同时存放三种文件：md、pdf、txt。

## 功能特性

- 🤖 **智能对话**: 基于 GPT-4o-mini 的对话能力
- 🔍 **知识检索**: 本地向量数据库 RAG 检索
- 🌐 **网络搜索**: 集成 Tavily 和博查 AI 搜索工具
- 🧮 **计算工具**: Python REPL 计算器
- 💾 **记忆管理**: 支持对话历史记忆
- ⚙️ **灵活配置**: 可配置的模型参数和工具

## 项目结构

```
ChenAgent_1.1/
├── agents/                    # Agent 核心模块
│   ├── llm_agent.py          # LLM Agent 主逻辑
│   ├── memory/               # 记忆管理
│   │   └── memory.py         # 对话记忆实现
│   ├── retriever/            # 知识检索
│   │   ├── retriever.py      # 向量数据库检索
│   │   ├── data/             # 知识库数据
│   │   └── chroma_db/        # Chroma 向量数据库
│   └── tools/                # 工具集合
│       ├── tools.py          # 工具定义
│       └── bocha/            # 博查 AI 搜索工具
├── main.py                   # 主程序入口
├── config.py                 # 配置文件
├── requirements.txt          # 依赖包
└── README.md                 # 项目说明
```

## 安装依赖

1. 克隆项目到本地
2. 安装 Python 依赖：

```bash
pip install -r requirements.txt
```

## 环境配置

创建 `.env` 文件并配置以下环境变量：

```env
# OpenAI 配置
OPENAI_API_KEY=your_openai_api_key
OPENAI_BASE_URL=your_openai_base_url

# 搜索工具配置
TAVILY_API_KEY=your_tavily_api_key
BOCHA_API_KEY=your_bocha_api_key
BOCHA_BASE_URL=your_bocha_base_url
```

## 使用方法

### 启动对话 Agent

```bash
python main.py
```

启动后，你可以与 Agent 进行对话：
- 输入问题开始对话
- 输入 `exit` 或 `quit` 退出程序

### 配置说明

在 `config.py` 中可以调整以下参数：

- **LLM 配置**:
  - `MODEL_NAME`: 使用的模型名称
  - `TEMPERATURE`: 模型温度参数

- **记忆配置**:
  - `MEMORY_TYPE`: 记忆类型 (`buffer_window` | `buffer`)
  - `MEMORY_K`: 记忆窗口大小

- **RAG 配置**:
  - `RAG_DATA_PATH`: 知识库数据文件路径
  - `RAG_DB_PATH`: 向量数据库存储路径
  - `RAG_CHUNK_SIZE`: 文档分块大小
  - `RAG_TOP_K`: 检索返回的文档数量

## 核心功能

### 1. 知识检索 (RAG)
- 基于 Chroma 向量数据库
- 支持本地文档检索
- 自动检测文档更新并重建索引

### 2. 工具集成
- **Tavily 搜索**: 互联网信息检索
- **博查 AI 搜索**: 中文搜索优化
- **Python 计算器**: 数学计算和数据处理

### 3. 记忆管理
- 支持滑动窗口记忆
- 可配置记忆长度
- 保持对话上下文

## 开发说明

### 添加新工具

1. 在 `agents/tools/` 目录下创建工具模块
2. 在 `tools.py` 中注册新工具
3. 在 `llm_agent.py` 中启用工具

### 自定义知识库

1. 将文档放入 `agents/retriever/data/` 目录
2. 修改 `config.py` 中的 `RAG_DATA_PATH`
3. 重启程序自动重建向量数据库

## 技术栈

- **LangChain**: Agent 框架
- **OpenAI**: 大语言模型
- **Chroma**: 向量数据库
- **Tavily**: 网络搜索
- **Python**: 计算工具

## 注意事项

- 确保已正确配置所有必需的 API 密钥
- 首次运行时会自动构建向量数据库
- 建议定期更新知识库数据
- 工具执行异常时会自动处理并返回错误信息

## 许可证

本项目仅供学习和研究使用。