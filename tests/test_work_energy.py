import pytest
from flask import Flask
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

# -------------------------------
# Test for Work (W = F * d)
# -------------------------------

def test_valid_work(app):
    with app.test_client() as client:
        response = client.post('/api/work_energy/work', json={'force': 10, 'distance': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 50  # 10 * 5 = 50


def test_missing_fields_work(app):
    """Test missing required fields for work calculation"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/work', json={'force': 10})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Missing required fields' in data['error']


def test_invalid_input_work(app):
    """Test for invalid input (non-numeric)"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/work', json={'force': 'invalid', 'distance': 5})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Invalid input' in data['error']


def test_zero_values_work(app):
    """Test zero values for force or distance"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/work', json={'force': 0, 'distance': 10})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 0  # 0 * 10 = 0


# -------------------------------
# Test for Power (P = W / t)
# -------------------------------

def test_valid_power(app):
    with app.test_client() as client:
        response = client.post('/api/work_energy/power', json={'work': 50, 'time': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 10  # 50 / 5 = 10


def test_missing_fields_power(app):
    """Test missing required fields for power calculation"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/power', json={'work': 50})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Missing required fields' in data['error']


def test_invalid_input_power(app):
    """Test for invalid input (non-numeric)"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/power', json={'work': 'invalid', 'time': 5})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Invalid input' in data['error']


def test_zero_values_power(app):
    """Test zero values for work or time"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/power', json={'work': 0, 'time': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 0  # 0 / 5 = 0


# -------------------------------
# Test for Kinetic Energy (KE = 1/2 * m * v^2)
# -------------------------------

def test_valid_kinetic(app):
    with app.test_client() as client:
        response = client.post('/api/work_energy/kinetic', json={'mass': 10, 'velocity': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 125  # 1/2 * 10 * 5^2 = 125


def test_missing_fields_kinetic(app):
    """Test missing required fields for kinetic energy calculation"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/kinetic', json={'mass': 10})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Missing required fields' in data['error']


def test_invalid_input_kinetic(app):
    """Test for invalid input (non-numeric)"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/kinetic', json={'mass': 'invalid', 'velocity': 5})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Invalid input' in data['error']


def test_zero_values_kinetic(app):
    """Test zero values for mass or velocity"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/kinetic', json={'mass': 10, 'velocity': 0})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 0  # 1/2 * 10 * 0^2 = 0


# -------------------------------
# Test for Potential Energy (PE = m * g * h)
# -------------------------------

def test_valid_potential(app):
    with app.test_client() as client:
        response = client.post('/api/work_energy/potential', json={'mass': 10, 'height': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 490.0  # 10 * 9.8 * 5 = 490.0


def test_missing_fields_potential(app):
    """Test missing required fields for potential energy calculation"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/potential', json={'mass': 10})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Missing required fields' in data['error']


def test_invalid_input_potential(app):
    """Test for invalid input (non-numeric)"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/potential', json={'mass': 'invalid', 'height': 5})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Invalid input' in data['error']


def test_zero_values_potential(app):
    """Test zero values for mass or height"""
    with app.test_client() as client:
        response = client.post('/api/work_energy/potential', json={'mass': 10, 'height': 0})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 0  # 10 * 0 = 0
