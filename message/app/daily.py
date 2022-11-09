import datetime

STUDY_TASK = {'2022-11-10': {'room_ids': ['48978056256@chatroom', '39167613285@chatroom', '19561654518@chatroom'],
                             'message': '上班好塞车啊（这个是每日资料推送）'}}

GREETING_TASK = {'2022-11-10': {'room_ids': ['48978056256@chatroom', '39167613285@chatroom', '19561654518@chatroom'],
                                'message': '收工啦！收工啦！（这个是每日讨论或者问候）'}}

TASK = {'study': STUDY_TASK,
        'greeting': GREETING_TASK}

DEFAULT = {'action': 'pass'}


def get_daily_task(data):
    task_name = data['task_name']

    if task_name not in TASK:
        return DEFAULT

    cur_task = TASK[task_name]
    today = str(datetime.datetime.now()).split()[0]

    if today in cur_task:
        task_info = cur_task[today]
        task_info['action'] = 'push'
        return task_info
    else:
        return DEFAULT
