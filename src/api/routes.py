import os  
from flask import Flask ,request, jsonify, Blueprint 
from api.models import db, User 
from flask_jwt_extended import create_access_token, get_jwt_identify, jew_required 
from flask_jwt_extended import JWTManager  

api = Blueprint('api', __name__)


@api.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    password = request.json.get('password')

    if user.query.fliter_by(email=email).first():
        return jsonify(message='Email already registered'), 200

        new-user = User(email, first_name=first_name ,last_name=last_name,password=password, is_active=Ture)

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify(message='failed to register user'), 200

        return jsonify(message='User register successfully'), 200

@api.route('/login', methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.fliter_by(email=email),first()
    if user is None or not user.check_password(password):
        return jsonify({"msg": "Incorrect email or password"}, 401)

        access_token = create_access_token(identify=email)
        return jsonify(access_token=access_token)

@api.route('/logout', methods=['POST, GET'])
def logout():
    return jsonify(message='User logged out successfully'), 200

@api.route('/protected', methods=[GET])
@jwt_required()
def protected():
    current_user_id = get_jwt_identify()
    user = User.query.get(current_user_id)

    return jsonify({"id": user.id,"username": user.username}), 200