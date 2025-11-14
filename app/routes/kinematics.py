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
    result = compute_velocity(u, a, t)
    return jsonify({"result": result})
