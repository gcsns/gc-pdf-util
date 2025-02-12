import sys
import pytest

sys.path.append('../src')

from utils.findandparsejsonobject import findAndParseJsonObject 

def test_findAndParseJsonObject():
    input_str = "This is some text {\"key\": \"value\"} followed by more text"
    expected_output = {"key": "value"}
    assert findAndParseJsonObject(input_str) == expected_output

    # input_str = "Some text {\"key1\": \"value1\"} in between {\"key2\": \"value2\"} more text"
    # expected_output = {"key1": "value1"}
    # assert Ocr.findAndParseJsonObject(input_str) == expected_output

    input_str = "This is some text without JSON content"
    with pytest.raises(Exception):
        findAndParseJsonObject(input_str)

    input_str = "Some text {\"key\": \"value\" but missing closing bracket"
    with pytest.raises(Exception):
        findAndParseJsonObject(input_str)
