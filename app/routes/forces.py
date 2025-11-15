from flask import Blueprint, request, jsonify
from app.formulas.forces import (
    compute_normal_force,
    compute_frictional_force,
    compute_tension_force,
    compute_applied_force,
    compute_gravitational_force,
    compute_electromagnetic_force
)
from app.utils.validator import validate_inputs
from app.utils.error_handler import handle_invalid_input_error, handle_missing_input_error, handle_zero_division_error, handle_generic_error

bp = Blueprint('forces', __name__, url_prefix='/api/forces')

# ------------------------
# Normal Force: N = mg
# ------------------------
@bp.route('/normal', methods=['POST'])
def normal():
    data = request.json
    if not validate_inputs(data, ['mass']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        mass = float(data['mass'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_normal_force(mass)
    return jsonify({
        "formula": "N = mg",
        "inputs": {"mass": mass},
        "result": result
    })

# ------------------------
# Frictional Force: F_f = μN
# ------------------------
@bp.route('/friction', methods=['POST'])
def friction():
    data = request.json
    if not validate_inputs(data, ['mu', 'normal_force']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        mu = float(data['mu'])
        normal_force = float(data['normal_force'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_frictional_force(mu, normal_force)
    return jsonify({
        "formula": "F_f = μN",
        "inputs": {"mu": mu, "normal_force": normal_force},
        "result": result
    })

# ------------------------
# Tension Force: T = mg
# ------------------------
@bp.route('/tension', methods=['POST'])
def tension():
    data = request.json
    if not validate_inputs(data, ['mass']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        mass = float(data['mass'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_tension_force(mass)
    return jsonify({
        "formula": "T = mg",
        "inputs": {"mass": mass},
        "result": result
    })

# ------------------------
# Applied Force: F = Applied force (given directly)
# ------------------------
@bp.route('/applied', methods=['POST'])
def applied():
    data = request.json
    if not validate_inputs(data, ['force']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        force = float(data['force'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_applied_force(force)
    return jsonify({
        "formula": "F = Applied force",
        "inputs": {"force": force},
        "result": result
    })

# ------------------------
# Gravitational Force: F = G * (m1 * m2) / r^2
# ------------------------
@bp.route('/gravitational', methods=['POST'])
def gravitational():
    data = request.json
    if not validate_inputs(data, ['m1', 'm2', 'r']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        m1 = float(data['m1'])
        m2 = float(data['m2'])
        r = float(data['r'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_gravitational_force(m1, m2, r)
    return jsonify({
        "formula": "F = G * (m1 * m2) / r^2",
        "inputs": {"m1": m1, "m2": m2, "r": r},
        "result": result
    })

# ------------------------
# Electromagnetic Force: F = k_e * (q1 * q2) / r^2
# ------------------------
@bp.route('/electromagnetic', methods=['POST'])
def electromagnetic():
    data = request.json
    if not validate_inputs(data, ['q1', 'q2', 'r']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        q1 = float(data['q1'])
        q2 = float(data['q2'])
        r = float(data['r'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_electromagnetic_force(q1, q2, r)
    return jsonify({
        "formula": "F = k_e * (q1 * q2) / r^2",
        "inputs": {"q1": q1, "q2": q2, "r": r},
        "result": result
    })
