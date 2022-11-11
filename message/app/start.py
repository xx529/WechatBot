from flask import Flask, request
from db import add_receive_message, add_send_message
from daily import get_daily_task
from answer import get_answer

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def message():
    data = request.json
    add_receive_message(data)
    res = get_answer(data)

    if res['action'] == 'answer':
        add_send_message(data, res['text'])

    return res


@app.route('/room_join', methods=['POST'])
def room_join():
    data = request.json
    return data


@app.route('/daily_push', methods=['POST'])
def daily_task():
    return get_daily_task(request.json['task_name'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
