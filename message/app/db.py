import os
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

conn_info = {'dbname': os.environ.get('PG_DB'),
             'user': os.environ.get('PG_USER'),
             'password': os.environ.get('PG_PASSWORD'),
             'host': os.environ.get('PG_HOST'),
             'port': os.environ.get('PG_PORT')}


def auto_exec(func):
    def inner(*args, **kwargs):
        with psycopg2.connect(**conn_info) as conn:
            sql = func(*args, **kwargs)
            conn.cursor().execute(sql)
        return True
    return inner


@auto_exec
def add_message(data):
    logging.info(
        f"{data['wechat_id']} - {data['wechat_name']} - {data['room_id']} - {data['timestamp']} - {data['message'][:15]}...")

    sql = f"""insert into message 
              (wechat_id, wechat_name, room_id, timestamp, message)
              values ('{data['wechat_id']}', '{data['wechat_name']}', '{data['room_id']}', {data['timestamp']}, '{data['message']}')
               """
    return sql
