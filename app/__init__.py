from flask import Flask
from .db import db, migrate
from .models import planet, moon   
from .routes.planet_routes import bp as planets_bp
from .routes.moon_routes import bp as moons_bp
import os
from dotenv import load_dotenv

load_dotenv()


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(planets_bp)
    app.register_blueprint(moons_bp)

    return app
