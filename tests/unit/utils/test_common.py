import pytest
import sys

sys.path.append("../src")
from field import Field

from utils.common import (
    has_repetitive_words,
    fix_arabic_text_in_output,
    fix_arabic_text_in_nested_output,
)


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("a cat in the hat", False),  # No repetitive words
        (
            "apple banana apple orange banana",
            True,
        ),  # Repetitive word: "apple" and "banana"
        ("hello world hello world", True),  # Repetitive word: "hello" and "world"
        ("one two three four", False),  # No repetitive words
        ("", False),  # Empty string
        ("hello", False),  # Single word
        ("apple Apple apple", True),  # Case-insensitive repetition
    ],
)
def test_has_repetitive_words(input_string, expected_result):
    assert has_repetitive_words(input_string) == expected_result


def test_fix_arabic_text_in_output():
    llmJson = {
        "field1": {"value": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23"},
        "field2": [
            {"value": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23"},
            {"value": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23"},
        ],
    }
    fields = [Field("field1"), Field("field2")]

    result = fix_arabic_text_in_output(llmJson, fields)

    assert result["field1"]["value"] == "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13"
    assert (
        result["field2"][0]["value"] == "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13"
    )
    assert (
        result["field2"][1]["value"] == "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13"
    )


def test_fix_arabic_text_in_nested_output():
    llmJson = {
        "field1": {"value": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23"},
        "field2": [
            {"value": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23"},
            {"value": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23"},
        ],
        "field3": {
            "subfield1": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23",
            "subfield2": {"value": "محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23"},
        },
    }

    result = fix_arabic_text_in_nested_output(llmJson)

    assert result == {
        "field1": {"value": "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13"},
        "field2": [
            {"value": "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13"},
            {"value": "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13"},
        ],
        "field3": {
            "subfield1": "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13",
            "subfield2": {"value": "محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13"},
        },
    }
