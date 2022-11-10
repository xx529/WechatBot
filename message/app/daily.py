import datetime
import yaml


def get_daily_task(task_name):

    with open('/message/app/tasklist.yaml') as f:
        task_list = yaml.load(f, Loader=yaml.FullLoader)

    if task_name not in task_list:
        return {'action': 'pass'}

    cur_task = task_list[task_name]
    today = str(datetime.datetime.now()).split()[0]

    if today in cur_task:
        task_info = cur_task[today]
        task_info['action'] = 'push'
        return task_info
    else:
        return {'action': 'pass'}
