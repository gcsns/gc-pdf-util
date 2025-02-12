import copy
from field import Field, FieldType
import re
import datetime
import requests
import configs

def validate_data_type(llmJson: dict, fields: list[Field]) -> dict:
    validationFields = list(filter(lambda field: field.type and llmJson.get(field.name), fields))

    if not len(validationFields):
        return llmJson

    validatedResult = copy.deepcopy(llmJson)

    for field in validationFields:
        valueDictOrListOfDict = validatedResult.get(field.name)
        
        if not valueDictOrListOfDict:
            continue
        
        if isinstance(valueDictOrListOfDict, list):
            toBeRemoved = []
            for i, valueDict in enumerate(valueDictOrListOfDict):
                value = valueDict.get("value") if valueDict else None
                if not value is None:
                    value = check_and_convert(value, field)
                if value is None:
                    toBeRemoved.append(i)
                else:
                    valueDict["value"] = value

            for i in reversed(toBeRemoved):
                valueDictOrListOfDict.pop(i)

        elif isinstance(valueDictOrListOfDict, dict):
            value = valueDictOrListOfDict.get("value")
            if not value is None:
                value = check_and_convert(value, field)
            if value is None:
                validatedResult.pop(field.name)
            else:
                valueDictOrListOfDict["value"] = value

    return validatedResult

def check_and_convert(value, field: Field) -> str|float|None:
    """
    Checks whether a given value is valid for a specific type of field.

    Args:
        value: The value to be validated.
        field: The field object containing information about the field type and format.

    Returns:
        The value if it is valid for the field type, otherwise None.
    """
    if field.type == FieldType.NUMBER:
        try:
            return float(value)
        except ValueError:
            return None
    elif field.type == FieldType.DIGITS:
        return value if str(value).isdigit() else None
    elif field.type == FieldType.ALPHA:
        return value if str(value).isalpha() else None
    elif field.type == FieldType.ALPHANUM:
        return value if str(value).isalnum() else None
    elif field.type == FieldType.IBAN:
        try:
            iban = value.replace(' ', '').upper()
            response = requests.get(url=f"{configs.IBAN_VALIDATION_BASE_URL}{iban}")
            # Documentation for the api in https://openiban.com/IBAN. 
            data = response.json()
            valid = data['valid']
            return iban if valid else None
        except Exception:
            return None
    elif field.type == FieldType.REGEX:
        # Assuming the format field contains a valid regex pattern
        return value if re.match(field.format, str(value)) is not None else None
    elif field.type == FieldType.DATE:
        # Assuming the format field contains a valid date format string
        try:
            date  = datetime.datetime.strptime(str(value), field.format) if field.format else datetime.datetime.fromisoformat(str(value))
            return date.isoformat()
        except ValueError:
            return None
    else:
        return value  # no validation for unkown types. treating them as any or blank type
