from enum import Enum
import csv
from io import StringIO


class FieldType(str, Enum):
    NUMBER = 'number'
    DIGITS = 'digits'
    ALPHA = 'alpha'
    ALPHANUM = 'alphanum'
    IBAN = 'iban'
    REGEX = 'regex'
    DATE = 'date'

class Field:
    name: str
    type: FieldType
    description: str
    format: str # regex in case type is regex and date format in case type is date
    def __init__(self, name: str, type: FieldType | None = None, description: str| None = None, format: str| None= None):
        self.name = name
        self.type = type
        self.description = description
        self.format = format

def parse_field(field: str) -> Field:
    """
    parses input string as Field

    The input string can represent a field in one of three formats:
    <name>:<type>:<description>: This format represents a field with a name, type, and description. The type should be one of the possible values defined in the FieldType enumeration. For regex type will be regex-<regular expression> 
    <name>: This format represents a field with only a name.
    <name>:<type>: This format represents a field with a name and type only.
    <name>:<description>: This format represents a field with a name and description only.
    """
    parts = list(csv.reader(StringIO(field), delimiter=":", escapechar="\\"))[0]
    name = parts[0]
    type = None
    description = None
    format = None

    # Check if type and description are provided
    if len(parts) >= 3:
        type = parts[1]
        description = ":".join(parts[2:]) # consider 3rd separator onwards as part of description

    # Check if only type is provided
    elif len(parts) == 2:
        if parts[1] in list(FieldType) or parts[1].startswith('regex-') or parts[1].startswith('date-'):
            type = parts[1]
        else:
            description = parts[1]

    # If type starts with 'regex-', it's a regex type
    if type and (type.startswith('regex-') or type.startswith('date-')):
        type_parts = type.split('-', 1)
        type = type_parts[0]
        format = type_parts[1]
    if type and not type in list(FieldType):
        raise ValueError(f"Invalid field type: {type}")

    return Field(name, type, description, format)