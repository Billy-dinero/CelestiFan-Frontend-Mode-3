import sys
import os 
# Ensure the parent directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from flask_jwt_extended import JWTManager
import pymysql
from extensions import db

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# JWT Secret Key
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-default-secret')

#setting up MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
# Import User model after db is initialized
from models import User

db.init_app(app)
jwt = JWTManager(app)

# Import and register blueprints after initializing extensions
from authentication.auth import authentication
app.register_blueprint(authentication, url_prefix='/auth')

# Create all tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)