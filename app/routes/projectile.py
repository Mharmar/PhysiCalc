from flask import Blueprint, request, jsonify
from app.formulas.projectile import compute_range, compute_time_of_flight, compute_max_height
from app.utils.validator import validate_inputs

bp = Blueprint('projectile', __name__, url_prefix='/api/projectile')

@bp.route('/range', methods=['POST'])
def range_route():
    data = request.json
    if not validate_inputs(data, ['u', 'angle']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        u = float(data['u'])
        angle = float(data['angle'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_range(u, angle)
    return jsonify({"result": result})

@bp.route('/time', methods=['POST'])
def time_route():
    data = request.json
    if not validate_inputs(data, ['u', 'angle']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        u = float(data['u'])
        angle = float(data['angle'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_time_of_flight(u, angle)
    return jsonify({"result": result})

@bp.route('/height', methods=['POST'])
def height_route():
    data = request.json
    if not validate_inputs(data, ['u', 'angle']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        u = float(data['u'])
        angle = float(data['angle'])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    result = compute_max_height(u, angle)
    return jsonify({"result": result})