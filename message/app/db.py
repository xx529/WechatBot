import os
import psycopg2
import logging
import time

logging.basicConfig(level=logging.INFO)

CONN = {'dbname': os.environ.get('PG_DB'),
        'user': os.environ.get('PG_USER'),
        'password': os.environ.get('PG_PASSWORD'),
        'host': os.environ.get('PG_HOST'),
        'port': os.environ.get('PG_PORT')}

MESSAGE_SQL = """
    insert into 
    message (talk_type, talker_id, talker_name, receiver_id, receiver_name, timestamp, message)
    values ('{talk_type}', '{talker_id}', '{talker_name}', '{receiver_id}', '{receiver_name}', {timestamp}, '{message}')
    """

ROOM_SQL = """
    insert into 
    room (room_id, room_name, current_size, wechat_id, wechat_name, in_out, operate_wechat_id, operate_wechat_name, timestamp)
    values ('{room_id}', '{room_name}', {current_size}, '{wechat_id}', '{wechat_name}', {in_out}, '{operate_wechat_id}', '{operate_wechat_name}', {timestamp})"""


def auto_execute(func):
    def inner(*args, **kwargs):
        with psycopg2.connect(**CONN) as conn:
            info = func(*args, **kwargs)
            conn.cursor().execute(MESSAGE_SQL.format(**info))

        log_info = f"{info['talker_name']}({info['talker_id']}) >>> {info['receiver_name']}({info['receiver_id']})：{info['message'][:100]}..."
        logging.info(log_info)
        return True
    return inner


@auto_execute
def add_receive_message(data):

    info = {'talk_type': 'private' if data['room_id'] == '' else 'room',
            'talker_id': data['from_id'],
            'talker_name': data['from_name'],
            'receiver_id': data['bot_id'] if data['room_id'] == '' else data['room_id'],
            'receiver_name': data['bot_name'] if data['room_id'] == '' else data['room_name'],
            'timestamp': time.time(),
            'message': data['message']}

    return info


@auto_execute
def add_send_message(data, answer_text):

    info = {'talk_type': 'private' if data['room_id'] == '' else 'room',
            'talker_id': data['bot_id'],
            'talker_name': data['bot_name'],
            'receiver_id': data['from_id'] if data['room_id'] == '' else data['room_id'],
            'receiver_name': data['from_name'] if data['room_id'] == '' else data['room_name'],
            'timestamp': time.time(),
            'message': answer_text}

    return info


def room_join_record(data):
    info = {'timestamp': time.time(),
            'in_out': 1,
            'room_id': data['room_id'],
            'room_name': data['room_name'],
            'operate_wechat_id': data['inviter_id'],
            'operate_wechat_name': data['inviter_name']}

    num_ls = [data['room_size'] - x + 1 for x in list(range(len(data['invitees_ls']), 0, -1))]

    with psycopg2.connect(**CONN) as conn:
        for idx, (num, invite) in enumerate(zip(num_ls, data['invitees_ls'])):
            info['current_size'] = num
            info['wechat_id'] = data['invitees_ls'][idx]['wechat_id']
            info['wechat_name'] = data['invitees_ls'][idx]['wechat_name']

            conn.cursor().execute(ROOM_SQL.format(**info))


def room_leave_record(data):

    info = {'timestamp': time.time(),
            'in_out': -1,
            'room_id': data['room_id'],
            'room_name': data['room_name'],
            'operate_wechat_id': data['remover_id'],
            'operate_wechat_name': data['remover_name']}

    num_ls = [data['room_size'] - x for x in list(range(len(data['leavers_ls'])))]

    with psycopg2.connect(**CONN) as conn:
        for idx, (num, invite) in enumerate(zip(num_ls, data['leavers_ls'])):
            info['current_size'] = num
            info['wechat_id'] = data['leavers_ls'][idx]['wechat_id']
            info['wechat_name'] = data['leavers_ls'][idx]['wechat_name']

            conn.cursor().execute(ROOM_SQL.format(**info))
