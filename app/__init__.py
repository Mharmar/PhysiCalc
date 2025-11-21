from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    CORS(app)  # Optional: for Cross-Origin Resource Sharing if needed
    
    # Initialize Swagger
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    
    template = {
        "swagger": "2.0",
        "info": {
            "title": "PhysiCalc API",
            "description": "A modular physics calculation engine for Kinematics, Forces, Electricity, and more.",
            "version": "1.0.0"
        }
    }

    Swagger(app, config=swagger_config, template=template)

    # Import blueprints
    from app.routes import kinematics, projectile, work_energy, electricity, forces
    app.register_blueprint(kinematics.bp)
    app.register_blueprint(projectile.bp)
    app.register_blueprint(work_energy.bp)
    app.register_blueprint(electricity.bp)
    app.register_blueprint(forces.bp)
    
    return app