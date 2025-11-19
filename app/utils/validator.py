# app/utils/validator.py

from app.utils.error_handler import handle_missing_input_error, handle_invalid_input_error

def validate_inputs(data, required_fields):
    """
    Checks if all required fields exist and are numbers.
    Returns True if valid, otherwise calls the error handler.
    """
    for field in required_fields:
        value = data.get(field)
        if value is None:  # Check for missing field
            return handle_missing_input_error([field])  # Return missing field error immediately
        
        try:
            float(value)  # Try to convert to float
        except (ValueError, TypeError):  # Catch invalid types
            return handle_invalid_input_error("Invalid input")  # Return invalid input error if conversion fails

    return True  # Return True if all fields are valid
