# DCL

DCL用于管理数据库用户，控制数据库访问权限

## 一、管理用户

### 1. 查询用户

```mysql
use mysql;
select * from user;
```

### 2. 创建用户

```mysql
create user 'username'@'hostname' identify by 'password';
host = %：在任意主机均可访问数据库
```

### 3. 修改密码

```mysql
alter user 'username'@'hostname' identify with 'old_password' by 'new_password';
```

### 4. 删除用户

```mysql
drop user 'username'@'hostname';
```

## 二、权限控制

### 1. 查询权限

```mysql
show grants for 'username'@'hostname';
```

### 2. 授予权限

```mysql
grant 权限列表 on databasename.tablename to 'username'@'hostname';
```

### 3. 撤销权限

```mysql
revoke 权限列表 on databasename.tablename from 'username'@'hostname';
```
