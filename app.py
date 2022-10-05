import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from Schema import RequestData
from create_data import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = RequestData().load(request.json)
    except ValidationError as error:
        return error.messages, 400

    result = None
    result = build_query(
        cmd=params['cmd1'],
        param=params['value1'],
        data=result
    )

    result = build_query(
        cmd=params['cmd2'],
        param=params['value2'],
        data=result
    )
    return jsonify(result)


if __name__ == "__main__":
    app.run()
