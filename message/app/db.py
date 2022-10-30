import os
import psycopg2
import logging
import time

logging.basicConfig(level=logging.INFO)

conn_info = {'dbname': os.environ.get('PG_DB'),
             'user': os.environ.get('PG_USER'),
             'password': os.environ.get('PG_PASSWORD'),
             'host': os.environ.get('PG_HOST'),
             'port': os.environ.get('PG_PORT')}


def auto_execute(func):
    def inner(*args, **kwargs):
        with psycopg2.connect(**conn_info) as conn:
            sql = func(*args, **kwargs)
            conn.cursor().execute(sql)
        return True
    return inner


@auto_execute
def add_message(data):
    timestamp = int(time.time())
    talk_type = 'private' if data['room_id'] == '' else 'room'
    receiver_id = data['bot_id'] if data['room_id'] == '' else data['room_id']
    receiver_name = data['bot_name'] if data['room_id'] == '' else data['room_name']

    logging.info(f"from bot: {data['bot_name']} - {data['bot_id']}")
    logging.info(f"from talker: {data['from_name']} - {data['from_id']}")
    logging.info(f"from room: {data['room_name']} - {data['room_id']}")
    logging.info(f"message: {data['message'][:100]}...")

    sql = f"""insert into message 
              (talk_type, talker_id, talker_name, receiver_id, receiver_name, timestamp, message)
              values ('{talk_type}', 
                      '{data['from_id']}', 
                      '{data['from_name']}', 
                      '{receiver_id}', 
                      '{receiver_name}', 
                      {timestamp}, '
                      {data['message']}')
               """
    return sql
