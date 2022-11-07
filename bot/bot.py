import asyncio
import logging
import requests
import json
import os
from typing import Optional, List
from wechaty import Wechaty, Contact, Friendship, Room
from wechaty.user import Message
from wechaty.plugin import WechatyPlugin
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import random
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class DailyPushPlugin(WechatyPlugin):

    @property
    def name(self) -> str:
        return 'daily task'

    async def task(self):
        res = requests.get(f"http://{os.environ.get('MESSAGE_SERVICE_ENDPOINT')}/daily_push")
        log.info(f'定时推送请求: {res.status_code}')

        log.info(res.json())
        task_info = res.json()

        if 'action' in task_info and task_info['action'] == 'push':
            delay = random.randint(1, 60) * 60
            log.info(f'延迟推送：{delay}s')
            time.sleep(delay)

            rooms = await self.bot.Room.find_all()
            for room in rooms:
                if room.room_id in task_info['room_ids']:
                    await room.say(task_info['message'])
                    time.sleep(random.randint(1, 10))

    async def init_plugin(self, wechaty: Wechaty):
        await super().init_plugin(wechaty)
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.task, 'interval', seconds=10)
        # scheduler.add_job(func=self.task, trigger='cron', hour=8, minute=0, second=0)


class MyBot(Wechaty):
    """
    listen wechaty event with inherited functions, which is more friendly for
    oop developer
    """
    def __init__(self):
        super().__init__()

    # 消息处理
    async def on_message(self, msg: Message):

        from_contact = msg.talker()
        text = msg.text()
        room = msg.room()

        data = {'bot_id': self.user_self().contact_id,
                'bot_name': self.user_self().name,
                'from_id': from_contact.contact_id,
                'from_name': from_contact.name,
                'room_id': room.room_id if room else '',
                'room_name': room.payload.topic if room else '',
                'message': text}

        log.info(f"bot: {data['bot_name']} - {data['bot_id']}")
        log.info(f"from: {data['from_name']} - {data['from_id']}")
        log.info(f"room: {data['room_name']} - {data['room_id']}")
        log.info(f"message: {data['message']}")

        if data['from_id'] not in [self.user_self().contact_id, 'weixin']:
            res = requests.post(url=f"http://{os.environ.get('MESSAGE_SERVICE_ENDPOINT')}/message",
                                json=json.dumps(data, ensure_ascii=False),
                                headers={'content-type': 'application/json'})

            log.info(f'消息服务请求: {res.status_code}')

            command = res.json()

            if command['action'] == 'answer':

                sleep_time = random.randint(1, 10)
                log.info(f"回复: {command['text']} (等待{sleep_time}s)")
                time.sleep(sleep_time)

                conversation = from_contact if room is None else room
                await conversation.ready()
                await conversation.say(command['text'])

            else:
                log.info('回复：无')

    # 好友申请
    async def on_friendship(self, friendship: Friendship) -> None:

        receive_content = friendship.hello()
        contact = friendship.contact()

        log.info(f"receive: {receive_content}")
        log.info(f'wechat_id: {contact.contact_id}')
        log.info(f'wechat_name: {contact.name}')

        if receive_content == 'hello':
            await friendship.ready()
            await friendship.accept()

    # 人员进群信息监听
    async def on_room_join(self, room: Room, invitees: List[Contact], inviter: Contact, date: datetime) -> None:

        room_size = await room.member_list()
        room_id = Room.room_id
        inviter_wechat_id = inviter.contact_id
        inviter_wechat_name = inviter.name
        invitees_ls = [{'wechat_id': c.contact_id, 'wechat_name': c.name} for c in invitees]

        log.info(f'room_id: {room_id}')
        log.info(f'room_size: {room_size}')
        log.info(f'inviter: {inviter_wechat_id} - {inviter_wechat_name}')
        log.info(f"invitees_ls: {[(i['wechat_id'], i['wechat_name']) for i in invitees_ls]}")

    # 人员退群信息监听
    async def on_room_leave(self, room: Room, leavers: List[Contact], remover: Contact, date: datetime) -> None:

        room_size = await room.member_list()
        room_id = Room.room_id
        remover_wechat_id = remover.contact_id
        remover_wechat_name = remover.name
        leavers_ls = [{'wechat_id': c.contact_id, 'wechat_name': c.name} for c in leavers]

        log.info(f"'room_id': {room_id}")
        log.info(f'room_size: {room_size}')
        log.info(f'remover: {remover_wechat_id} - {remover_wechat_name}')
        log.info(f"leavers_ls: {[(i['wechat_id'], i['wechat_name']) for i in leavers_ls]}")


bot: Optional[MyBot] = None


async def main():
    """doc"""
    global bot
    bot = MyBot().use(DailyPushPlugin())
    await bot.start()


asyncio.run(main())
