FROM python:3.8.13-slim-bullseye

# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple wechaty requests wechaty-plugin-contrib

#COPY ./bot.py /wechatbot/bot.py

#CMD python /wechatbot/bot.py
