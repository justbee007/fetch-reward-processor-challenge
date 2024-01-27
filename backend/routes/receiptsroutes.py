from flask import request, jsonify, make_response, jsonify, make_response
from flask_json import FlaskJSON, as_json_p, json_response
from . import receiptsroutesobject
from services.receiptservices import validate_schema, generate_id, checkJsonisempty
from services.redisservices import getReceipt, insertReceipt
from services.calculatepointsservices import calculateTotalPoints


@receiptsroutesobject.route("/process", methods=["POST"])  # Route to process receipt
def receipts_process():
    receipt_json = request.json
    isValid = validate_schema(receipt_json)
    try:
        checkJsonisempty(receipt_json)
        if isValid:
            receiptId = generate_id()
            print(receiptId)
            insertReceipt(receiptId, receipt_json)
            message = {"id": receiptId}
            return make_response(
                jsonify(message), 200, {"Content-Type": "application/json"}
            )
        else:
            message = {"description": "The receipt is invalid"}
            return make_response(
                jsonify(message), 400, {"Content-Type": "application/json"}
            )
    except Exception as e:
        message = {"description": "The receipt is invalid"}
        return make_response(
            jsonify(message), 400, {"Content-Type": "application/json"}
        )


@receiptsroutesobject.route(
    "<string:id>/points", methods=["GET"]
)  # Route to get receipt points
def getpoints(id):
    try:
        receiptJson = getReceipt(id)
        totalPoints = calculateTotalPoints(receiptJson)
        message = {"points": totalPoints}
        return make_response(
            jsonify(message), 200, {"Content-Type": "application/json"}
        )
    except:
        message = {"description": "No receipt found for that id"}
        return make_response(
            jsonify(message), 400, {"Content-Type": "application/json"}
        )
