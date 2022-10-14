from flask import Flask, request
import json
from db import add_message

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def message():
    data = json.loads(request.json)
    add_message(data)
    return {'state': 'ok'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
