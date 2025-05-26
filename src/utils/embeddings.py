from agno.embedder.openai import OpenAIEmbedder
from agno.embedder.azure_openai import AzureOpenAIEmbedder
from logger import logger

def get_embeddings(embedding_model: str):
    splitted = embedding_model.split(":", 1)
    model_name = None
    if(len(splitted) > 1):
        model_name = splitted[1]
    if embedding_model.startswith('openai'):
        return OpenAIEmbedder(id=model_name) 
    elif embedding_model.startswith('azure'):
        return AzureOpenAIEmbedder(id=model_name) 
    raise Exception(f'Invalid embedding model: {embedding_model}')
