from flask import request, Blueprint
from .sevices import *  # service spelling is wrong but kept as-is for now
from flask import Flask, request, jsonify


bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/get_all_Customers', methods=['GET'])
def get_Customers():
    result = get_all_Customers_from_services()
    return result

# @bp.route('/admin_dashboard/<int:user_id>', methods=['GET'])
# def admin_dashboard_route(user_id):
#     dashboard_data = admin_dashboard(user_id)
#     return jsonify(dashboard_data)
# store = [
#     {
#         "name":"my store",
#         "items":[
#             {
#                 "name":"chair",
#                 "price":14.99
#             }
#         ]
#     }
# ]

# @app.get("/stores")
# def get_store():
#     return {"stores":store}

# @app.post("/stores")
# def create_store():
#     request_data = request.get_json()
#     new_store = {"name":request_data["name"], "items":[]}
#     store.append(new_store)
#     return new_store, 201

# @app.post("/stores/<string:name>/items")
# def create_item(name):
#     request_data=request.get_json()
#     for inp_sto in store:
#         if inp_sto["name"] == name:
#             print("selected store name... ", inp_sto["name"])

#             new_item = {"name":request_data["name"], "price":request_data["price"]}
#             print("this are new item which are going to add... ",new_item)
#             print(" ")
#             print("this is a store.. ", store)
#             print(" ")
#             print("this is store inp insibe... ",inp_sto["items"])
#             print(" ")
#             inp_sto["items"].append(new_item)
#             print("updated inp store... ",inp_sto["items"])
#             return new_item, 201
#     return {"message":"store not found"}, 404

# @app.get("/stores/<string:store_name>")
# def get_specific_store(store_name):
#     for i in store:
#         if i["name"] == store_name:
#             return i
#     return {"message": "store not found"}, 404

# @app.get("/stores/<string:store_name>/items")
# def get_specific_store_items(store_name):
#     for j in store:
#         if j["name"] == store_name:
#             return {"items": i}
#     return {"message": "store not found"}, 404
    
# hsd

@bp.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    result, status_code = add_customer_by_service(data)
    return jsonify(result), status_code


@bp.route('/update_customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    result, status_code = update_customer_by_service(customer_id, data)
    return jsonify(result), status_code








