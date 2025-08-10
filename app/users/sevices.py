from .models import *
from flask import Flask, request, jsonify


def get_users_from_services():
    data = (
            db.session.query(User)
            .filter_by(is_delete=0)
            .all()
        )
    return jsonify([i.to_dict() for i in data])

    if not data:
            return {
                "status": "no",
                "message": "No data found for users",
                "data": []
            }
    

def adding_user_by_service(data):
    #user_checking
    user = db.session.query(User).filter_by(User.email == data['email'])
    if user:
         return {
                "message": "this users is already exsist",
         }
    new_user = {
        username = data['username'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        password = data['password'],
        date_of_birth = data['date_of_birth'],
        contact_no = data['contact_no'],
        address = data['address'],
        state = data['state'],
        country = data['country'],
        city = data['city'],
        is_delete = 0
    }
    User.add(new_user)
    db.commit()