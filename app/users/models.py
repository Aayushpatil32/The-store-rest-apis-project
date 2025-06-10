from app import db

class User(db.Model):
    __tablename__ = 'user_activities'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def to_dict(self):
        return {
            "id" : self.id,
            "username" : self.username,
            "email" : self.email
                }

    def __repr__(self):
        return f'<User {self.username}>'
    
    