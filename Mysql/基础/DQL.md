# DQL

DQL,数据查询语言，用于查询数据库中表的记录

## 一、语法（单表查询）

```mysql
select 
    字段列表
from
    表名列表
where
    条件列表
group by
    分组列表
having
    分组后条件列表
order by
    排序字段列表
limit
    分页参数
```

## 二、基本查询

### 1. 设置别名

```mysql
select 字段1 [as 别名1] from 表名;
```

### 2. 去除重复记录

```mysql
select distinct 字段列表 from表名;
```

### 3. 查询所有字段

```mysql
select 所有字段名 from 表名;
效率上高于
select * from 表名;
```

### 4. 条件查询

```mysql
select * from 表名 where 字段 like 占位符
模糊匹配：_匹配单个字符，%匹配多个字符
```

### 5. 聚合函数

```mysql
min max avg sum count
```

### 6. 分组查询

#### where和having的区别

* 执行时机：where分组之前过滤，不满足条件就不参与分组。having对分组结果过滤。
* 判断条件：where不能对聚合函数判断。

### 7. 排序查询

#### 排序方式

* ASC：升序
* DESC：降序

多字段排序，第一个值相同排第二个值

### 8.分页查询

```mysql
select [字段] from 表名 limit 起始索引， 查询记录数;
```

#### 注意

* 起始索引从0开始，起始索引=(查询页码 - 1) * 每页显示记录数
* 查询第一页起始索引可以省略，简写为limit 10

## 三、执行顺序

from -> where -> group by -> having -> select -> order by -> limit

