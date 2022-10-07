FROM python:3.8.13-slim-bullseye

RUN apt update -y && \
    apt-get update -y &&  \
    apt -y upgrade

RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple wechaty
