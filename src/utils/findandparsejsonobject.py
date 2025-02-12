import json
from logger import logger

def findAndParseJsonObject(input_str: str)-> dict:
    """
    parses input string as json object. strips any character before first '{' and after last '}' before parsing
    """
    start_pos = 0
    end_pos = None
    json_string = input_str
    if input_str[0] !=  '{':
        start_pos = input_str.find('{')
    if input_str[-1] != '}':
        end_pos = input_str.rfind('}')
    if start_pos != 0 or end_pos != None:
        logger.debug('findAndParseJsonObject->start_pos: %s %s %s', start_pos, 'end_pos:', end_pos)
        if start_pos == -1 or end_pos == -1:
            raise Exception('seems string doesn\'t contain a valid json object')
        json_string = input_str[start_pos:None if end_pos == None else end_pos + 1]
    return json.loads(json_string)

