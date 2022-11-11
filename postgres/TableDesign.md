# Table Design

[TOC]

## message

表名：room_message

作用：记录微信消息记录



| 字段名        | 数据类型 | 主键 | 默认值 | 描述                             |
| ------------- | -------- | ---- | ------ | -------------------------------- |
| talk_type     | varchar  |      |        | room（群聊）或者 private（私聊） |
| talker_id     | varchar  |      |        | 发送者微信号ID                   |
| talker_name   | varchar  |      |        | 发送者微信号名称                 |
| receiver_id   | varchar  |      |        | 接收者微信号ID                   |
| receiver_name | varchar  |      |        | 接受者微信名称                   |
| timestamp     | float    |      |        | 消息时间戳                       |
| message       | text     |      |        | 消息文本内容                     |

```sql
CREATE TABLE public.message (
  talk_type varchar NULL,
	talker_id varchar NULL,
	talker_name varchar NULL,
	receiver_id varchar NULL,
  receiver_name varchar NULL,
	"timestamp" float NULL,
	message text NULL
);
```



## room

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



## hot words

表名：hot_words

作用：记录每个群的词频热词统计

| 字段名  | 数据类型 | 主键 | 默认值 | 描述       |
| ------- | -------- | ---- | ------ | ---------- |
| room_id | varchar  |      |        | 消息群名ID |
| word    | varchar  |      |        | 单词       |
| count   | int      |      |        | 单词词频数 |

```sql
CREATE TABLE public.hot_words (
	room_id varchar NULL,
	word varchar NULL,
	"count" int NULL
);
```

