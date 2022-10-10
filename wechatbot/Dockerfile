FROM python:3.8.13-slim-bullseye

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple wechaty

COPY ./bot.py /wechatbot/bot.py

CMD python /wechatbot/bot.py
