from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
DB_NAME = "mad1.db"

class User(db.Model, UserMixin):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True) #every table needs an id and primary key
    name = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable = False, unique = True)
    password = db.Column(db.Text, nullable = False)
    role = db.Column(db.Text, nullable = False) #admin, sponsor or influencer 



