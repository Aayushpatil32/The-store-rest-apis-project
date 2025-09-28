from .models import *
from flask import Flask, request, jsonify
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def get_all_Customers_from_services():
    data = (
            db.session.query(Customers)
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
    

def add_customer_by_service(data):
    #user_checking
    user = db.session.query(Customers).filter_by(email=data['email']).first()
    if user:
         return {
                "message": "this users is already exsist",
         }, 400
    ph = PasswordHasher()
    hashed_password = ph.hash(data['password'])
    new_user = Customers(
        username = data['username'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        password = hashed_password,
        date_of_birth = data['date_of_birth'],
        contact_no = data['contact_no'],
        address = data['address'],
        state = data['state'],
        country = data['country'],
        city = data['city'],
        is_delete = 0
    )
    db.session.add(new_user)
    db.session.commit()


    return {
                "message": "Customer added successfully",
         }, 201

# def update_customer_by_service(data):
#         user = db.session.query(Customers).filter_by(email=data['email']).first()
#         ph = PasswordHasher()

#         if user:
#             hashed_password = ph.hash(data['password'])
#             update_user = Customers(
#                 username = data['username'],
#                 first_name = data['first_name'],
#                 last_name = data['last_name'],
#                 email = data['email'],
#                 password = hashed_password,
#                 date_of_birth = data['date_of_birth'],
#                 contact_no = data['contact_no'],
#                 address = data['address'],
#                 state = data['state'],
#                 country = data['country'],
#                 city = data['city'],
#         )
#         db.session.add(update_user)
#         db.session.commit()



def update_customer_by_service(customer_id, data):
    try:

        user = db.session.query(Customers).filter_by(customer_id=customer_id).first()

        if not user:
            return {"error": "Customer not found"}, 404

        # Update only fields present in request
        user.username = data.get("username", user.username)
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.date_of_birth = data.get("date_of_birth", user.date_of_birth)
        user.contact_no = data.get("contact_no", user.contact_no)
        user.address = data.get("address", user.address)
        user.state = data.get("state", user.state)
        user.country = data.get("country", user.country)
        user.city = data.get("city", user.city)

        # Update password only if provided
        if "password" in data and data["password"]:
            ph = PasswordHasher()
            user.password = ph.hash(data["password"])

        db.session.commit()
        return {"message": "Customer updated successfully"}, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500