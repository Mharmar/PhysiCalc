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
    """
    Calculate Normal Force (N)
    ---
    tags:
      - Forces
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - mass
          properties:
            mass:
              type: number
              description: Mass (kg)
              example: 10
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Normal Force (Newtons)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['mass']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        mass = float(data['mass'])
        result = compute_normal_force(mass)
    except (ValueError, TypeError) as e:
        return handle_invalid_input_error(str(e))
    
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
    """
    Calculate Frictional Force (F_f)
    ---
    tags:
      - Forces
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - mu
            - normal_force
          properties:
            mu:
              type: number
              description: Coefficient of Friction (μ)
              example: 0.5
            normal_force:
              type: number
              description: Normal Force (N)
              example: 98
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Frictional Force (Newtons)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['mu', 'normal_force']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        mu = float(data['mu'])
        normal_force = float(data['normal_force'])
        result = compute_frictional_force(mu, normal_force)
    except (ValueError, TypeError) as e:
        return handle_invalid_input_error(str(e))
    
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
    """
    Calculate Tension Force (T)
    ---
    tags:
      - Forces
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - mass
          properties:
            mass:
              type: number
              description: Mass (kg)
              example: 5
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Tension Force (Newtons)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['mass']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        mass = float(data['mass'])
        result = compute_tension_force(mass)
    except (ValueError, TypeError) as e:
        return handle_invalid_input_error(str(e))
    
    return jsonify({
        "formula": "T = mg",
        "inputs": {"mass": mass},
        "result": result
    })


# ------------------------
# Applied Force: F = Applied force
# ------------------------
@bp.route('/applied', methods=['POST'])
def applied():
    """
    Return Applied Force
    ---
    tags:
      - Forces
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - force
          properties:
            force:
              type: number
              description: The applied force value
              example: 150
    responses:
      200:
        description: Successful return
        schema:
          type: object
          properties:
            result:
              type: number
              description: Applied Force (Newtons)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['force']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        force = float(data['force'])
        result = compute_applied_force(force)
    except (ValueError, TypeError) as e:
        return handle_invalid_input_error(str(e))
    
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
    """
    Calculate Gravitational Force
    ---
    tags:
      - Forces
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - m1
            - m2
            - r
          properties:
            m1:
              type: number
              description: Mass 1 (kg)
              example: 5.972e24
            m2:
              type: number
              description: Mass 2 (kg)
              example: 7.348e22
            r:
              type: number
              description: Distance (m)
              example: 384400000
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Gravitational Force (Newtons)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['m1', 'm2', 'r']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        m1 = float(data['m1'])
        m2 = float(data['m2'])
        r = float(data['r'])
        result = compute_gravitational_force(m1, m2, r)
    except (ValueError, TypeError) as e:
        return handle_invalid_input_error(str(e))
    
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
    """
    Calculate Electromagnetic Force
    ---
    tags:
      - Forces
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - q1
            - q2
            - r
          properties:
            q1:
              type: number
              description: Charge 1 (Coulombs)
              example: 1.602e-19
            q2:
              type: number
              description: Charge 2 (Coulombs)
              example: -1.602e-19
            r:
              type: number
              description: Distance (m)
              example: 5.29e-11
    responses:
      200:
        description: Successful calculation
        schema:
          type: object
          properties:
            result:
              type: number
              description: Electromagnetic Force (Newtons)
      400:
        description: Invalid input
    """
    data = request.json
    required = ['q1', 'q2', 'r']

    validation = validate_inputs(data, required)
    if validation is not True:
        return validation

    try:
        q1 = float(data['q1'])
        q2 = float(data['q2'])
        r = float(data['r'])
        result = compute_electromagnetic_force(q1, q2, r)
    except (ValueError, TypeError) as e:
        return handle_invalid_input_error(str(e))
    
    return jsonify({
        "formula": "F = k_e * (q1 * q2) / r^2",
        "inputs": {"q1": q1, "q2": q2, "r": r},
        "result": result
    })