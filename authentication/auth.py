from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from flask_jwt_extended  import set_access_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from main.models import db, User


authentication = Blueprint('authentication', __name__)

@authentication.route('/signup', methods=['POST'])
def sign():
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')

    Missing_fields = []

    if not firstname:
        Missing_fields.append('firstname')
    if not lastname:
        Missing_fields.append('lastname')
    if not email:
        Missing_fields.append('email')
    if not password:
        Missing_fields.append('password')


    if Missing_fields:   
           return jsonify({"Error": f"Missing_fields: {Missing_fields}"}), 400
        
        
        #Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "Email already exists"}), 400
        
    #hash the password, making it invisible
    hashed_password = generate_password_hash(password)

    #saves user info in the database
    new_user = User(firstname=firstname, lastname=lastname, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Account created successfuly'}), 201


#login route 
@authentication.route('/login', methods=['POST'])
def log():
       
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        #FIX THIS MISSING FIELDS 
        Missing_fields = []
        if not email:
             Missing_fields.append('email')
        if not password:
             Missing_fields.append('password')
        if Missing_fields:
             jsonify({"Error": f"Missing_fields: {Missing_fields}"}), 400
        
        #find a user by email 
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
             return jsonify({'message': 'User not found'}), 400
        
        
        response = jsonify({'msg': 'logged in successfully'})
        #create an access token for the user to verify their identity when visiting a protected route
        access_token = create_access_token(identity=email)
        set_access_cookies(response, access_token)
        return response
     
