from flask import Blueprint, request, jsonify
from app.formulas.work_energy import compute_work, compute_power, compute_kinetic_energy, compute_potential_energy
from app.utils.validator import validate_inputs
from app.utils.error_handler import handle_invalid_input_error, handle_missing_input_error, handle_zero_division_error, handle_generic_error

bp = Blueprint('work_energy', __name__, url_prefix='/api/work_energy')

# ------------------------
# Work: W = F * d
# ------------------------
@bp.route('/work', methods=['POST'])
def work_route():
    data = request.json
    required = ['force', 'distance']

    validation_result = validate_inputs(data, required)
    if validation_result is not True:
        return validation_result

    try:
        force = float(data['force'])
        distance = float(data['distance'])
        result = compute_work(force, distance)
    except (ValueError, TypeError):
        return handle_invalid_input_error("Invalid input")
    except Exception as e:
        return handle_generic_error(str(e))

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
    required = ['work', 'time']

    validation_result = validate_inputs(data, required)
    if validation_result is not True:
        return validation_result

    try:
        work = float(data['work'])
        time = float(data['time'])
        result = compute_power(work, time)
    except (ValueError, TypeError):
        return handle_invalid_input_error("Inputs must be numbers")
    except ZeroDivisionError:
        return handle_zero_division_error()
    except Exception as e:
        return handle_generic_error(str(e))

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
    required = ['mass', 'velocity']

    validation_result = validate_inputs(data, required)
    if validation_result is not True:
        return validation_result

    try:
        mass = float(data['mass'])
        velocity = float(data['velocity'])
        result = compute_kinetic_energy(mass, velocity)
    except (ValueError, TypeError):
        return handle_invalid_input_error("Inputs must be numbers")
    except Exception as e:
        return handle_generic_error(str(e))

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
    required = ['mass', 'height']

    validation_result = validate_inputs(data, required)
    if validation_result is not True:
        return validation_result

    try:
        mass = float(data['mass'])
        height = float(data['height'])
        result = compute_potential_energy(mass, height)
    except (ValueError, TypeError):
        return handle_invalid_input_error("Inputs must be numbers")
    except Exception as e:
        return handle_generic_error(str(e))

    return jsonify({
        "formula": "PE = m * g * h",
        "inputs": {"mass": mass, "height": height},
        "result": result
    })