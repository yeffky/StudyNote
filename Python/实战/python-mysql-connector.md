# Python操作Mysql数据库

## 1. 安装

```shell
pip install mysql-connector-python
```

## 2. 数据库插入json格式数据

```python
import mysql.connector
import json
from datetime import datetime

# 创建数据库连接
db = mysql.connector.connect(
    host="localhost",  # MySQL服务器地址
    user="root",           # 用户名
    password="123456",  # 密码
    database="test",  # 数据库名称
    port="3307"             # 端口
)

# 创建游标对象，用于执行SQL查询
cursor = db.cursor()

# 读取JSON文件并解析为Python字典
with open('./data/goods_2025-02-12.json', 'r', encoding='utf-8') as file:
    goods = json.load(file)

# 将字典转换为JSON字符串
goods_json = json.dumps(goods, ensure_ascii=False)

# 日期
date = '2025-02-12'

# 执行SQL
sql = "INSERT INTO goods (content, date) VALUES (%s, %s)"
val = (goods_json, date)
cursor.execute(sql, val)

# 提交事务
db.commit()

# 关闭游标和数据库连接
cursor.close()
db.close()
```

## 3. 数据库查询json格式数据

```python
import mysql.connector
import json
from datetime import datetime

# 创建数据库连接
db = mysql.connector.connect(
    host="47.122.42.169",  # MySQL服务器地址
    user="root",           # 用户名
    password="cfQyVCny64jhAy3rxmu7",  # 密码
    database="xhs_workflow",  # 数据库名称
    port="5629"             # 端口
)

# 创建游标对象，用于执行SQL查询
cursor = db.cursor()

sql = "SELECT * FROM goods WHERE date = %s"
val = ('2025-02-12',)
cursor.execute(sql, val)

# 获取查询结果
result = cursor.fetchall()

# 遍历结果并打印
for row in result:
    print(row)

# 获取商品信息(json格式)
goods = json.loads(row[1])
    
# 提交事务
db.commit()

# 关闭游标和数据库连接
cursor.close()
db.close()
```




