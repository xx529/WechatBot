from flask import Flask, request
import json
import random
from db import add_message

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def message():
    data = json.loads(request.json)
    add_message(data)

    res = {'action': 'nothing'}

    text = data['message']

    if '新闻' in text:
        res['action'] = 'answer'
        res['text'] = random.choice(['非常好', '我都觉得系感样', '边有可能', '我五信！'])

    elif '好的' in text:
        res['action'] = 'answer'
        res['text'] = 'Ok的！'

    else:
        if random.random() > 0.7:
            res['action'] = 'answer'
            res['text'] = random.choice(['知道了', '收到', '明白', 'Ok'])

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
