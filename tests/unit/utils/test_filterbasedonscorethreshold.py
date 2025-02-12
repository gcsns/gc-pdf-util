import sys

sys.path.append('../src')

from utils.filterbasedonscorethreshold import filterBasedOnScoreThreshold 

def test_filterBasedOnScoreThreshold():
    # Test case where all scores are above the threshold
    input_data = {
        "name": [
            {"value": "John Smith", "score": 0.98},
            {"value": "Alice Johnson", "score": 0.95}
        ],
        "id": {"value": "1234", "score": 0.99}
    }
    expected_output = input_data
    assert filterBasedOnScoreThreshold(input_data, 0.9) == expected_output

    # Test case where some scores are below the threshold
    input_data = {
        "name": [
            {"value": "John Smith", "score": 0.88},
            {"value": "Alice Johnson", "score": 0.95}
        ],
        "id": {"value": "1234", "score": 0.99}
    }
    expected_output = {
        "name": [{"value": "Alice Johnson", "score": 0.95}],
        "id": {"value": "1234", "score": 0.99}
    }
    assert filterBasedOnScoreThreshold(input_data, 0.9) == expected_output
