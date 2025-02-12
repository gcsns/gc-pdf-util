import pytest
import sys

sys.path.append('../src')

from utils.validatedatatype import check_and_convert, validate_data_type
from field import Field, FieldType


@pytest.mark.parametrize("llmJson, fields, expected", [
    # valid single value field
    ({"number_field": {"value": "123"}, "other_field": { "value": "other_value" }}, [Field(name="number_field", type=FieldType.NUMBER)], {"number_field": {"value": 123}, "other_field": { "value": "other_value" }}),

    # invalid single value field
    ({"number_field": {"value": "123a"}, "other_field": { "value": "other_value" }}, [Field(name="number_field", type=FieldType.NUMBER)], {"other_field": { "value": "other_value" }}),

    # valid and invalid multi value field
    ({"number_field": [{"value": "123"}, {"value": "123s"}], "other_field": { "value": "other_value" }}, [Field(name="number_field", type=FieldType.NUMBER)], {"number_field": [{"value": 123}], "other_field": { "value": "other_value" }}),
])
def test_validate_data_type(llmJson, fields, expected):
    assert validate_data_type(llmJson, fields) == expected

# Define test cases
@pytest.mark.parametrize("value, field, expected", [
    # Test cases for FieldType.NUMBER
    (10, Field(name="test_field", type=FieldType.NUMBER, description="Test field", format=""), 10),
    ("10", Field(name="test_field", type=FieldType.NUMBER, description="Test field", format=""), 10),
    ("10.5", Field(name="test_field", type=FieldType.NUMBER, description="Test field", format=""), 10.5),
    ("abc", Field(name="test_field", type=FieldType.NUMBER, description="Test field", format=""), None),

    # Test cases for FieldType.DIGITS
    ("123", Field(name="test_field", type=FieldType.DIGITS, description="Test field", format=""), "123"),
    ("123.01", Field(name="test_field", type=FieldType.DIGITS, description="Test field", format=""), None),
    ("123abc", Field(name="test_field", type=FieldType.DIGITS, description="Test field", format=""), None),
    ("abc", Field(name="test_field", type=FieldType.DIGITS, description="Test field", format=""), None),

    # Test cases for FieldType.ALPHA
    ("abc", Field(name="test_field", type=FieldType.ALPHA, description="Test field", format=""), "abc"),
    ("123", Field(name="test_field", type=FieldType.ALPHA, description="Test field", format=""), None),
    ("abc123", Field(name="test_field", type=FieldType.ALPHA, description="Test field", format=""), None),

    # Test cases for FieldType.ALPHANUM
    ("abc123", Field(name="test_field", type=FieldType.ALPHANUM, description="Test field", format=""), "abc123"),
    ("123", Field(name="test_field", type=FieldType.ALPHANUM, description="Test field", format=""), "123"),
    ("abc", Field(name="test_field", type=FieldType.ALPHANUM, description="Test field", format=""), "abc"),
    ("abc123#", Field(name="test_field", type=FieldType.ALPHANUM, description="Test field", format=""), None),

    # Test cases for FieldType.IBAN
    ("DE89370400440532013000", Field(name="test_field", type=FieldType.IBAN, description="Test field", format=""), 'DE89370400440532013000'),
    ("DE8937040044053201300", Field(name="test_field", type=FieldType.IBAN, description="Test field", format=""), None),
    ("GB29NWBK60161331926819", Field(name="test_field", type=FieldType.IBAN, description="Test field", format=""), 'GB29NWBK60161331926819'),
    ("GB29NWBK6016133192681", Field(name="test_field", type=FieldType.IBAN, description="Test field", format=""), None),

    # Test cases for FieldType.REGEX
    ("abc123", Field(name="test_field", type=FieldType.REGEX, description="Test field", format="[a-z]+[0-9]+"), "abc123"),
    ("123abc", Field(name="test_field", type=FieldType.REGEX, description="Test field", format="[a-z]+[0-9]+"), None),

    # Test cases for FieldType.DATE
    ("2024-04-24", Field(name="test_field", type=FieldType.DATE, description="Test field", format="%Y-%m-%d"), "2024-04-24T00:00:00"),
    ("2024-04-24", Field(name="test_field", type=FieldType.DATE, description="Test field", format=None), "2024-04-24T00:00:00"),
    ("24-04-2024", Field(name="test_field", type=FieldType.DATE, description="Test field", format="%Y-%m-%d"), None),
    ("2024/04/24", Field(name="test_field", type=FieldType.DATE, description="Test field", format="%Y-%m-%d"), None),
])
def test_check_and_convert(value, field, expected):
    assert check_and_convert(value, field) == expected