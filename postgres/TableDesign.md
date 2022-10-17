# Table Design

[TOC]

## Message

表名：message

作用：记录微信消息记录

| 字段名      | 数据类型 | 主键 | 默认值 | 描述                       |
| ----------- | -------- | ---- | ------ | -------------------------- |
| wechat_id   | varchar  |      |        | 微信号ID                   |
| wechat_name | varchar  |      |        | 微信号名称                 |
| room_id     | varchar  |      |        | 消息群名ID，如果为空则为私聊 |
| timestamp   | int      |      |        | 消息时间戳                 |
| message     | text     |      |        | 消息内容                   |

```sql
CREATE TABLE public.message (
	wechat_id varchar NULL,
	wechat_name varchar NULL,
	room_id varchar NULL,
	"timestamp" int NULL,
	message text NULL
);
```



## Room

表名：room

作用：记录群的人员进出情况

| 字段名              | 数据类型 | 主键 | 默认值 | 描述                         |
| ------------------- | -------- | ---- | ------ | ---------------------------- |
| room_id             | varchar  |      |        | 消息群名ID                   |
| current_size        | int      |      |        | 当前群总人数                 |
| wechat_id           | varchar  |      |        | 微信号ID                     |
| wechat_name         | varchar  |      |        | 微信号名称                   |
| in_out              | int      |      |        | 进群为1，退群为-1            |
| operate_wechat_id   | varchar  |      |        | 进群邀请人或退群操作人微信ID |
| operate_wechat_name | varchar  |      |        | 进群邀请人或退群操作人微信名 |
| timestamp           | int      |      |        | 消息时间戳                   |

```sql
CREATE TABLE public.room (
	room_id varchar NULL,
	current_size int NULL,
	wechat_id varchar NULL,
	wechat_name varchar NULL,
	in_out int NULL,
	operate_wechat_id varchar NULL,
	operate_wechat_name varchar NULL,
	"timestamp" int NULL
);
```

