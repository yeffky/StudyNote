# Web

## 一、REST

Representational State Transfer

### 1.实质

URL只使用名词定位资源，使用HTTP协议动词实现增删改查。

例子：

```Java
增加一个朋友，uri: generalcode.cn/v1/friends 接口类型：POST
删除一个朋友，uri: generalcode.cn/va/friends 接口类型：DELETE（在http的parameter指定好友id）
修改一个朋友，uri: generalcode.cn/va/friends 接口类型：PUT（在http的parameter指定好友id）
查找一个朋友，uri: generalcode.cn/va/friends 接口类型：GET
```

反例：

```Java
generalcode.cn/va/deleteFriends 该接口用来表示删除朋友，这就是不符合REST协议的接口。
```

## 二、HTTP

### 1.请求数据格式

#### (1)请求行

第一行，声明请求方式，资源路径等

#### (2)请求头

* Host：主机名
* User-Agent：浏览器版本
* Accept：浏览器接收资源类型，例如test/*
* Accept-Language：偏好语言
* Accept-Encoding：支持的压缩类型
* Content-Type：请求主体的数据类型
* Content-Length：请求主体的大小

#### (3)请求体

POST请求存放请求参数（GET放在请求行）

### 2.相应数据格式

#### (1)响应行

第一行，包含协议、状态码、描述

状态码：

* 1xx：响应中
* 2xx：成功接收
* 3xx：重定向
* 4xx：发生错误，责任在客户端
* 5xx：服务器错误-处理发生错误，责任在服务端

#### (2)响应头

* Content-Type
* Content-Length
* Content-Encoding
* Cache-Control
* Set-Cookie：为当前页面所在域设置cookie

#### (3)响应体

存放响应数据

## 三、WEB服务器

完成对HTTP协议的操作封装，使得程序员不必对协议进行操作。

### 1.Tomcat

* 支持Servlet/JSP少量JavaEE规范
* Web容器、Servlet容器。Servlet运行依赖Tomcat
* SpringBoot内嵌Tomcat

### 2.三层架构

* Service层： Service层是业务逻辑层，负责处理业务逻辑、数据处理和业务规则。它是业务逻辑的核心，负责封装和处理具体业务功能。在Service层中，通常会调用DAO层的方法来访问数据库，并根据业务需求进行数据处理和业务规则的实现。Service层的设计使得业务逻辑与具体的数据访问分离，使得业务逻辑更加清晰，易于维护和修改。
* DAO层： DAO层是数据访问层，负责与数据库进行交互，执行CRUD（增删改查）操作。DAO层封装了对数据库的操作，包括数据库的连接、查询语句的执行和结果的返回。通过将数据访问封装在DAO层中，实现了数据访问与业务逻辑的分离。这样，当数据库变化时，只需要修改DAO层的代码而不影响Service层的业务逻辑。
* Controller层： Controller层是控制层，负责接收用户请求、调用相应的Service层方法，并将处理结果返回给前端。Controller层处理与用户交互相关的逻辑，通常是通过Web框架（如Spring MVC）来实现。它将用户请求的数据解析后，交由Service层处理，再将处理结果封装成相应的数据格式返回给前端。Controller层的设计使得用户界面和业务逻辑分离，提高了系统的灵活性和可维护性。
* SpringBoot中的DispatcherServlet是前端控制器（分发请求给Controller），实现了Servlet接口。DispatcherServlet接收了HTTP请求，并封装为HttpServletRequest对象。HttpServletResponse用于返回响应数据。
