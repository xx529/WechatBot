from flask import Flask, request
import json
from db import add_message
from faker import Faker


app = Flask(__name__)
f = Faker('zh_CN')


@app.route('/message', methods=['POST'])
def message():
    data = json.loads(request.json)
    add_message(data)

    res = {'action': 'nothing'}

    text = data['message']

    if '今日头条' in text and '@AI小黑狗' in text and data['room_id'] in ['48978056256@chatroom', '19561654518@chatroom']:
        res['action'] = 'answer'
        res['text'] = f.text().replace('\n', '')
    elif '拍了拍我' in text and data['room_id'] in ['48978056256@chatroom']:
        res['action'] = 'answer'
        res['text'] = '别拍了，疼（含羞脸）[翻白眼]'
    else:
        pass

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
    data = json.loads(request.json)
    return data


@app.route('/daily_push', methods=['GET'])
def daily_task():
    # task_info = {'action': 'push',
    #              'room_ids': ['48978056256@chatroom', '19561654518@chatroom'],
    #              'message': '今日的定时任务来啦！'}
    task_info = {'action': 'pass'}
    return task_info


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
