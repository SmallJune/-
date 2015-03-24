# Python 示例程序

## 项目介绍

本项目是一个使用 [Flask](http://flask.pocoo.org) 框架编写的简单的 [Python](https://www.python.org) 示例程序, 目录结构：

```
.
├── Procfile
├── README.md
├── hello.py
└── requirements.txt
```

## 项目要求

项目必须使用 [Pip](https://pip.pypa.io) 来解决依赖，如果项目目录下没有 `requirements.txt` 文件，你必须创建一个，否则项目将无法部署。

> 小提示：可以使用 `pip freeze > requirements.txt` 命令生成 `requirements.txt` 文件

`requirements.txt` 示例：

```
Flask==0.9
Jinja2==2.7.2
Werkzeug==0.8.3
gunicorn==0.17.2

```

要想应用可以跑起来，还需要一个 `Procfile` 文件，里面指定应用的启动命令。

`Procfile` 示例：

```
web: gunicorn hello:app -b $VCAP_APP_HOST:$VCAP_APP_PORT
```

## 本地测试

* 安装 [Python](http://python.org) 和 [Virtualenv](http://pypi.python.org/pypi/virtualenv)，[查看参考文档](http://install.python-guide.org)。
* 执行下面命令创建一个 [Virtualenv](http://pypi.python.org/pypi/virtualenv) 并在里面启动项目：

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn hello:app
```
* 访问 <http://localhost:8000> 查看效果。
