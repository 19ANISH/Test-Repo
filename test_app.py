import pytest
import requests
def test_get_endpoint():
    response = requests.get('http://localhost:8000/view_file/19ANISH/ADS//README.md')
    assert response.status_code == 200
    # You can also check the response payload or other attributes using assertions
    # For example, assert response.json() == expected_data

