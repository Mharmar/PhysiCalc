from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Optional: for Cross-Origin Resource Sharing if needed
    
    # Import blueprints
    from app.routes import kinematics, projectile, work_energy, electricity, forces
    app.register_blueprint(kinematics.bp)
    app.register_blueprint(projectile.bp)
    app.register_blueprint(work_energy.bp)
    app.register_blueprint(electricity.bp)
    app.register_blueprint(forces.bp)
    
    return app
