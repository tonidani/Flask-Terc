from . import api_v1
from flask import jsonify, request

@api_v1.errorhandler(404)
def not_found(e):
    res = jsonify({"error": "brak wyników", "url": request.url})
    res.status_code = 404
    return res

@api_v1.errorhandler(400)
def bad_request(e):
    res = jsonify({"error": "zły filtr lub parametr", "url": request.url})
    res.status_code = 400
    return res