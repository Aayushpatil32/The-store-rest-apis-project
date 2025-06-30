from app import db
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class User(db.Model):
    __tablename__ = 'users_table'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    contact_no = db.Column(db.BigInteger, unique=True, nullable=False)
    address = db.Column(db.String(300), unique=True, nullable=False)  # Changed from Text to String
    state = db.Column(db.String(70), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(70), nullable=False)
    is_delete = db.Column(db.Boolean, nullable=False, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date_of_birth": str(self.date_of_birth),
            "contact_no": self.contact_no,
            "address": self.address,
            "state": self.state,
            "country": self.country,
            "city": self.city,
            "is_delete" : self.is_delete
        }

    def __repr__(self):
        return f'<User {self.id}>'