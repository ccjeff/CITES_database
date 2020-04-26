from flask import Blueprint, jsonify


main = Blueprint('main', __name__)

@main.route('/get_call', methods = ['POST'])
def get_call():

    return 'Done', 201

@main.route('/table')

def tables():

    countries = []


    return jsonify({'country': countries})

