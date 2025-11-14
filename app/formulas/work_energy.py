def compute_work(force, distance):
    """Compute work W = F * d"""
    return force * distance

def compute_power(work, time):
    """Compute power P = W / t"""
    if time == 0:
        raise ValueError("Time cannot be zero")
    return work / time

def compute_kinetic_energy(mass, velocity):
    """Compute kinetic energy KE = 1/2 * m * v^2"""
    return 0.5 * mass * velocity ** 2

def compute_potential_energy(mass, height, g=9.8):
    """Compute potential energy PE = m * g * h"""
    return mass * g * height
