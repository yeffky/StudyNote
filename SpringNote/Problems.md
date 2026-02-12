# Exception in thread "main" java.lang.ClassNotFoundException: DemoApplication

## Bug Description

在运行SpringBoot项目时，出现如下异常：

```shell
Exception in thread "main" java.lang.ClassNotFoundException: DemoApplication
```

## Reproduciton Steps

1.maven打包项目，生成app.jar。依赖如下：

```xml
<plugins>
    <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <executions>
            <execution>
                <phase>package</phase>
                <goals>
                    <goal>repackage</goal>
                </goals>
            </execution>
        </executions>
        <configuration>
            <includeSystemScope>true</includeSystemScope>
            <mainClass>DemoApplication</mainClass>
        </configuration>
    </plugin>
</plugins>
```

2.上传服务器，执行如下命令：

```shell
java -jar app.jar
```

## Reason

1.在pom.xml文件中，`<mainClass>`标签中的类名是错误的，需要将包路径和类名写全。

## Solution

修改configuration下的mainClass为：

```xml
<configuration>
    <includeSystemScope>true</includeSystemScope>
    <mainClass>com.example.demo.DemoApplication</mainClass>
</configuration>
```

# feign.RetryableException: 不知道这样的主机。 (nacos-pay-provider) executing GET http://nacos-pay-provider/pay/nacos/1

## Bug Description

在调用Feign api时，出现如下异常：

```shell
feign.RetryableException: 不知道这样的主机。 (nacos-pay-provider) executing GET http://nacos-pay-provider/pay/nacos/1
```

调用消费者对应方法，返回json数据：

```json
{
    "code": "500",
    "message": "不知道这样的主机。 (nacos-pay-provider) executing GET http://nacos-pay-provider/pay/nacos/1",
    "data": null,
    "timestamp": 1738382623457
}
```


## Reproduciton Steps

1.启动nacos-pay-provider服务，并启动nacos-pay-consumer服务。
2.调用nacos-pay-consumer服务中的Feign api。

## Reason

在nacos-pay-consumer服务中，openFeign的负载均衡组件缺失，需要手动引入依赖loadbalancer。

## Solution

在nacos-pay-consumer服务中，引入如下依赖：

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-loadbalancer</artifactId>
</dependency>
```

# feign Api接口中注解问题：not annotated with HTTP method type (ex. GET, POST)

### Bug Description

在调用Feign api时，出现如下异常：

```shell
java.lang.IllegalStateException: Method PayFeignSentinelApi#getPayByOrderNo(String) not annotated with HTTP
```

## Reproduciton Steps

1.启动nacos-pay-provider服务，并启动nacos-pay-consumer服务。
2.调用nacos-pay-consumer服务中的Feign api。

## Reason

SpringCloudAlibaba版本匹配问题，原先配置版本为：

```xml
<spring.boot.version>3.2.0</spring.boot.version>
<spring.cloud.version>2023.0.0</spring.cloud.version>
<spring.cloud.alibaba.version>2022.0.0.0</spring.cloud.alibaba.version>
```

查看官网文档[SpringCloudAlibaba版本发布说明](https://sca.aliyun.com/docs/2023/overview/version-explain/?spm=5176.29160081.0.0.74805c72tNhhrp)，发现版本对应关系如下：

| Spring Cloud Alibaba Version | Spring Cloud Version | Spring Boot Version |
| ---------------------------- | -------------------- | -------------------- |
| 2023.0.1.0*                   | Spring Cloud 2023.0.1             | 3.2.4                |
| 2023.0.0.0-RC1                   | Spring Cloud 2023.0.0           | 3.2.0                |

## Solution

因此，需要修改版本为：

```xml
<spring.boot.version>3.2.0</spring.boot.version>
<spring.cloud.version>2023.0.0</spring.cloud.version>
<spring.cloud.alibaba.version>2023.0.0.0-RC1</spring.cloud.alibaba.version>
```
