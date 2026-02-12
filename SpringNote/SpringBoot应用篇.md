# SpringBoot应用篇

## 一、请求

### 1.@RequestMapping

可以接受简单参数，参数名和形参名必须匹配。可接收GET、POST。

### 2.@RequestParam(用于接收复杂参数)

```Java
语法：@RequestParam(value=”参数名”,required=”true/false”,defaultValue=””)
 
value：参数名
 
required：是否包含该参数，默认为true，表示该请求路径中必须包含该参数，如果不包含就报错。
 
defaultValue：默认参数值，如果设置了该值，required=true将失效，自动为false,如果没有传该参数，就使用默认值
```

### 3.复杂实体

* 传递参数：需要展示实体中的实体参数。
* 例：User中包含Address，需要写address.province参数。

### 4.数组集合参数

* 传递参数：key相同，value不同
* 集合List接收时要加@RequestParam注解进行封装。

### 5.日期参数

* 接收参数类型为LocalDateTime
* 添加@DateTimeFormat(pattern="yyyy-MM-dd HH:mm:ss")指定格式

### 6.Json参数

* 使用@RequestBody来识别参数并封装到实体类

```Java
例：
    @RequestMapping("/jsonParam")
    public String jsonParam(@RequestBody User user)
```

### 7.路径参数

* 通过URL传递参数
* 使用@PathVariable获取路径参数

```Java
例：
@RequestMapping("/path/{id}")
public String pathParam(@PathVariable Integer id)

@RequestMapping("/path/{id}/{name}")
public String pathParam2(@PathVariable Integer id, @PathVariable String name) 
```

## 二、响应

### 1.@ResponseBody

* 类型：方法注解、类注解
* 位置：Controller方法上/类上
* 作用：将返回值直接响应，如果返回值为实体或是JSON，则会转换为JSON格式
* 说明：@RestController=@Controller + @ResponseBody

### 2.统一响应结果

构建Result响应类(code, msg, data)

## 三、静态资源存放

默认存放目录为：classpath:/static、classpath:/public、classpath:/resources

## 四、分层解耦

### 1.三层架构

* controller：控制层，接收前端发送请求，对请求进行处理并响应数据
* service：业务逻辑层，处理具体的业务逻辑
* dao：数据访问层，负责数据访问操作，包括增删改查

### 2.分层解耦

* 内聚：各模块内部功能联系
* 耦合：各模块之间关联程度

![本地路径](./1.jpg "IOC-DI")

* IOC：Inversion of Control，控制反转。对象控制权由程序自身转移到容器（无须new一个对象，降低耦合性，避免实现类更名而要进行大量程序变动）
* DI：Dependency Injection，依赖注入。容器为应用程序提供运行时所需资源
* Bean：IOC容器中创建和管理的对象

### 3.IOC&DI实现

#### (1)@Component实现容器化管理(IOC)

#### (2)@Autowired实现自动装配，依赖注入(DI)

### 4.IOC详解

#### (1)Bean声明

* @Component：基础注解，不属于以下三类时使用
* @Controller
* @Service
* @Repository；和mybatis整合，用得少

可以使用value="xx"指定bean名字

#### (2)Bean扫描

* bean注解要生效需要被@ComponentScan扫描
* @ComponentScan已经包含在@SpringBootApplication中，默认扫描范围时启动类所在包和子包

### 5.DI详解

* @Autowired：存在多个相同类型Bean会报错
* @Primary：设置Bean优先值
* @Qualifier：配合@Autowired使用，指明装配对应实现类
* @Resource：不配合@Autowired，直接使用，指明装配对应类
* @Autowired和@Resource区别：
  * @Autowired是spring框架提供，按类型注入；@Resource是JDK提供，按名称注入

## 五、PageHelper插件

便捷化分页查询

代码示例：

```Java
@Override
public PageBean page(Integer page, Integer pageSize) {
    PageHelper.startPage(page, pageSize);
    List<Emp> empList = empMapper.list();
    Page<Emp> p = (Page<Emp>) empList;
    return new PageBean(p.getTotal(), p.getResult());
}
```

## 六、文件上传

### 1.前端页面

* 表单项：type="file"
* 表单提交方式：POST
* 表单entrytype：multipart/form-data

### 2.服务端接收文件

