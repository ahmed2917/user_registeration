import datetime
from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token

from USER_REG.models.user_registeration.user_registration import User_registration

user_login_blueprint = Blueprint("user_login_blueprint", __name__)


@user_login_blueprint.route("/logins", methods=["POST"])
def user_login_function():
    json_data = request.get_json()
    email = json_data["email"]
    password = json_data["password"]
    if not email:
        return jsonify(message="Enter Email First")
    if not password:
        return jsonify(message="Enter Password First")
    if User_registration.objects(email=email):
        user_login = User_registration.objects(email=email).get()
        if user_login.password == password:
            print("matched", password)
            expires = datetime.timedelta(days=30)
            access_token = create_access_token(identity=email, expires_delta=expires)
            return jsonify(message="Login Succeeded!", access_token=access_token, user_id=str(user_login.id))
