import base64
from fastapi.testclient import TestClient
from unittest.mock import patch
from fastapi import FastAPI
from routes.finance_report_gen import router  # Adjust path as needed

# Initialize the FastAPI app
app = FastAPI()
app.include_router(router)

# Initialize TestClient with the app
client = TestClient(app)  # Correct initialization of TestClient

def test_generate_financial_analysis_route():
    dummy_md = "# This is a markdown test"
    base64_md = base64.b64encode(dummy_md.encode("utf-8")).decode("utf-8")

    # Patch the correct location where the function is being used (not where it's defined)
    with patch("routes.finance_report_gen.generate_financial_analysis") as mock_generate:
        mock_generate.return_value = "# Generated Financial Analysis"  # Mock return value

        # Send the post request to the endpoint
        response = client.post(
            "/annual-report/generate-full-markdown",
            json={"mdStrings": [base64_md]},  # This works correctly
        )

    # Check the response status and returned data
    assert response.status_code == 200
    result = response.json()

    # Ensure the expected result is in the response
    assert "mdString" in result
    decoded = base64.b64decode(result["mdString"]).decode("utf-8")
    assert "# Generated Financial Analysis" in decoded
