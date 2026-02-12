# DDL

## 一、数据库操作

### 1. 创建

```mysql
CREATE DATABASE [IF NOT EXISTS] 数据库名 [CHARSET 字符集] [COLLATE 排序规则] 
字符集包括utf8和utf8mb4，utf8mb4范围更大，可以保存emoji
```

## 二、表操作

### 1. 查询表结构

```mysql
DESC 表名;
```

### 2. 查询指定表建表语句

```mysql
SHOW CREATE TABLE 表名;
```

### 3.数据类型

* TINY(INT\BLOB\TEXT)：整型、二进制、文本

* MEDIUM

* LONG
* CHAR&VARCHAR：定长&变长字符串

* DATE：日期值
* TIME：时间值
* YEAR：年份
* DATETIME：混合
* TIMESTAMP：时间戳

### 4.修改表

* 添加字段

```mysql
ALTER TABLE 表名 ADD 字段名 类型（长度）
```

* 修改数据类型

```mysql
ALTER TABLE 表名 MODIFY 字段名 类型（长度）
```

* 修改字段名和字段类型

```mysql
ALTER TABLE 表名 CHANGE 旧字段名 新字段名 类型（长度）
```

* 删除字段

```mysql
ALTER TABLE 表名 DROP 字段名
```

* 修改表名

```mysql
ALTER TABLE 表名 RENAME TO 新表名
```

* 删除并重新创建表

```mysql
TRUNCATE TABLE 表名
```