from flask import jsonify

def handle_zero_division_error():
    """Handles division by zero errors gracefully."""
    return jsonify({"error": "Division by zero is not allowed"}), 400

def handle_invalid_input_error(message="Invalid input"):
    """Handles invalid input errors."""
    return jsonify({"error": message}), 400

def handle_missing_input_error(required_fields):
    """Handles missing input errors."""
    return jsonify({"error": f"Missing required fields: {', '.join(required_fields)}"}), 400

def handle_generic_error(message="An unexpected error occurred"):
    """Handles generic errors."""
    return jsonify({"error": message}), 500