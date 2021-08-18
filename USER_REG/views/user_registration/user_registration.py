from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from USER_REG.models.user_registeration.user_registration import User_registration
from USER_REG.extensions.extensions import jwt
from flask import *
user_registration_bluePrint = Blueprint("user_registration_bluePrint", __name__)


@user_registration_bluePrint.route("/register", methods=["POST"])
@jwt_required()
def register_user():
    json_data = request.get_json()
    name = json_data["name"]
    email = json_data["email"]
    password = json_data["password"]
    confirm_password = json_data["cnf_password"]
    if name == "":
        return jsonify(message="Enter Name First")
    if email == "":
        return jsonify(message="Enter Email First")
    if password == "":
        return jsonify(message="Enter Password First")
    if confirm_password == "":
        return jsonify(message="Enter Confirm Password First")
    if password != confirm_password:
        return jsonify(message="Password and confirm password must be same")
    # if User_registration.objects(email=email).First() is not None:
    #     return jsonify(message="User Already Registered")
    if name == "" or email == "" or password == "" or confirm_password == "":
        return jsonify(message="Please Fill Required Fields")
    else:
        user_registration = User_registration()
        user_registration.email = email
        user_registration.name = name
        user_registration.password = password
        user_registration.confirm_password = confirm_password
        user_registration.save()
        return jsonify(message="User Successfully Registered", id_=str(user_registration.id))


@user_registration_bluePrint.route("/search", methods=["GET"])
def get_register_user():
    json_data = request.get_json()
    user_id = json_data["user_id"]
    if not user_id:
        return jsonify(message="Id is Required")
    user_registration_data = User_registration.objects(id=user_id)
    # get() returns  objects
    # and without get it returns list of objects
    print(user_registration_data)
    if not user_registration_data:
        return jsonify(message="no data found")
    data = []
    for items in user_registration_data:
        data.append({
            "name": items.name,
            "email": items.email,
            "password": items.password,
            "cnf_password": items.confirm_password
        })
    return jsonify(data)


@user_registration_bluePrint.route("/delete", methods=["DELETE"])
def delete():
    json_data = request.get_json()
    user_id = json_data["user_id"]
    if user_id == "":
        return jsonify(message="Enter id to delete user")
    try:
        user_data = User_registration.objects(id=user_id)
        if user_data:
            user_data.delete()
            return jsonify(message="deleted successfully")
        else:
            return jsonify(message="Data does not exist")
    except Exception as err:
        return jsonify(message=str(err))


@user_registration_bluePrint.route("/edit", methods=["PUT"])
def edit_user():
    json_data = request.get_json()
    user_id = json_data["user_id"]
    if not user_id:
        return jsonify(message="Enter user id first")
    user_data = User_registration.objects(id=user_id).get()
    if user_data:
        name = json_data["name"]
        email = json_data["email"]
        password = json_data["password"]
        confirm_password = json_data["cnf_password"]
        if not name:
            return jsonify(message="Enter user name first")
        if not email:
            return jsonify(message="Enter user Email first")
        if not password:
            return jsonify(message="Enter user password first")
        if not confirm_password:
            return jsonify(message="Enter confirm password first")
        if password != confirm_password:
            return jsonify(message="Password and confirm password must be same")
        user_data.update(
            name=name,
            email=email,
            password=password,
            confirm_password=confirm_password
        )
        return jsonify(message="User Updated Successfully")


@user_registration_bluePrint.route("/partial", methods=["PATCH"])
def edit_partial_user():
    json_data = request.get_json()
    user_id = json_data["user_id"]
    if not user_id:
        return jsonify(message="Enter user id first")
    try:
        user_data = User_registration.objects(id=user_id).get()
        if user_data:
            name = json_data["name"]
            email = json_data["email"]
            password = json_data["password"]
            confirm_password = json_data["cnf_password"]
            user_data.update(
                name=name,
                email=email,
                password=password,
                confirm_password=confirm_password
                )
            return jsonify(message="Updated Successfully")
    except Exception as err:
        return jsonify(message=str(err))
