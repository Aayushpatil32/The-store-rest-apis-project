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