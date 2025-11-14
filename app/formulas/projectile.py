import math

def compute_range(u, angle_deg):
    """Compute horizontal range R = (u^2 * sin(2θ)) / g"""
    g = 9.8
    angle_rad = math.radians(angle_deg)
    return (u ** 2) * math.sin(2 * angle_rad) / g

def compute_time_of_flight(u, angle_deg):
    """Compute time of flight T = (2 * u * sinθ) / g"""
    g = 9.8
    angle_rad = math.radians(angle_deg)
    return (2 * u * math.sin(angle_rad)) / g

def compute_max_height(u, angle_deg):
    """Compute max height H = (u^2 * sin^2θ) / (2g)"""
    g = 9.8
    angle_rad = math.radians(angle_deg)
    return (u ** 2) * (math.sin(angle_rad) ** 2) / (2 * g)
