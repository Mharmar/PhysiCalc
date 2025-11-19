import pytest
from flask import Flask
from app import create_app

# Initialize the Flask app for testing
@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

# Test the /velocity endpoint
def test_velocity(app):
    with app.test_client() as client:
        response = client.post('/api/kinematics/velocity', json={'u': 0, 'a': 9.8, 't': 10})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 98  # 0 + 9.8 * 10 = 98

# Test the /displacement endpoint
def test_displacement(app):
    with app.test_client() as client:
        response = client.post('/api/kinematics/displacement', json={'u': 0, 'a': 9.8, 't': 10})
        data = response.get_json()
        assert response.status_code == 200
        # Round the result to 2 decimal places to avoid precision issues
        assert round(data['result'], 2) == 490.00  # 0 * 10 + 0.5 * 9.8 * (10 ** 2) = 490

# Test the /velocity_squared endpoint
def test_velocity_squared(app):
    with app.test_client() as client:
        response = client.post('/api/kinematics/velocity_squared', json={'u': 0, 'a': 9.8, 's': 19.6})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 384.16  # 0 + 2 * 9.8 * 19.6 = 384.16

# Test the /time endpoint
def test_time(app):
    with app.test_client() as client:
        response = client.post('/api/kinematics/time', json={'v': 98, 'u': 0, 'a': 9.8})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 10  # (98 - 0) / 9.8 = 10

# Test the /acceleration endpoint
def test_acceleration(app):
    with app.test_client() as client:
        response = client.post('/api/kinematics/acceleration', json={'v': 98, 'u': 0, 't': 10})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 9.8  # (98 - 0) / 10 = 9.8