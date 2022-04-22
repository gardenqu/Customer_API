from flask import Blueprint, jsonify, request
from .models import Customer,db


bp=Blueprint('customers',__name__,url_prefix='/customers')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    customers = Customer.query.all() # ORM performs SELECT query
    result = []
    for customer in customers:
        result.append(customer.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = Customer.query.get_or_404(id)
    return jsonify(u.serialize())

@bp.route('', methods=['POST'])
def create():
   
    new_customer = Customer(
        first_name=request.json['First_Name'],
        last_name=request.json['Last_Name'],
        email=request.json['Email'],
        address=request.json['Street_Address'],
        city=request.json['City'],
        state=request.json['State'],
        zip=request.json['Zip']
    )
    db.session.add(new_customer) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(new_customer.serialize())


