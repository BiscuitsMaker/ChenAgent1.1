from langchain.memory import ConversationBufferWindowMemory, ConversationBufferMemory
import config

def create_memory(memory_type: str = "buffer_window"):
    if memory_type == "buffer_window":
        memory = ConversationBufferWindowMemory(
            k=config.MEMORY_K,               
            memory_key="chat_history",
            input_key="input",
            return_messages=True  
        )
    elif memory_type == "buffer":
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            input_key="input",
            return_messages=True 
        )
    else:
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            input_key="input",
            return_messages=True 
        )
    
    return memory

