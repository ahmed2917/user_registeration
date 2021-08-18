from flask import Flask
from flask_cors import CORS
from USER_REG import config


def create_app(config_file="config.py"):
    app = Flask(__name__)
    CORS(app)
    app.config.from_pyfile(config_file)

    from USER_REG.extensions.extensions import db
    db.init_app(app)

    from USER_REG.extensions.extensions import jwt
    jwt.init_app(app)

    from .views.user_registration.user_registration import user_registration_bluePrint
    app.register_blueprint(user_registration_bluePrint)

    from .views.login.login import user_login_blueprint
    app.register_blueprint(user_login_blueprint)
    return app
