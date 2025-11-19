import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

# -------------------------------
# Test for Current (I = V / R)
# -------------------------------

def test_valid_current(app):
    with app.test_client() as client:
        # V=10, R=2 -> I=5
        response = client.post('/api/electricity/current', json={'voltage': 10, 'resistance': 2})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 5.0

def test_missing_fields_current(app):
    with app.test_client() as client:
        response = client.post('/api/electricity/current', json={'voltage': 10})
        assert response.status_code == 400
        assert 'Missing required fields' in response.get_json()['error']

def test_invalid_input_current(app):
    with app.test_client() as client:
        response = client.post('/api/electricity/current', json={'voltage': 'invalid', 'resistance': 2})
        assert response.status_code == 400
        assert 'Invalid input' in response.get_json()['error']

def test_zero_resistance_current(app):
    with app.test_client() as client:
        response = client.post('/api/electricity/current', json={'voltage': 10, 'resistance': 0})
        assert response.status_code == 400
        assert 'Resistance cannot be zero' in response.get_json()['error']

# -------------------------------
# Test for Voltage (V = I * R)
# -------------------------------

def test_valid_voltage(app):
    with app.test_client() as client:
        # I=5, R=2 -> V=10
        response = client.post('/api/electricity/voltage', json={'current': 5, 'resistance': 2})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 10.0

def test_missing_fields_voltage(app):
    with app.test_client() as client:
        response = client.post('/api/electricity/voltage', json={'current': 5})
        assert response.status_code == 400
        assert 'Missing required fields' in response.get_json()['error']

def test_invalid_input_voltage(app):
    with app.test_client() as client:
        response = client.post('/api/electricity/voltage', json={'current': 5, 'resistance': 'invalid'})
        assert response.status_code == 400
        assert 'Invalid input' in response.get_json()['error']

# -------------------------------
# Test for Resistance (R = V / I)
# -------------------------------

def test_valid_resistance(app):
    with app.test_client() as client:
        # V=10, I=5 -> R=2
        response = client.post('/api/electricity/resistance', json={'voltage': 10, 'current': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 2.0

def test_missing_fields_resistance(app):
    with app.test_client() as client:
        response = client.post('/api/electricity/resistance', json={'voltage': 10})
        assert response.status_code == 400
        assert 'Missing required fields' in response.get_json()['error']

def test_zero_current_resistance(app):
    with app.test_client() as client:
        # Current cannot be zero for resistance calc
        response = client.post('/api/electricity/resistance', json={'voltage': 10, 'current': 0})
        assert response.status_code == 400
        assert 'Current cannot be zero' in response.get_json()['error']

# -------------------------------
# Test for Power (Multiple Formulas)
# -------------------------------

def test_valid_power_vi(app):
    """Test P = V * I"""
    with app.test_client() as client:
        response = client.post('/api/electricity/power', json={'voltage': 10, 'current': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 50.0  # 10 * 5

def test_valid_power_i2r(app):
    """Test P = I^2 * R"""
    with app.test_client() as client:
        response = client.post('/api/electricity/power', json={'current': 2, 'resistance': 10})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 40.0  # 2^2 * 10 = 4 * 10 = 40

def test_valid_power_v2r(app):
    """Test P = V^2 / R"""
    with app.test_client() as client:
        response = client.post('/api/electricity/power', json={'voltage': 10, 'resistance': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 20.0  # 10^2 / 5 = 100 / 5 = 20

def test_not_enough_values_power(app):
    """Test error when only 1 variable is provided"""
    with app.test_client() as client:
        response = client.post('/api/electricity/power', json={'voltage': 10})
        assert response.status_code == 400
        assert 'Not enough values' in response.get_json()['error']

def test_zero_resistance_power(app):
    """Test error when calculating P = V^2 / R with R=0"""
    with app.test_client() as client:
        response = client.post('/api/electricity/power', json={'voltage': 10, 'resistance': 0})
        assert response.status_code == 400
        assert 'Resistance cannot be zero' in response.get_json()['error']

def test_invalid_input_power(app):
    with app.test_client() as client:
        response = client.post('/api/electricity/power', json={'voltage': 'invalid', 'current': 5})
        assert response.status_code == 400
        assert 'Invalid input' in response.get_json()['error']