```Java
@PostMapping("/upload")
public Result updaload(String username, Integer age, MultipartFile image) {
    log.info("文件上传：{}, {}, {}", username, age, image);
    return Result.success();
}
```

### 3.本地存储

接收到上传文件后将文件存储在本地磁盘

```Java
@PostMapping("/upload")
public Result updaload(String username, Integer age, MultipartFile image) throws IOException {
    log.info("文件上传：{}, {}, {}", username, age, image);

    String originalFilename = image.getOriginalFilename();
    image.transferTo(new File("F:\\StudyNote\\Java\\SpringBoot\\Images\\" + originalFilename));
    return Result.success();
}
```

### 4.OSS云存储

使用OSS可以通过网络随时存储和调用文件

## 七、参数配置化

### 1.properties

在properties配置文件中声明类中参数，并使用@Value注解注入

```Java
// Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。
@Value("${aliyun.oss.endpoint}")
private String endpoint;
@Value("${aliyun.oss.accessKeyId}")
private String accessKeyId;
@Value("${aliyun.oss.accessKeySecret}")
private String accessKeySecret;
// 填写Bucket名称，例如examplebucket。
@Value("${aliyun.oss.bucketName}")
private String bucketName;
```

### 2.yml

* 大小写敏感
* 数值前必须有空格
* 使用缩进代表层级关系

```yml
server:
  port: 8080
#对象
user:
  name: Tom
  age: 20
#数组
hobby:
  - java
  - python
  - C
```

### 3.@Configuration


配置参数

```Java
@Data
@Component
@ConfigurationProperties(prefix = "aliyun.oss")
public class AliOSSProperties {
    private String endpoint;
    private String accessKeyId;
    private String accessKeySecret;
    private String bucketName;
}
```

获取配置参数

```Java
@Autowired
private AliOSSProperties aliOSSProperties;

public String upload(MultipartFile file) throws IOException {
    String endpoint = aliOSSProperties.getEndpoint();
    String accessKeyId = aliOSSProperties.getAccessKeyId();
    String accessKeySecret = aliOSSProperties.getAccessKeySecret();
    String bucketName = aliOSSProperties.getBucketName();
```

## 八、登录认证和校验

当用户未登录时应该限制操作，需要进行登录校验。登录校验使用登录标记与统一拦截技术。登录成功之后在每一次请求都可以获取到登录标记。统一拦截包括过滤器filter以及拦截器Interceptor。

### 1.会话技术

* 会话：用户打开浏览器，访问web资源，会话建立，直到断开会话结束。
* 会话跟踪：维护浏览器状态的方法，服务器需要识别多次请求是否来自同一浏览器，以便在同义词会话的多次请求间共享数据。
* 会话跟踪方案：
  * 客户端会话跟踪技术：Cookie
  * 服务端会话跟踪技术：Session
  * 令牌技术

#### （1）Cookie

登录后服务端生成Cookie，存储一些相关的用户信息。服务端自动将Cookie响应给浏览器，浏览器自动将Cookie存储在本地，之后的请求Cookie会自动响应到服务端。如果服务端识别不到来自客户端的Cookie说明用户尚未登录。

优点：

* HTTP协议支持，请求头和响应头用于发送Cookie

缺点：

* 移动端APP无法使用Cookie
* 用户可以禁用Cookie
* Cookie不能跨域

跨域： 三个维度（协议、IP/域名、端口），有一个不同就是跨域。

#### （2）Session

服务端响应时将sessionID封装在Cookie中，浏览器后续请求携带sessionID。通过sessionID来区分会话。

优点：

* 存储在服务端，安全

缺点：

* 服务器集群环境无法直接使用session：当前服务器普遍使用负载均衡服务器进行服务转发，如果同一浏览器两次访问的不是同一台服务器则获取不到同一session。

* Cookie的缺点

#### （3）令牌技术

登录成功时生成令牌，响应时存储在客户端，后续请求携带令牌到服务端。服务端校验令牌，令牌有效则用户已经登陆，同一会话共享数据将数据存储在令牌中。

优点：

* 支持PC端和移动端（因为可以不使用Cookie存储令牌）
* 解决集群环境下的认证问题
* 减轻服务端存储压力

## 九、JWT令牌

JSON Web Token: 定义了一种简洁的、自包含的格式，用于在通信双方以json数据格式安全传输信息。由于数字签名的存在，这些信息是可靠的。
简洁：jwt是字符串
自包含：jwt令牌可以存储自定义内容，例如可以存储用户相关信息

