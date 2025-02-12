from munch import DefaultMunch
from openai import OpenAI

class BetaChatOpenAI:
    def __init__(self, model_name, temperature, max_tokens):
        self.model_name=model_name, 
        self.temperature=temperature, 
        self.max_tokens=max_tokens
        self.openAI = OpenAI()

    def invoke(self, messages, withStructuredOutput):
        return self.openAI.beta.chat.completions.parse(
            model=self.model_name,
            messages= messages,
            response_format=withStructuredOutput
        ).choices[0].message