from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Import blueprints
    from .routes import kinematics, projectile
    app.register_blueprint(kinematics.bp)
    app.register_blueprint(projectile.bp)
    
    return app