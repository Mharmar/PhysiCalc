import pytest
from flask import Flask
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

# -------------------------------
# Test for missing required fields
# -------------------------------

def test_missing_fields(app):
    """Test for missing required fields"""
    with app.test_client() as client:
        # Test missing "voltage" for current route
        response = client.post('/api/electricity/current', json={'resistance': 5})
        assert response.status_code == 400  # Should return 400 for missing fields
        assert 'Missing required fields' in response.get_json()['error']

# -------------------------------
# Test for invalid input types
# -------------------------------

def test_invalid_input(app):
    """Test for invalid input types"""
    with app.test_client() as client:
        # Test invalid "voltage" (string instead of float)
        response = client.post('/api/electricity/current', json={'voltage': 'invalid', 'resistance': 5})
        assert response.status_code == 400  # Should return 400 for invalid input
        assert 'Invalid input' in response.get_json()['error']

# -------------------------------
# Test for zero division error
# -------------------------------

def test_zero_division_error(app):
    """Test for division by zero errors"""
    with app.test_client() as client:
        # Test zero resistance
        response = client.post('/api/electricity/current', json={'voltage': 10, 'resistance': 0})
        assert response.status_code == 400
        assert 'Resistance cannot be zero' in response.get_json()['error']

        # Test zero current for resistance calculation
        response = client.post('/api/electricity/resistance', json={'voltage': 10, 'current': 0})
        assert response.status_code == 400
        assert 'Current cannot be zero' in response.get_json()['error']

# -------------------------------
# Test for missing or generic error handling
# -------------------------------

def test_generic_error(app):
    """Test for a generic unexpected error"""
    with app.test_client() as client:
        # Trigger a generic error by posting to a non-existent route
        response = client.post('/api/non_existent_route', json={})
        assert response.status_code == 404  # Expect 404 for non-existent route
