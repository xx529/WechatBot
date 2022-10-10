# Table Design

[TOC]

## Message

表名：message

作用：记录微信消息记录

| 字段名      | 数据类型 | 主键 | 默认值 | 描述                       |
| ----------- | -------- | ---- | ------ | -------------------------- |
| wechat_id   | varchar  |      |        | 微信号ID                   |
| wechat_name | varchar  |      |        | 微信号名称                 |
| room        | varchar  |      |        | 消息群名，如果为空则为私聊 |
| timestamp   | int      |      |        | 消息时间戳                 |
| message     | text     |      |        | 消息内容                   |

```sql
CREATE TABLE public.message (
	wechat_id varchar NULL,
	wechat_name varchar NULL,
	room varchar NULL,
	"timestamp" int NULL,
	message text NULL
);
```