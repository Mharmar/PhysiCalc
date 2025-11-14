from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Import blueprints
    from .routes import kinematics, projectile, work_energy
    app.register_blueprint(kinematics.bp)
    app.register_blueprint(projectile.bp)
    app.register_blueprint(work_energy.bp)
    
    return app