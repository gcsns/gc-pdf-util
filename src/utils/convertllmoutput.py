from typing import TypedDict
import logger

class Value(TypedDict):
    value: float | str
    score: float

def convert_llm_output(aiJsonOutput: dict)->dict:
    try:
        output=dict()
        for key, value in aiJsonOutput.items():
            if isinstance(value, list):
                output[key] = convert_llm_list_output(value)
            else:
                output[key] = convert_llm_single_output(value)
        return output
    except Exception as e:
        logger.exception("error in convert_llm_output: %s", e)
        return aiJsonOutput
    
def convert_llm_list_output(values: list, score=None, isTranslated=None)-> list[Value]:
    return [convert_llm_single_output(value, score, isTranslated) for value in values]

def convert_llm_single_output(value, score=None, isTranslated=None)-> Value:
    if isinstance(value, dict):
        value_value = value.get("value")
        if isinstance(value_value, list):
            return convert_llm_list_output(value_value, value.get("score"), value.get("isTranslated"))
        return value
    output = { "value": value }
    if score:
        output["score"] = score
    if isTranslated is not None:
        output["isTranslated"] = isTranslated
    return output

