import numbers
from logger import logger

def filterBasedOnScoreThreshold(aiJsonOutput: dict, threshold):
    try:
        output=dict()
        for key, value in aiJsonOutput.items():
            if isinstance(value, list):
                output[key] = []
                for item in value:
                    if isinstance(item, dict) and isinstance(item.get("score"), numbers.Number):
                        if item.get("score") >= threshold :
                            output[key].append(item)
                    else:
                        output[key].append(item)
            elif isinstance(value, dict) and isinstance(value.get("score"), numbers.Number):
                if value.get("score") >= threshold:
                    output[key] = value
            else:
                output[key] = value
        return output
    except Exception as e:
        logger.exception("error in filterBasedOnScoreThreshold: %s", e)
        return aiJsonOutput

