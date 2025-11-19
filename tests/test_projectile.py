import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

# -------------------------------
# Test for Horizontal Range
# Formula: R = (u^2 * sin(2θ)) / g
# -------------------------------

def test_valid_range(app):
    with app.test_client() as client:
        # u = 10 m/s, angle = 45 degrees (max range)
        # R = (100 * sin(90)) / 9.8 = 100 / 9.8 ≈ 10.204
        response = client.post('/api/projectile/range', json={'u': 10, 'angle': 45})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == pytest.approx(10.204, 0.01)

def test_missing_fields_range(app):
    with app.test_client() as client:
        response = client.post('/api/projectile/range', json={'u': 10})
        assert response.status_code == 400
        assert 'Missing required fields' in response.get_json()['error']

def test_invalid_input_range(app):
    with app.test_client() as client:
        response = client.post('/api/projectile/range', json={'u': 'invalid', 'angle': 45})
        assert response.status_code == 400
        # FIX: Expect the standard "Invalid input" from validator
        assert 'Invalid input' in response.get_json()['error']

# -------------------------------
# Test for Time of Flight
# Formula: T = (2 * u * sinθ) / g
# -------------------------------

def test_valid_time_of_flight(app):
    with app.test_client() as client:
        # u = 10 m/s, angle = 30 degrees
        # sin(30) = 0.5
        # T = (2 * 10 * 0.5) / 9.8 = 10 / 9.8 ≈ 1.020
        response = client.post('/api/projectile/time', json={'u': 10, 'angle': 30})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == pytest.approx(1.020, 0.01)

def test_missing_fields_time(app):
    with app.test_client() as client:
        response = client.post('/api/projectile/time', json={'angle': 30})
        assert response.status_code == 400
        assert 'Missing required fields' in response.get_json()['error']

def test_invalid_input_time(app):
    with app.test_client() as client:
        response = client.post('/api/projectile/time', json={'u': 10, 'angle': 'fast'})
        assert response.status_code == 400
        # FIX: Expect the standard "Invalid input" from validator
        assert 'Invalid input' in response.get_json()['error']

# -------------------------------
# Test for Maximum Height
# Formula: H = (u^2 * sin^2θ) / (2g)
# -------------------------------

def test_valid_max_height(app):
    with app.test_client() as client:
        # u = 10 m/s, angle = 90 degrees (straight up)
        # sin(90) = 1
        # H = (100 * 1) / (2 * 9.8) = 100 / 19.6 ≈ 5.102
        response = client.post('/api/projectile/height', json={'u': 10, 'angle': 90})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == pytest.approx(5.102, 0.01)

def test_missing_fields_height(app):
    with app.test_client() as client:
        response = client.post('/api/projectile/height', json={'u': 10})
        assert response.status_code == 400
        assert 'Missing required fields' in response.get_json()['error']

def test_invalid_input_height(app):
    with app.test_client() as client:
        response = client.post('/api/projectile/height', json={'u': 'high', 'angle': 90})
        assert response.status_code == 400
        # FIX: Expect the standard "Invalid input" from validator
        assert 'Invalid input' in response.get_json()['error']