### 1.组成

x.x.x：由json数据进行Base64编码转化而来。
Base64：是一种基于64中可打印字符（A-Z a-z 0-9 + /)来表示二进制数据的编码方式

* 第一部分：Header，加密算法
* 第二部分：Payload，编译内容（自定义内容和默认内容）
* 第三部分：Signature，签名，防止Token被篡改，确保安全性。将header、payload部分，并加入指定密钥，通过指定签名算法计算而来

### 2.应用场景

登录认证：

* 登录成功后生成令牌
* 后续请求携带JWT令牌，每次处理请求之前先校验令牌，通过后再处理

### 3.jwt生成与解析

```Java
@Test
public void testGenJwt() {
    Map<String, Object> cliams = new HashMap<>();
    cliams.put("id", 1);
    cliams.put("name", "tom");
    String jwt = Jwts.builder()
            .signWith(SignatureAlgorithm.HS256, "itheima") //签名算法
            .setClaims(cliams) //自定义内容
            .setExpiration(new Date(System.currentTimeMillis() + 3600 * 1000)) //设置有效期
            .compact();
    System.out.println(jwt);
}

@Test
public void testParseJwt() {
    Claims claims = Jwts.parser()
            .setSigningKey("itheima").parseClaimsJws("eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidG9tIiwiaWQiOjEsImV4cCI6MTcwNzQ2NTUzNn0.2ZSILs2AErRWmQQXtNdq6AQun56zSv9ncr_CboyQp68")
            .getBody();
    System.out.println(claims );
}
```

## 十、过滤器Filter

请求和响应都要通过过滤器过滤,属于JavaWeb中的Servlet技术

![本地路径](./2.jpg "Filter")

常用场景：

* 登录校验
* 统一编码处理
* 敏感字符处理

### 1.快速入门

```Java
@WebFilter(urlPatterns = "/*")
public class DemoFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.printf("init");
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("filter");
        filterChain.doFilter(servletRequest, servletResponse); //放行请求和响应
    }


    @Override
    public void destroy() {
        System.out.println("destroy");
    }
}
```

```Java
@ServletComponentScan
@SpringBootApplication
public class TliasWebManagementApplication {

    public static void main(String[] args) {
        SpringApplication.run(TliasWebManagementApplication.class, args);
    }

}
```

### 2.拦截路径

