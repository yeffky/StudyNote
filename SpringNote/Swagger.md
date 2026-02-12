# Swagger

## 1.常用注解

```java
@Tag：用在Controller类上，说明该类的作用
@Parameter：用在方法上，说明参数的作用
@Parameters：用在方法上，包含多个@Parameter
@Schema：用在model层的JavaBean，描述模型作用和每个属性
@Operation：用在方法上，说明方法的作用
@ApiResponses：用在方法上，用于表示一组响应码
```

## 2.使用方式

```java
package org.example.cloud.config;

import io.swagger.v3.oas.models.ExternalDocumentation;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springdoc.core.models.GroupedOpenApi;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @Author WongSilver
 * @Date 2024/3/12 21:55
 * @Description <a href="http://localhost:8001/swagger-ui/index.html">Swagger3管理页面</a>
 */
@Configuration
public class Swagger3Config {

    @Bean
    public GroupedOpenApi payApi() {
        return GroupedOpenApi.builder().group("支付微服务模块").pathsToMatch("/pay/**").build();
    }

    @Bean
    public GroupedOpenApi otherApi() {
        return GroupedOpenApi.builder().group("其他微服务模块").pathsToMatch("/other/**").build();
    }

    @Bean
    public OpenAPI docsOpenApi() {
        return new OpenAPI()
                .info(new Info()
                        .title("spring-cloud")
                        .description("通用设计")
                        .version("v1.0")
                )
                .externalDocs(new ExternalDocumentation()
                        .description("")
                        .url("")
                );
    }
}
```

访问地址：http://localhost:8001/swagger-ui/index.html，查看接口文档
