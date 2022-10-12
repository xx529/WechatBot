import asyncio
import logging

from typing import Optional

from wechaty import Wechaty, Contact
from wechaty.user import Message

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class MyBot(Wechaty):
    """
    listen wechaty event with inherited functions, which is more friendly for
    oop developer
    """
    def __init__(self):
        super().__init__()

    async def on_message(self, msg: Message):
        """
        listen for message event 
        """
        from_contact = msg.talker()
        text = msg.text()
        room = msg.room()

        log.info(f'wechat_id: {from_contact.contact_id}')
        log.info(f'wechat_name: {from_contact.name}')
        log.info(f'message: {text}')
        log.info(f"room_id: {room.room_id if room else '私聊'}")

        if text == '1':
            conversation = from_contact if room is None else room
            await conversation.ready()
            await conversation.say('# 这是自动回复：dong')
    #
    # async def on_login(self, contact: Contact):
    #     print(f'user: {contact} has login')
    #
    # async def on_scan(self, status: ScanStatus, qr_code: Optional[str] = None,
    #                   data: Optional[str] = None):
    #     contact = self.Contact.load(self.contact_id)
    #     print(f'user <{contact}> scan status: {status.name} , '
    #           f'qr_code: {qr_code}')


bot: Optional[MyBot] = None


async def main():
    """doc"""
    global bot
    bot = MyBot()
    await bot.start()


asyncio.run(main())