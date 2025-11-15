# CONTACT FORCE

def compute_normal_force(mass, g=9.8):
    """Normal Force: N = mg"""
    return mass * g

def compute_frictional_force(mu, normal_force):
    """Frictional Force: F_f = μN"""
    return mu * normal_force

def compute_tension_force(mass, g=9.8):
    """Tension Force: T = mg"""
    return mass * g

def compute_applied_force(force):
    """Applied Force: F = Applied force (usually given directly in the problem)"""
    return force

# NON - CONTACT FORCE

def compute_gravitational_force(m1, m2, r):
    """Gravitational Force: F = G * (m1 * m2) / r^2"""
    G = 6.67430e-11  # Gravitational constant
    return G * (m1 * m2) / r**2

def compute_electromagnetic_force(q1, q2, r):
    """Electromagnetic Force: F = k_e * (q1 * q2) / r^2"""
    k_e = 8.9875e9  # Coulomb's constant
    return k_e * (q1 * q2) / r**2