# 系统数据库

MYSQL自带四个数据库，具体作用如下：

* mysql：存储MYSQL服务器正常运行所需要的信息，（时区、主从、用户、权限等）
* information_schema：提供了访问数据库元数据的各种表和视图，包含数据库、表、字段类型和访问权限等。
* performance_schema：为MYSQL服务器运行时状态提供了底层监控功能，主要用于收集数据库服务器性能参数。
* sys：方便DBA和开发人员利用performance_schema性能数据库进行性能调优和诊断的视图。

## 一、常用工具

### 1. mysql客户端工具

```mysql
mysql [options] [database] [-e]
options:
    -u: --user=name
    -p: --password
    -h: --host=name  #指定服务器IP或域名
    -p: --port=port  #指定端口
    -e: --execute=name   #执行SQL并退出
```

### 2. mysqladmin

执行管理操作的客户端程序。可以检查服务器配置和状态，创建并删除数据库等。

### 3. mysqlbinlog

查看binlog（二进制日志）

```mysql
mysqlbinlog [options] log-file1 log-file2
options:
    -d: --database=name
    -o: --offset=#
    -r: --result-file=name: output2target_file
    -s: --short-form
```

### 4.mysqlshow

```mysql
mysqlshow[options][db_name[table_name[col_name]]]
options:
    --count：显示数据库和表的统计信息
    -i：显示指定数据库或者指定表的状态信息
```

### 5.mysqldump

备份数据库或在不同数据库之间进行数据迁移。备份内容包含创建表以及插入表的SQL语句。

```mysql
mysqldump[options] db_name[tables]
mysqldump[options] --database/-B db1[db2 db3...]
mysqldump[options] --all-databases/-A
connection options:
    -u
    -p
    -h
    -p
output options:
    --add-drop-database
    --add-drop-table
    -n: --no-create-db：不包含建库
    -t: --no-create-info：不包含建表
    -d: --no-data：不包含数据
    -T: --tab=name：自动生成.sql和.txt文件
```

### 6. mysqlimport/source

导入mysqldump加-T参数后导出的文本文件。

```mysql
mysqlimport [options] db_name textfile1[textfile2...]
example:
    mysqlimport -uroot -p123456 test /tmp/city.txx
```

导入sql文件

