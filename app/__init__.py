from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Simple root route to check if API is running
    @app.route("/")
    def home():
        return {"message": "PhysiCalc API is running!"}

    # Import blueprints
    from .routes import kinematics, projectile, work_energy, electricity, forces
    app.register_blueprint(kinematics.bp)
    app.register_blueprint(projectile.bp)
    app.register_blueprint(work_energy.bp)
    app.register_blueprint(electricity.bp)
    app.register_blueprint(forces.bp)
    
    return app