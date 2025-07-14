from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#db model for buyer authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(150), unique=True,)
    password = db.Column(db.String(300),)
