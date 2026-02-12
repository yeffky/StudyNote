# Mybatis

* 简化JDBC开发

## 一、快速入门

### 1.导入Mybatis和MySQL Driver依赖

### 2.配置mybatis（数据库连接信息）

application.properties

```Java
# 驱动类
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
# 数据库
spring.datasource.url=jdbc:mysql://localhost:3306/mybatis
# username
spring.datasource.username="root"
# password
spring.datasource.password="123456"
```

### 3.编写对应DAO，需要编写方法、SQL语句和注解

## 二、JDBC

Java Database Connectivity：使用Java语言操作关系型数据库的一套API。提供规范接口，具体实现由各个厂商提供实现方法。JDBC的实现即为各个数据库的驱动。

### 1.操作

#### （1）注册驱动

#### （2）获取连接对象

#### （3）获取执行SQL的对象statement，执行SQL返回结果

#### （4）封装结果数据

#### （5）释放资源

## 三、数据库连接池

* 容器，负责分配、管理数据库连接
* 允许应用程序重复使用一个现有的数据库连接
* 释放空闲时间超过最大空闲时间的连接，避免没有释放连接而引起的资源浪费

### 1.标准接口：DataSource

#### （1）作用

获取连接

#### （2）常见产品

* Druid
* Hikari

## 四、Lombok

通过注解自动生成构造器、getter/setter、equals、hashcode、toString等方法，自动化生成日志变量，简化开发。

@NoArgsConstructor：生成无参构造
@AllArgsConstructor：生成除了static修饰字段以外带有各参数的构造器

## 五、Mybatis基础操作

### 1.参数占位符

\#{}代表占位符，执行时会替换为？，生成预编译SQL。
使用场景：参数传递
例：

```Java
// delete
    @Delete（"delete  from emp where id = #{id}"）
    public void delete（Integer id）;
```

\${}代表占位符，直接将参数拼接。
使用场景：对表名、列名动态设置
例：

```Java
// delete
    @Delete（"delete  from emp where id = ${id}"）
    public void delete（Integer id）;
```

### 2.配置控制台输出日志

```Java
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```

### 3.预编译SQL

```Java
==>  Preparing: delete from emp where id = ?
==> Parameters: 16（Integer）
<==    Updates: 0
```

* 性能更高，更安全：预编译SQL会将编译语句放入MYSQL服务器缓存，格式一样会命中缓存，只需要更改参数执行即可
* 防止SQL注入

### 4.主键返回

```Java
@Options（keyProperty = "id", useGeneratedKeys = true）
    @Insert（"insert into emp （username, name, gender, image, job, entrydate, dept_id, create_time, update_time）" +
            " values （#{username}, #{name}, #{gender}, #{image}, #{job}, #{entrydate}, #{deptId}, #{createTime}, #{updateTime}）"）
    public void insert（Emp emp）;
```

使用场景：在数据插入成功之后需要获取数据库主键。
例：添加套餐数据时需要维护套餐菜品关系表数据。

### 5.数据封装

实体类属性名和数据库字段名不一致不会自动封装。
解决方案：

* 给字段起别名
* 通过@Results， @Result注解手动映射封装

```Java
@Results（{
            @Result（column = "dept_id", property = "deptId"）,
            @Result（column = "create_time", property = "createTime"）,
            @Result（column = "update_time", property = "updateTime"）

    }）
    @Select（"select * from emp where id = #{id}"）
    public Emp getById（Integer id）;
```

* 开启mybatis驼峰命名自动映射方式

```Java
mybatis.configuration.map-underscore-to-camel-case=true
```

### 6.条件查询

涉及到模糊查询时，传递参数要用concat拼接

例：

```Java
@Select（"select * from emp where name like concat（'%', #{name}, '%'） and gender = #{gender} and entrydate" +
            " between #{begin} and #{end} order by update_time desc "）
    public List<Emp> list（String name, Short gender, LocalDate begin, LocalDate end）;
```

### 7.XML映射文件

#### （1）规范

* 与Mapper接口名称一致，并且将XML和Mapper接口放置在相同包下，XML文件存放在Resouces下，同包同名
* namespace属性要和Mapper接口全类名保持一致
* sql语句id与Mapper接口中的方法名一致，保持返回类型一致

例：

```xml
<mapper namespace="com.itheima.mapper.EmpMapper">
<!--    resultType：单条记录封装类型-->
    <select id="list" resultType="com.itheima.pojo.Emp">
        select * from emp where name like concat（'%', #{name}, '%'） and gender = #{gender}
        and entrydate between #{begin} and #{end} order by update_time desc
    </select>
</mapper>
```

### 8.动态SQL

#### （1）\<if>

用于判断条件是否成立。使用test属性判断，条件为true，拼接SQL。

#### （2）\<where>

where只会在子元素有内容的情况下插入where字句，并且会自动去除字句开头的and和or

例：

```xml
select *
from emp
<where>
    <if test="name != null">
        name like concat('%', #{name}, '%')
    </if>
    <if test="gender != null">
        and gender = #{gender}
    </if>
    <if test="begin != null and end != null">
        and entrydate between #{begin} and #{end} order by update_time desc
    </if>
</where>
```

#### （3）\<set>

用于删除update中set的额外逗号。where需要在\<set>之外

#### （4）\<foreach>

```xml
<!--    collection：遍历的集合-->
<!--    item：遍历出来的元素-->
<!--    separator：分隔符-->
<!--    open：便离开时前拼接的SQL片段-->
<!--    close：遍历结束后的拼接的SQL片段-->
    <delete id="deleteByIds">
        delete from emp where id in
            <foreach collection="ids" item="id" separator="," open="(" close=")">
                #{id}
            </foreach>
    </delete>
```

#### （5）\<sql>\<include>

```xml
<sql id="commonSelect">
    select id,id, username, password, name, gender, image, job, entrydate, dept_id, create_time, update_time
    from emp
</sql>
<select id="list" resultType="com.itheima.pojo.Emp">
    <include refid="commonSelect"/>
    <where>
        <if test="name != null">
            name like concat('%',
            #{name},
            '%'
            )
        </if>
        <if test="gender != null">
            and gender =
            #{gender}
        </if>
        <if test="begin != null and end != null">
            and entrydate between
            #{begin}
            and
            #{end}
            order
            by
            update_time
            desc
        </if>
    </where>
</select>
```

封装可重用的SQL片段

### 9.Mybatis常见报错及解决方法

#### （1）元素内容必须由格式正确的字符数据或标记组成

特殊字符需要转义

```xml
&lt;<  小于号；

&gt;> 大于号； 

&amp; & 和 ；

&apos;  ‘’单引号； 

&quot; “”  双引号；
```
