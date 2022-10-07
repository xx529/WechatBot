# 微信机器人

在本项目根目录创建 `envfile` 文件夹，并在该文件夹下创建以下文件

1. `gateway.env`
	```.env
	WECHATY_LOG=verbose
	WECHATY_PUPPET=wechaty-puppet-padlocal
	WECHATY_PUPPET_PADLOCAL_TOKEN=官网申请的token
	WECHATY_PUPPET_SERVER_PORT=8080
	WECHATY_TOKEN=自定义唯一字符串
	```

2. `pg.env`

   ```
   POSTGRES_PASSWORD=
   POSTGRES_USER=
   POSTGRES_DB=wechat
   TZ=Asia/Shanghai
   ```


3. `wechatbot.env`

   ```
   WECHATY_PUPPET_SERVICE_TOKEN=官网申请的token
   WECHATY_PUPPET_SERVICE_ENDPOINT=gateway的ip和端口
   ```

   

Token获取网址：http://pad-local.com/
