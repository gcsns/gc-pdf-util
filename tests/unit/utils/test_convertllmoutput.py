import pytest
import sys
sys.path.append('../src')

from utils.convertllmoutput import convert_llm_output, convert_llm_list_output, convert_llm_single_output

def test_convert_llm_single_output():
    # Test when value is a dictionary
    value = {"value": "test", "score": 0.5}
    expected_output = {"value": "test", "score": 0.5}
    assert convert_llm_single_output(value) == expected_output
    
    # Test when value is not a dictionary
    value = "test"
    expected_output = {"value": "test"}
    assert convert_llm_single_output(value) == expected_output
    
    # Test with score provided
    value = "test"
    score = 0.8
    expected_output = {"value": "test", "score": 0.8}
    assert convert_llm_single_output(value, score) == expected_output

def test_convert_llm_list_output():
    # Test when values are dictionaries
    values = [{"value": "test1", "score": 0.5}, {"value": "test2", "score": 0.7}]
    expected_output = [{"value": "test1", "score": 0.5}, {"value": "test2", "score": 0.7}]
    assert convert_llm_list_output(values) == expected_output
    
    # Test when values are not dictionaries
    values = ["test1", "test2"]
    expected_output = [{"value": "test1"}, {"value": "test2"}]
    assert convert_llm_list_output(values) == expected_output

def test_convert_llm_output():
    # Test with valid input
    input = {
        "key1": [{"value": "test1", "score": 0.5}, {"value": "test2", "score": 0.7}],
        "key2": {"value": "test", "score": 0.8}
    }
    expected_output = input
    assert convert_llm_output(input) == expected_output
    
    # Test with invalid input
    input = {
        "key1": "invalid",
        "key2": {"value": "test", "score": 0.8}
    }
    expected_output = {
        "key1": {"value": "invalid"},
        "key2": {"value": "test", "score": 0.8}
    }
    assert convert_llm_output(input) == expected_output

    input = {
        "key1": ["invalid", "invalid2"],
        "key2": {"value": "test", "score": 0.8}
    }
    expected_output = {
        "key1": [{"value": "invalid"}, {"value": "invalid2"}],
        "key2": {"value": "test", "score": 0.8}
    }
    assert convert_llm_output(input) == expected_output

    input = {
        "key1": {"value": ["invalid", "invalid2"], "score": 0.7},
        "key2": {"value": "test", "score": 0.8}
    }
    expected_output = {
        "key1": [{"value": "invalid", "score": 0.7}, {"value": "invalid2", "score": 0.7}],
        "key2": {"value": "test", "score": 0.8}
    }
    assert convert_llm_output(input) == expected_output
