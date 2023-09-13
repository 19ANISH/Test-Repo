import pytest
import requests
def test_get_endpoint():
    response = requests.get('http://localhost:8000/')
    #pass the link for requests.get() to get it tested	
    assert response.status_code == 200
    # You can also check the response payload or other attributes using assertions
    # For example, assert response.json() == expected_data

