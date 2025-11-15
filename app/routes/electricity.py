from flask import Blueprint, request, jsonify
from app.formulas.electricity import compute_current, compute_voltage, compute_resistance, compute_power
from app.utils.validator import validate_inputs
from app.utils.error_handler import handle_invalid_input_error, handle_missing_input_error, handle_zero_division_error, handle_generic_error

bp = Blueprint('electricity', __name__, url_prefix='/api/electricity')


@bp.route('/current', methods=['POST'])
def current_route():
    data = request.json
    if not validate_inputs(data, ['voltage', 'resistance']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        voltage = float(data['voltage'])
        resistance = float(data['resistance'])
        result = compute_current(voltage, resistance)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({
        "formula": "I = V / R",
        "inputs": {"voltage": voltage, "resistance": resistance},
        "result": result
    })


@bp.route('/voltage', methods=['POST'])
def voltage_route():
    data = request.json
    if not validate_inputs(data, ['current', 'resistance']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        current = float(data['current'])
        resistance = float(data['resistance'])
        result = compute_voltage(current, resistance)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({
        "formula": "V = I * R",
        "inputs": {"current": current, "resistance": resistance},
        "result": result
    })


@bp.route('/resistance', methods=['POST'])
def resistance_route():
    data = request.json
    if not validate_inputs(data, ['voltage', 'current']):
        return jsonify({"error": "Missing or invalid input values"}), 400
    try:
        voltage = float(data['voltage'])
        current = float(data['current'])
        result = compute_resistance(voltage, current)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({
        "formula": "R = V / I",
        "inputs": {"voltage": voltage, "current": current},
        "result": result
    })


@bp.route('/power', methods=['POST'])
def power_route():
    data = request.json
    try:
        voltage = float(data['voltage']) if 'voltage' in data else None
        current = float(data['current']) if 'current' in data else None
        resistance = float(data['resistance']) if 'resistance' in data else None
        result = compute_power(voltage, current, resistance)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({
        "formula": "P = V * I OR P = I^2 * R OR P = V^2 / R",
        "inputs": {"voltage": voltage, "current": current, "resistance": resistance},
        "result": result
    })