def compute_velocity(u, a, t):
    """Compute final velocity v = u + a * t"""
    return u + a * t

def compute_displacement(u, a, t):
    """Compute displacement s = u * t + 0.5 * a * t^2"""
    return (u * t) + (0.5 * a * (t ** 2))

def compute_velocity_squared(u, a, s):
    """Compute final velocity squared v^2 = u^2 + 2 * a * s"""
    return (u ** 2) + (2 * a * s)

def compute_time(v, u, a):
    """Compute time t = (v - u) / a"""
    return (v - u) / a

def compute_acceleration(v, u, t):
    """Compute acceleration a = (v - u) / t"""
    return (v - u) / t
