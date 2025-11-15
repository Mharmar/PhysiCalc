from flask import Blueprint, request, jsonify
from app.formulas.kinematics import (
    compute_velocity,
    compute_displacement,
    compute_velocity_squared,
    compute_time,
    compute_acceleration
)
from app.utils.validator import validate_inputs

bp = Blueprint('kinematics', __name__, url_prefix='/api/kinematics')


# ------------------------
# Final Velocity: v = u + a * t
# ------------------------
@bp.route('/velocity', methods=['POST'])
def velocity():
    data = request.json
    required = ['u', 'a', 't']
    if not validate_inputs(data, required):
        return jsonify({"error": "Missing or invalid input values"}), 400

    u = float(data['u'])
    a = float(data['a'])
    t = float(data['t'])
    result = compute_velocity(u, a, t)

    return jsonify({
        "formula": "v = u + a * t",
        "inputs": {"u": u, "a": a, "t": t},
        "result": result
    })


# ------------------------
# Displacement: s = ut + 1/2 * a * t^2
# ------------------------
@bp.route('/displacement', methods=['POST'])
def displacement():
    data = request.json
    required = ['u', 'a', 't']
    if not validate_inputs(data, required):
        return jsonify({"error": "Missing or invalid input values"}), 400

    u = float(data['u'])
    a = float(data['a'])
    t = float(data['t'])
    result = compute_displacement(u, a, t)

    return jsonify({
        "formula": "s = u * t + 0.5 * a * t^2",
        "inputs": {"u": u, "a": a, "t": t},
        "result": result
    })


# ------------------------
# Final Velocity Squared: v^2 = u^2 + 2 * a * s
# ------------------------
@bp.route('/velocity_squared', methods=['POST'])
def velocity_squared():
    data = request.json
    required = ['u', 'a', 's']
    if not validate_inputs(data, required):
        return jsonify({"error": "Missing or invalid input values"}), 400

    u = float(data['u'])
    a = float(data['a'])
    s = float(data['s'])
    result = compute_velocity_squared(u, a, s)

    return jsonify({
        "formula": "v^2 = u^2 + 2 * a * s",
        "inputs": {"u": u, "a": a, "s": s},
        "result": result
    })


# ------------------------
# Time: t = (v - u) / a
# ------------------------
@bp.route('/time', methods=['POST'])
def time():
    data = request.json
    required = ['v', 'u', 'a']
    if not validate_inputs(data, required):
        return jsonify({"error": "Missing or invalid input values"}), 400

    v = float(data['v'])
    u = float(data['u'])
    a = float(data['a'])
    result = compute_time(v, u, a)

    return jsonify({
        "formula": "t = (v - u) / a",
        "inputs": {"v": v, "u": u, "a": a},
        "result": result
    })


# ------------------------
# Acceleration: a = (v - u) / t
# ------------------------
@bp.route('/acceleration', methods=['POST'])
def acceleration():
    data = request.json
    required = ['v', 'u', 't']
    if not validate_inputs(data, required):
        return jsonify({"error": "Missing or invalid input values"}), 400

    v = float(data['v'])
    u = float(data['u'])
    t = float(data['t'])
    result = compute_acceleration(v, u, t)

    return jsonify({
        "formula": "a = (v - u) / t",
        "inputs": {"v": v, "u": u, "t": t},
        "result": result
    })