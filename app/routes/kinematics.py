from flask import Blueprint, request, jsonify
from app.formulas.kinematics import (
    compute_velocity,
    compute_displacement,
    compute_velocity_squared,
    compute_time,
    compute_acceleration
)
from app.utils.validator import validate_inputs
from app.utils.error_handler import handle_invalid_input_error, handle_missing_input_error, handle_zero_division_error, handle_generic_error

bp = Blueprint('kinematics', __name__, url_prefix='/api/kinematics')


# ------------------------
# Final Velocity: v = u + a * t
# ------------------------
@bp.route('/velocity', methods=['POST'])
def velocity():
    data = request.json
    required = ['u', 'a', 't']
    
    # FIX: Check if result is explicitly not True
    validation = validate_inputs(data, required)
    if validation is not True:
        return validation
        
    try:
        u = float(data['u'])
        a = float(data['a'])
        t = float(data['t'])
        result = compute_velocity(u, a, t)
    except ValueError as e:
        return handle_invalid_input_error(str(e))
        
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
    
    # FIX: Check if result is explicitly not True
    validation = validate_inputs(data, required)
    if validation is not True:
        return validation
        
    try:
        u = float(data['u'])
        a = float(data['a'])
        t = float(data['t'])
        result = compute_displacement(u, a, t)
    except ValueError as e:
        return handle_invalid_input_error(str(e))
        
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
    
    # FIX: Check if result is explicitly not True
    validation = validate_inputs(data, required)
    if validation is not True:
        return validation
        
    try:
        u = float(data['u'])
        a = float(data['a'])
        s = float(data['s'])
        v_squared = compute_velocity_squared(u, a, s)
        final_velocity = round(v_squared ** 0.5, 2)
    except ValueError as e:
        return handle_invalid_input_error(str(e))
        
    return jsonify({
        "formula": "v^2 = u^2 + 2 * a * s",
        "inputs": {"u": u, "a": a, "s": s},
        "result": v_squared,
        "final_velocity": final_velocity
    })


# ------------------------
# Time: t = (v - u) / a
# ------------------------
@bp.route('/time', methods=['POST'])
def time():
    data = request.json
    required = ['v', 'u', 'a']
    
    # FIX: Check if result is explicitly not True
    validation = validate_inputs(data, required)
    if validation is not True:
        return validation
        
    try:
        v = float(data['v'])
        u = float(data['u'])
        a = float(data['a'])
        result = compute_time(v, u, a)
    except ValueError as e:
        return handle_invalid_input_error(str(e))
        
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
    
    # FIX: Check if result is explicitly not True
    validation = validate_inputs(data, required)
    if validation is not True:
        return validation
        
    try:
        v = float(data['v'])
        u = float(data['u'])
        t = float(data['t'])
        result = compute_acceleration(v, u, t)
    except ValueError as e:
        return handle_invalid_input_error(str(e))
        
    return jsonify({
        "formula": "a = (v - u) / t",
        "inputs": {"v": v, "u": u, "t": t},
        "result": result
    })