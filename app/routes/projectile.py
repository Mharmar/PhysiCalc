from flask import Blueprint, request, jsonify
from app.formulas.projectile import compute_range, compute_time_of_flight, compute_max_height
from app.utils.validator import validate_inputs
from app.utils.error_handler import (
    handle_invalid_input_error,
    handle_missing_input_error,
    handle_zero_division_error,
    handle_generic_error,
)

bp = Blueprint('projectile', __name__, url_prefix='/api/projectile')


# ------------------------
# Horizontal Range: R = (u^2 * sin(2θ)) / g
# ------------------------
@bp.route('/range', methods=['POST'])
def range_route():
    """
    Calculate Horizontal Range (R)
    ---
    tags:
      - Projectile Motion
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - u
            - angle
          properties:
            u:
              type: number
              description: Initial Velocity (m/s)
              example: 20
            angle:
              type: number
              description: Angle of projection (degrees)
              example: 45
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Range (meters)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['u', 'angle']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        u = float(data['u'])
        angle = float(data['angle'])
        result = compute_range(u, angle)
    except (ValueError, TypeError):
        return handle_invalid_input_error("Inputs must be numbers")
    except Exception as e:
        return handle_generic_error(str(e))

    return jsonify({
        "formula": "R = (u^2 * sin(2θ)) / g",
        "inputs": {"u": u, "angle": angle},
        "result": result
    })


# ------------------------
# Time of Flight: T = (2 * u * sinθ) / g
# ------------------------
@bp.route('/time', methods=['POST'])
def time_route():
    """
    Calculate Time of Flight (T)
    ---
    tags:
      - Projectile Motion
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - u
            - angle
          properties:
            u:
              type: number
              description: Initial Velocity (m/s)
              example: 20
            angle:
              type: number
              description: Angle of projection (degrees)
              example: 30
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Time (seconds)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['u', 'angle']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        u = float(data['u'])
        angle = float(data['angle'])
        result = compute_time_of_flight(u, angle)
    except (ValueError, TypeError):
        return handle_invalid_input_error("Inputs must be numbers")
    except Exception as e:
        return handle_generic_error(str(e))

    return jsonify({
        "formula": "T = (2 * u * sinθ) / g",
        "inputs": {"u": u, "angle": angle},
        "result": result
    })


# ------------------------
# Maximum Height: H = (u^2 * sin^2θ) / (2g)
# ------------------------
@bp.route('/height', methods=['POST'])
def height_route():
    """
    Calculate Maximum Height (H)
    ---
    tags:
      - Projectile Motion
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - u
            - angle
          properties:
            u:
              type: number
              description: Initial Velocity (m/s)
              example: 20
            angle:
              type: number
              description: Angle of projection (degrees)
              example: 60
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Maximum Height (meters)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['u', 'angle']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        u = float(data['u'])
        angle = float(data['angle'])
        result = compute_max_height(u, angle)
    except (ValueError, TypeError):
        return handle_invalid_input_error("Inputs must be numbers")
    except Exception as e:
        return handle_generic_error(str(e))

    return jsonify({
        "formula": "H = (u^2 * sin^2θ) / (2g)",
        "inputs": {"u": u, "angle": angle},
        "result": result
    })