import asyncio
import logging
import requests
import json
import os
from typing import Optional, List
from wechaty import Wechaty, Contact, Friendship, Room
from wechaty.user import Message
import datetime

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


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

        log.info(f'wechat_id: {from_contact.contact_id}')
        log.info(f'wechat_name: {from_contact.name}')
        log.info(f'message: {text}')
        log.info(f"room_id: {room.room_id if room else '私聊'}")

        data = {'wechat_id': from_contact.contact_id,
                'wechat_name': from_contact.name,
                'room_id': room.room_id if room else '私聊',
                'message': text}

        res = requests.post(url=f"{os.environ.get('MESSAGE_SERVICE_ENDPOINT')}/message",
                            json=json.dumps(data, ensure_ascii=False),
                            headers={'content-type': 'application/json'})

        log.info('后台请求', res.status_code)

        command = res.json()

        if command['action'] == 'answer':
            conversation = from_contact if room is None else room
            await conversation.ready()
            await conversation.say(command['text'])

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

        log.info(f"'room_id': {room_id}")
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
    bot = MyBot()
    await bot.start()


asyncio.run(main())
