# DML(数据操作语言)

用于完成对数据库中表的数据记录进行增删改查操作（insert,update,delete)

## 一、添加

### 1.指定字段添加

```mysql
单次：
insert into (字段1， 字段2) values(值1， 值2);
批量:
insert into (字段1， 字段2) values(值1， 值2), (值1， 值2), (值1， 值2);
```

## 二、修改

### 1. 修改数据

```mysql
update 表名 set 字段名1=值1， 字段名2=值;2， ... [where 条件];

不带where条件即修改整个表的数据
```






