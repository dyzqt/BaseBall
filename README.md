# BaseBall

http://127.0.0.1:8000/admin/ # 管理员登录
http://127.0.0.1:8000/articles/ # 文章列表
http://127.0.0.1:8000/ # 主页
#启动步骤
venv\\Scripts\\activate 进入虚拟环境

cd Baseball_django 进入文件夹

python manage.py runserver 启动Django
出现Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.说明启动成功

运行数据库迁移命令来应用模型更改：
cd Baseball_django # 进入项目目录
python manage.py makemigrations
python manage.py migrate


python manage.py runserver 192.168.168.89:8000

#短期让其他人测试：
使用ngrok.exe，官网下载，https://ngrok.com/ 注册账户，获取免费的ngrok-free.dev域名
在虚拟环境，Baseball_django项目中运行python manage.py runserver 192.168.168.89:8000
venv\\Scripts\\activate
cd Baseball_django
python manage.py runserver 0.0.0.0:8000

打开ngrok.exe
输入 ngrok http 8000
如果弹出 Forwarding      https://quyen-unsanctified-francina.ngrok-free.dev -> http://localhost:8000
则外人也可以通过https://quyen-unsanctified-francina.ngrok-free.dev 访问
