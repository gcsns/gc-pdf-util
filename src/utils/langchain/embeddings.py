from langchain_community.embeddings import HuggingFaceBgeEmbeddings, VoyageEmbeddings, BedrockEmbeddings, HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings
from langchain_nomic import NomicEmbeddings
import configs

def get_embeddings(embedding_model: str):
    splitted = embedding_model.split(":", 1)
    model_name = None
    if(len(splitted) > 1):
        model_name = splitted[1]
    if embedding_model.startswith('hf-bge'):
        if model_name:
            return HuggingFaceBgeEmbeddings(model_name=model_name)
        return HuggingFaceBgeEmbeddings()
    elif embedding_model.startswith('azure'):
        if model_name:
            return AzureOpenAIEmbeddings(azure_deployment=model_name)
    elif embedding_model.startswith('nomic'):
        return NomicEmbeddings(model=model_name)
    elif embedding_model.startswith('voyage'):
        return VoyageEmbeddings(model=model_name)
    elif embedding_model.startswith('bedrock'):
        return BedrockEmbeddings(model_id=model_name)
    elif embedding_model.startswith('openai'):
        return OpenAIEmbeddings(model=model_name)
    elif embedding_model.startswith('hf'):
        if model_name:
            return HuggingFaceEmbeddings(model_name=model_name, model_kwargs={"trust_remote_code": True})
        return HuggingFaceEmbeddings()
    raise Exception(f'Invalid embedding model: {embedding_model}')
