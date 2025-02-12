from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models import BaseChatModel
from langchain_aws import ChatBedrock
from botocore.config import Config
import configs
from .beta_azure_openai import BetaAzureOpenAI
from .beta_chat_openai import BetaChatOpenAI

def get_llm(model_name: str, fetchStructuredOutput: bool = False) -> BaseChatModel:
    if model_name.startswith('gpt'):
        max_tokens = 4096 
        if(model_name == 'gpt-3.5-turbo'):
            max_tokens = 3000
        if(model_name == 'gpt-4o-2024-08-06' or model_name == 'gpt-4o'):
            max_tokens = 16384
        if (fetchStructuredOutput):
            return BetaChatOpenAI(model_name=model_name, temperature=0, max_tokens=max_tokens)
        return ChatOpenAI(model_name=model_name, temperature=0, max_tokens=max_tokens)
    if model_name.startswith('claude'):
        return ChatAnthropic(model_name=model_name, temperature=0, max_tokens_to_sample=8192)
    if model_name.startswith('gemini'):
        return ChatGoogleGenerativeAI(model=model_name, temperature=0)
    if model_name.startswith('bedrock:'):
        model_id = model_name[8:]
        return ChatBedrock(model_id=model_id, model_kwargs={"temperature":0, "max_tokens": 8192}, config=Config(read_timeout=configs.BEDROCK_TIMEOUT))
    if model_name.startswith('azure:'):
        azure_deployment = model_name[6:]
        max_tokens = 16384 
        if(azure_deployment == 'gpt-3-5'):
            max_tokens = 3000
        if (fetchStructuredOutput):
            return BetaAzureOpenAI(model_name=azure_deployment, temperature=0, max_tokens=max_tokens)
        return AzureChatOpenAI(azure_deployment=azure_deployment, temperature=0, max_tokens=max_tokens)
    raise Exception(f'Invalid llm model: {model_name}')
