# Axios

* 基于promise网络请求库，作用于node.js和浏览器中
* Axios在浏览器端使用XMLHttpRequests发送网络请求，能够自动完成JSON数据转换

## 一、网络请求

```JS
axios.get(url, data).then(function(response){}).catch(function(error){})
axios.post(url, data).then(function(response){}).catch(function(error){})
```

## 二、异步回调

```JS
async function getUser() {
    try {
        const response = await axios.get

    }
    catch(error) {

    }
}
```

## 三、跨域请求

* 前后端运行于不同端口，前端axios请求不知道往那个端口进行请求
* 为了保证浏览器的安全，不同源的客户端脚本没有授权不能读写对方资源，这是同源策略
* 同源：两个页面具有相同protocol、host、port。当一个请求url的三者其中有一个与当前url不同即为跨域，无法读取非同源网页的Cookie，无法向非同源地址发送ajax请求

## 四、跨域问题解决

* CORS可以在不破坏既有规则的情况下通过后端实现CORS接口，从而实现跨域
* CORS将请求分为两类：简单请求和非简单请求
  * 简单请求：GET/POST/HEAD，除Accept、Accpt-Language、Content-Language、Last-Event-ID、Content-Type没有自定义请求头，Content-Type的值只有：text/plain、multipart/form-data、application/x-www-form-urlencoded
* 简单请求的处理：
CORS的策略是请求时在请求头添加一个Origin字段、服务器收到请求后根据该字段判断是否允许访问，如果允许在HTTP头信息中添加Access-Control-Allow-Origin字段
* 非简单请求的处理：
浏览器会在发送真是请求之前增加一次OPTION请求，成为预检请求。预检请求包含真实请求的信息，询问服务器是否允许这样的操作。服务器收到请求时对请求和预检请求进行对比验证，通过后会在返回HTTP头信息中心添加Access-Control-Allow-Methods、Access-Control-Allow-Headers（真是请求允许的方法和字段）、Access-Control-Allow-Credentials（是否允许发送、处理cookie）、Access-Control-Allow-Max-Age：预检请求的有效期

SpringBoot配置

```Java
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOriginPatterns("*")
                .allowedMethods("POST", "GET", "OPTIONS", "DELETE")
                .maxAge(168200)
                .allowedHeaders("*")
                .allowCredentials(true);
    }
}
```

注解配置

在对应Controller添加@CrossOrigin

## 五、axios与Vue整合

全局配置

```JS
import axios from 'axios'
axios.defaults.baseURL = "http://localhost:8081"//服务器根路径
Vue.prototype.$http = axios
```

```Vue
//this指代funtion
axios.get("http://localhost:8081/depts").then(function(response) {
    console.log(response)
    this.tableData = response.data
})
//this指代created，箭头函数作用域继承父级
this.$http.get("/depts").then((response) => {
    console.log(response)
    this.tableData = response.data
})
```