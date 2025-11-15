def compute_current(voltage, resistance):
    """Compute current I = V / R"""
    if resistance == 0:
        raise ValueError("Resistance cannot be zero")
    return voltage / resistance


def compute_voltage(current, resistance):
    """Compute voltage V = I * R"""
    return current * resistance


def compute_resistance(voltage, current):
    """Compute resistance R = V / I"""
    if current == 0:
        raise ValueError("Current cannot be zero")
    return voltage / current


def compute_power(voltage=None, current=None, resistance=None):
    """
    Compute power using available variables:
    P = V * I
    P = I^2 * R
    P = V^2 / R
    Must provide at least two arguments.
    """
    if voltage is not None and current is not None:
        return voltage * current
    elif current is not None and resistance is not None:
        return current ** 2 * resistance
    elif voltage is not None and resistance is not None:
        if resistance == 0:
            raise ValueError("Resistance cannot be zero")
        return voltage ** 2 / resistance
    else:
        raise ValueError("Not enough values to compute power")