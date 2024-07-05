from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    JWTManager(app)
    
    with app.app_context():
        from models import User, Post
        db.create_all()
    
    from app import register_routes
    register_routes(app)
    
    return app

app = create_app()
