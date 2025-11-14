def validate_inputs(data, required_fields):
    """
    Checks if all required fields exist and are numbers.
    Returns True if valid, False otherwise.
    """
    for field in required_fields:
        value = data.get(field)
        if value is None:
            return False
        # Check if it can be converted to float
        try:
            float(value)
        except (TypeError, ValueError):
            return False
    return True