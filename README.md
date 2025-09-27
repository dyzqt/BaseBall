# BaseBall

http://127.0.0.1:8000/admin/ # 管理员登录
http://127.0.0.1:8000/articles/ # 文章列表
http://127.0.0.1:8000/ # 主页

venv\\Scripts\\activate 进入虚拟环境

cd Baseball_django 进入文件夹

python manage.py runserver 启动Django
出现Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.说明启动成功

运行数据库迁移命令来应用模型更改：
cd D:\其他\Code\Vue\BaseBall\Baseball_django # 进入项目目录
python manage.py makemigrations
python manage.py migrate


python manage.py runserver 192.168.168.89:8000