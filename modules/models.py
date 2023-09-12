from . import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
    recipes = db.relationship('Recepi', backref='user')

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tile = db.Column(db.String(50))
    text = db.Column(db.String(500))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))