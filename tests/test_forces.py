import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

# -------------------------------
# Test for Normal Force (N = mg)
# -------------------------------

def test_valid_normal_force(app):
    with app.test_client() as client:
        response = client.post('/api/forces/normal', json={'mass': 10})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 98.0  # 10 * 9.8 = 98.0

def test_missing_fields_normal(app):
    with app.test_client() as client:
        response = client.post('/api/forces/normal', json={})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Missing required fields' in data['error']

def test_invalid_input_normal(app):
    with app.test_client() as client:
        response = client.post('/api/forces/normal', json={'mass': 'invalid'})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Invalid input' in data['error']

# -------------------------------
# Test for Frictional Force (F_f = μN)
# -------------------------------

def test_valid_friction(app):
    with app.test_client() as client:
        # mu = 0.5, Normal Force = 100
        response = client.post('/api/forces/friction', json={'mu': 0.5, 'normal_force': 100})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 50.0  # 0.5 * 100 = 50.0

def test_missing_fields_friction(app):
    with app.test_client() as client:
        response = client.post('/api/forces/friction', json={'mu': 0.5})
        data = response.get_json()
        assert response.status_code == 400
        assert 'Missing required fields' in data['error']

# -------------------------------
# Test for Tension Force (T = mg)
# -------------------------------

def test_valid_tension(app):
    with app.test_client() as client:
        response = client.post('/api/forces/tension', json={'mass': 5})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 49.0  # 5 * 9.8 = 49.0

def test_missing_fields_tension(app):
    with app.test_client() as client:
        response = client.post('/api/forces/tension', json={})
        assert response.status_code == 400

# -------------------------------
# Test for Applied Force (Returns input)
# -------------------------------

def test_valid_applied(app):
    with app.test_client() as client:
        response = client.post('/api/forces/applied', json={'force': 150})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == 150.0

def test_missing_fields_applied(app):
    with app.test_client() as client:
        response = client.post('/api/forces/applied', json={})
        assert response.status_code == 400

# -------------------------------
# Test for Gravitational Force (F = G * m1 * m2 / r^2)
# -------------------------------

def test_valid_gravitational(app):
    with app.test_client() as client:
        # m1=10, m2=10, r=1
        # F = 6.67430e-11 * (10 * 10) / 1^2 = 6.67430e-9
        response = client.post('/api/forces/gravitational', json={'m1': 10, 'm2': 10, 'r': 1})
        data = response.get_json()
        assert response.status_code == 200
        # Use pytest.approx for floating point comparisons
        assert data['result'] == pytest.approx(6.67430e-9)

def test_missing_fields_gravitational(app):
    with app.test_client() as client:
        response = client.post('/api/forces/gravitational', json={'m1': 10, 'm2': 10})
        assert response.status_code == 400
        assert 'Missing required fields' in response.get_json()['error']

# -------------------------------
# Test for Electromagnetic Force (F = k_e * q1 * q2 / r^2)
# -------------------------------

def test_valid_electromagnetic(app):
    with app.test_client() as client:
        # q1=1e-6, q2=1e-6, r=1
        # k_e = 8.9875e9
        # F = 8.9875e9 * (1e-6 * 1e-6) / 1^2 = 8.9875e9 * 1e-12 = 8.9875e-3
        response = client.post('/api/forces/electromagnetic', json={'q1': 1e-6, 'q2': 1e-6, 'r': 1})
        data = response.get_json()
        assert response.status_code == 200
        assert data['result'] == pytest.approx(8.9875e-3)

def test_missing_fields_electromagnetic(app):
    with app.test_client() as client:
        response = client.post('/api/forces/electromagnetic', json={'q1': 1e-6})
        assert response.status_code == 400