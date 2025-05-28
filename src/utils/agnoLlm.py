from agno.models.openai import OpenAIChat
from agno.models.azure import AzureOpenAI
from agno.models.aws.claude import Claude
from agno.models.anthropic import Claude as AnthropicClaude
from logger import logger
import configs

def get_llm(llm: str, temperature: float = 0.0, structured_outputs = False):
    splitted = llm.split(":", 1)
    model_name = None
    if(len(splitted) > 1):
        model_name = splitted[1]
    if llm.startswith('openai'):
        return OpenAIChat(
            id=model_name, 
            temperature=temperature,
            ) 
    elif llm.startswith('azure'):
        model = AzureOpenAI(
            id=configs.AZURE_OPENAI_MODEL_NAME,
            api_key=configs.AZURE_OPENAI_API_KEY,
            azure_endpoint=configs.AZURE_OPENAI_ENDPOINT,
            azure_deployment=configs.AZURE_OPENAI_DEPLOYMENT,
            temperature=temperature,
        )
        return model
    elif llm.startswith('claude'):
        model = Claude(
            id=model_name,
            temperature=temperature,
            cache_system_prompt=True,
            )
        return model
    elif llm.startswith('anthropic'):
        model = AnthropicClaude(
            id=model_name,
            temperature=temperature,
        )
        return model
    raise Exception(f'Invalid model: {llm}')