|拦截路径|urlPatterns|
|-----------|-----------|
|拦截具体路径|/login|
|拦截目录|/emps/*|
|拦截全部|/*|

### 3.过滤器链

* 介绍：一个web应用可以配置多个过滤器，多个过滤器形成过滤器链（第一个放行访问第二个，第二个通过才能访问web资源。
* 顺序：过滤器优先级按照过滤器类名的自然排序

## 十一、Interceptor

* 概念：动态拦截方法调用的机制，类似于过滤器。Spring框架提供用于动态拦截控制器方法执行
* 作用：拦截请求，在方法调用前后，根据业务需要执行预先设定的代码

### 1.拦截器方法

preHandle：目标资源方法前执行，根据返回值判断是否放行
postHandle ：目标资源方法执行后执行
afterCompletion：视图渲染完毕后执行，最后执行

### 2.使用流程

* 定义拦截器，实现HandlerInterceptor（@Component）
* 注册拦截器（Configuration）

### 3.示例代码

```Java
@Component
public class LoginCheckInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("prehandle");
        return true;
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("posthandle");
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("aftercompletion");
    }
}
```

```Java
@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Autowired
    private LoginCheckInterceptor loginCheckInterceptor;
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(loginCheckInterceptor).addPathPatterns("/*");
    }
}
```

* addPathPatterns：需要拦截那些资源
* excludePathPatterns：不需要拦截哪些资源

### 4.拦截路径

|拦截路径|含义|
|-------|----|
|/*|一级路径|
|/**|任意级路径|
|/depts/*|/depts下的一级路径|
|/depts/**|/depts下的任意级路径|

### 5.执行流程

浏览器——过滤器——DispatcherServlet（Tomcat只能识别Servlet）——Interceptor——Controller

![本地图片](./3.jpg "拦截器执行流程")

### 6.和Filter的不同

拦截范围：Filter拦截所有资源，Interceptor只拦截Spring环境中的资源

### 7.登录校验

```Java
@Override
public boolean preHandle(HttpServletRequest req, HttpServletResponse resp, Object handler) throws Exception {
    String url = req.getRequestURL().toString();
    log.info("url:{}", url);

    if (url.contains("login")) {
        log.info("login");
        return true;
    }
    String jwt = req.getHeader("token");
    if (! StringUtils.hasLength(jwt)) {
        log.info("请求头token为空，返回未登录的信息");
        Result error = Result.error("NOT_LOGIN");
        String not_login = JSONObject.toJSONString(error);
        resp.getWriter().write(not_login);
        return false;
    }
    try {
        JwtUtils.parseJWT(jwt);
    } catch (Exception e) {
        e.printStackTrace();
        log.info("请求头token为空，返回未登录的信息");
        Result error = Result.error("NOT_LOGIN");
        String not_login = JSONObject.toJSONString(error);
        resp.getWriter().write(not_login);
        return false;
    }
    log.info("令牌正确，放行");
    return true;
}
```

## 十二、异常处理

三层架构会将异常抛向Controller

### 1.全局异常处理器

```Java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class) //捕获所有异常
    public Result ex(Exception ex) {
        ex.printStackTrace();
        return Result.error("对不起，操作失败");
    }
}
```

## 十三、事务管理

### 1.事务注解

* 注解：@Transactional
* 位置：业务（service）层的方法上、类上、接口上，通常加在特定方法上
* 作用：将当前方法交给spring进行事务管理

### 2.rollbackFor

默认情况下，只有出现RuntimeException才回滚异常。rollbackFor用于指定异常类型回滚。

```Java
//所有异常均进行回滚
@Transactional(rollbackFor = Exception.class)
```

### 3.propagation

事务传播行为：当一个事务方法被其他事务方法调用时，这个事务方法应该如何进行事务控制

![本地路径](4.jpg "propagation")

REQUIRES_NEW：挂起当前事务，创建新事务

## 十四、AOP

### 1.概述

* 概念：Aspect Oriented Programming：面向切面编程、面向方面编程
* 实现：动态代理是面向切面编程最主流的实现。而SpringAOP是Spring框架的高级技术，旨在管理bean对象的过程中，主要通过底层的动态代理机制，对特定的方法进行编程

### 2.示例代码（统计各个业务层方法执行耗时）

```Java
@Slf4j
@Component
@Aspect
public class TimeAspect {
    @Around("execution(* com.itheima.service.*.* (..))") //切入点表达式
    //Advice
    public Object recordTime(ProceedingJoinPoint joinPoint) throws Throwable {
        Long begin = System.currentTimeMillis();

        Object result = joinPoint.proceed();

        Long end = System.currentTimeMillis();
        log.info(joinPoint.getSignature() + String.valueOf(end-begin));
        return result;
    }
}
(* com.itheima.service.*.* (..)): 返回值 类与方法 参数

```

### 3.场景

* 记录操作日志
* 权限控制
* 事务管理

### 4.核心概念

* 连接点：JoinPoint，可以被AOP控制的方法（暗含方法执行时的相关信息）
* 通知：Advice，指哪些重复的逻辑，也就是共性功能（最终体现为方法）
* 切入点：PointCut：匹配连接点的条件，通知仅会在切入点方法执行时被应用
* 切面：通知＋切入点
* 目标对象：Target，通知所应用的对象

### 5.执行逻辑

![本地路径](5.jpg "aop")

通过动态代理来进行功能增强

### 6.AOP进阶

#### (1)通知类型

* @Around：环绕通知，通知方法在目标方法前、后都被执行
  * 需要调用ProceedingJoinPoint.proceed()来让原始方法执行
  * 通知方法的返回值必须指定为Object，来接收原始方法的返回值
* @Before：前置通知，通知方法在目标方法前被执行
* @After：后置通知：在目标方法后执行，无论有无异常都执行
* @AfterReturning：返回后通知，有异常不会执行
* @AfterThrowing：异常后通知，发生异常后执行

#### (2)复用切入点表达式

```Java
@Pointcut("execution(* com.itheima.service.*.* (..))        ")
private void pt() {
}

//    @Around("execution(* com.itheima.service.*.* (..))") //切入点表达式
@Around("pt()")
public Object recordTime(ProceedingJoinPoint joinPoint) throws Throwable {
    Long begin = System.currentTimeMillis();

    Object result = joinPoint.proceed();

    Long end = System.currentTimeMillis();
    log.info(joinPoint.getSignature() + String.valueOf(end-begin));
    return result;
}
```

#### (3)通知顺序

##### ①不同切面类中，按照类名字母排序

目标方法前的通知方法：字母排名靠前的先执行
目标方法后的通知方法：字母排名靠后的先执行

##### ②用@Order在切面类上控制顺序

```Java
@Order(1)
@Slf4j
@Component
@Aspect
public class TimeAspect 
```

#### (4)切入点表达式-execution

* 语法：execution(访问修饰符？ 返回值 包名.类名.？方法名（参数类型的全类名) throws 异常？)（问号处可以省略）（可以基于接口构造表达式）

* 通配符：
  * *:单个独立的任意符号，可以通配任意返回值、包名、类名、方法名、任意类型的一个参数
  * ..：多个连续的任意符号，可以通配任意层级的包，或任意类型、个数的参数

```Java
//    @Pointcut("execution(* com.itheima.service.*Service.delete*(*))") //匹配以Service结尾，delete开头的仅含一个参数的方法
//    @Pointcut("execution(* com.itheima.service.DeptService.*(..))") //匹配DeptService中所有带有任意个参数的方法
//    @Pointcut("execution(* com..*.*(..))") //匹配com包下所有层级的所有方法
@Pointcut("execution(* com.itheima.service.DeptService.list()) || " +
        "execution(* com.itheima.service.DeptService.delete(java.lang.Integer))")//匹配两种方法
public void pt() {
}
```

#### (5)切入点表达式@annotation

用于匹配标识有特定注解的方法

注解类

```Java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface MyLog {
}
```

连接点

```Java
@MyLog
@Override
public List<Dept> list() {
    List<Dept> deptList = deptMapper.list();
    return deptList;
}

@MyLog
@Override
public void delete(Integer id) {
    //1. 删除部门
    deptMapper.delete(id);
}
```

切入点表达式

```Java
@Pointcut("@annotation(com.itheima.aop.MyLog)")
public void pt() {
}
```

#### (6)连接点

JoinPoint抽象了连接点，用它可以获得方法执行时的相关信息，如类名、方法名、方法参数等。

* 对于@Around，获取连接点只能使用ProceedingJoinPoint
* 对于其他通知，只能使用JoinPoint

```Java
@Before("pt()")
public void before(JoinPoint joinPoint) {
    log.info("before");
}

@Around("pt()")
public Object around(ProceedingJoinPoint joinPoint) throws Throwable {
    log.info("around before");
    //获取类名
    joinPoint.getClass().getName();
    //获取目标方法
    joinPoint.getSignature().getName();
    //获取参数
    joinPoint.getArgs();
    //放行目标方法执行
    Object result = joinPoint.proceed();
    //返回目标方法的返回值
    return result;
}
```

### (7)日志功能实现

```Java
@Component
@Aspect
@Slf4j
public class LogAspect {

    //Servlet注入
    @Autowired
    private HttpServletRequest request;

    @Autowired
    private OperateLogMapper operateLogMapper;

    @Around("@annotation(com.itheima.anno.Log)")
    public Object recordLog(ProceedingJoinPoint joinPoint) throws Throwable {

        // operator
        String jwt = request.getHeader("token");
        Claims claims = JwtUtils.parseJWT(jwt);
        Integer operateUser = (Integer) claims.get("id");
        // operateTime
        LocalDateTime operateTime = LocalDateTime.now();

        // operateClass
        String className = joinPoint.getTarget().getClass().getName();

        //操作方法名
        String methodName = joinPoint.getSignature().getName();

        // operateArgs
        Object[] args = joinPoint.getArgs();
        String methodParams = Arrays.toString(args);

        Long begin = System.currentTimeMillis();
        // 调用原始方法
        Object result = joinPoint.proceed();
        Long end = System.currentTimeMillis();

        //方法返回值
        String returnValue = JSONObject.toJSONString(result);

        // 操作耗时
        Long costTime = end - begin;

        // 记录操作日志
        OperateLog operateLog = new OperateLog(null, operateUser, operateTime, className, methodName, methodParams, returnValue, costTime);

        operateLogMapper.insert(operateLog);

        log.info("aop记录操作日志:{}", operateLog);
        return result;
    }
}
```














