from flask import Blueprint, request, jsonify
from app.formulas.kinematics import compute_velocity

bp = Blueprint('kinematics', __name__, url_prefix='/api/kinematics')

@bp.route('/velocity', methods=['POST'])
def velocity():
    data = request.json
    u = data.get('u')
    a = data.get('a')
    t = data.get('t')
    if u is None or a is None or t is None:
        return jsonify({"error": "Missing input values"}), 400
    
    # Convert to float and handle conversion errors
    try:
        u_float = float(u)
        a_float = float(a)
        t_float = float(t)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input values - must be numbers"}), 400
    
    result = compute_velocity(u_float, a_float, t_float)
    return jsonify({"result": result})