# T-fastapi

fastapi项目开发模板

## 用法

1. 运行项目

```shell
pipenv install
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

2. 反向生成ORM模型

```shell
# sqlite
sqlacodegen --outfile models.py sqlite:///database.db

# mysql
sqlacodegen --outfile models.py mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8
```

## License

T-fastapi uses the MIT license, see LICENSE file for the details.
