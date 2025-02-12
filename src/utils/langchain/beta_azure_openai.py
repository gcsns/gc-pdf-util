from munch import DefaultMunch
from openai import AzureOpenAI
import copy

class BetaAzureOpenAI:
    def __init__(self, model_name, temperature, max_tokens):
        self.model_name,=model_name, 
        self.temperature=temperature, 
        self.max_tokens=max_tokens
        self.openAI = AzureOpenAI()

    def invoke(self, messages, json_schema):
        if(json_schema): 
            response = self.openAI.beta.chat.completions.parse(
                model= self.model_name,
                messages= messages,
                response_format=json_schema,
                max_tokens=self.max_tokens
            )
        else:
            response = self.openAI.beta.chat.completions.parse(
                model= self.model_name,
                messages= messages,
                max_tokens=self.max_tokens
            )

        # Extract metadata by removing content
        metadata = copy.deepcopy(response)
        del metadata.choices[0].message
        final_response = {
            "content" : response.choices[0].message.content,
            "response_metadata" : metadata
            }
        return DefaultMunch.fromDict(final_response)