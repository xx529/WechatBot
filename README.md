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

2. `postgres.env`

   ```.env
   POSTGRES_PASSWORD=数据库密码
   POSTGRES_USER=用户名称
   POSTGRES_DB=数据库名
   TZ=Asia/Shanghai
   ```


3. `wechatbot.env`

   ```.env
   WECHATY_PUPPET_SERVICE_TOKEN=官网申请的token
   WECHATY_PUPPET_SERVICE_ENDPOINT=gateway的ip和端口
   ```

4. `dashboard.env`

   ```.env
   PG_HOST=数据库ip
   PG_PORT=数据库端口
   PG_DB=数据库名
   PG_USER=用户名称
   PG_PASSWORD=数据库密码
   ```
   
   

Token获取网址：http://pad-local.com/

