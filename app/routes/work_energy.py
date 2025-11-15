from flask import Blueprint, request, jsonify
from app.formulas.work_energy import compute_work, compute_power, compute_kinetic_energy, compute_potential_energy
from app.utils.validator import validate_inputs

bp = Blueprint('work_energy', __name__, url_prefix='/api/work_energy')


# ------------------------
# Work: W = F * d
# ------------------------
@bp.route('/work', methods=['POST'])
def work_route():
    data = request.json
    if not validate_inputs(data, ['force', 'distance']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        force = float(data['force'])
        distance = float(data['distance'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_work(force, distance)
    return jsonify({
        "formula": "W = F * d",
        "inputs": {"force": force, "distance": distance},
        "result": result
    })


# ------------------------
# Power: P = W / t
# ------------------------
@bp.route('/power', methods=['POST'])
def power_route():
    data = request.json
    if not validate_inputs(data, ['work', 'time']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        work = float(data['work'])
        time = float(data['time'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400
    try:
        result = compute_power(work, time)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "formula": "P = W / t",
        "inputs": {"work": work, "time": time},
        "result": result
    })


# ------------------------
# Kinetic Energy: KE = 1/2 * m * v^2
# ------------------------
@bp.route('/kinetic', methods=['POST'])
def kinetic_route():
    data = request.json
    if not validate_inputs(data, ['mass', 'velocity']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        mass = float(data['mass'])
        velocity = float(data['velocity'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_kinetic_energy(mass, velocity)
    return jsonify({
        "formula": "KE = 1/2 * m * v^2",
        "inputs": {"mass": mass, "velocity": velocity},
        "result": result
    })


# ------------------------
# Potential Energy: PE = m * g * h
# ------------------------
@bp.route('/potential', methods=['POST'])
def potential_route():
    data = request.json
    if not validate_inputs(data, ['mass', 'height']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        mass = float(data['mass'])
        height = float(data['height'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_potential_energy(mass, height)
    return jsonify({
        "formula": "PE = m * g * h",
        "inputs": {"mass": mass, "height": height},
        "result": result
    })