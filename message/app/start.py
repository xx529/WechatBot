from flask import Flask, request
from db import add_message
from daily import get_daily_task
from answer import get_answer

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def message():
    data = request.json
    add_message(data)
    res = get_answer(data)

    if res['action'] == 'answer':
        add_message({'bot_id': data['bot_id'],
                     'bot_name': data['bot_name'],
                     'from_id': data['bot_id'],
                     'from_name': data['bot_name'],
                     'room_id': data['room_id'],
                     'room_name': data['room_name'],
                     'message': res['text']})

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
