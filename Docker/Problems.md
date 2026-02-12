# Problem

## 1. Error response from daemon: driver failed programming external connectivity on endpoint mynginx1

### Bug Description

启动Docker容器时失败，报错如下：

```shell
Error response from daemon: driver failed programming external connectivity on endpoint mynginx1 (iptables: No chain/target/match by that name.)
```

### Reproduction Steps
  
```shell
docker run -d --name mynginx1 -p 88:80 mynginx:v1.0
```

### Reason
  
在Docker服务开启时对防火墙进行了规则配置，修改了开放端口配置firewall重启后，会从iptables中移除Docker配置链，导致Docker容器无法启动。

### Solution

```shell
systemctl restart docker
```

### Reference

- [docker出现Error response from daemon: driver failed programming external connectivity on endpoint](https://www.cnblogs.com/FlyGoldfish/articles/16083946.html)

## nginx配置请求转发不生效

### Bug Description

将vue打包部署时，修改了nginx.conf，在nginx.conf中配置了请求转发，但是请求转发不生效，请求返回状态码404。
nginx配置如下：

```conf
location ~ ^/api(/|$) {
    proxy_next_upstream http_500 http_502 http_503 http_504 error timeout invalid_header;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://localhost:8081;  #代理的ip
    
    expires 24;
}
```

### Reproduction Steps

1.编写vue项目，使用npm run build打包，将打包后的文件夹dist放到nginx的html目录下。
2.修改nginx.conf，配置请求转发。
3.启动nginx服务。

### Reason

在本地开发环境，为了解决跨域问题，修改了vue.config.js：

```javascript
devServer: {
    proxy: {
        '/api': {
        target: 'http://localhost:8081',
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
        ws: true,
        secure: false
        }
    }
}
```

此处做了路由改写，实际后端访问地址为`http://localhost:8081/`，而nginx配置的代理地址为`http://localhost:8081/api`，导致请求定向错误。

### Solution

将nginx.conf进行路由改写：

```conf
location ~ ^/api(/|$) {
    proxy_next_upstream http_500 http_502 http_503 http_504 error timeout invalid_header;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://localhost:8081;  #代理的ip
    # 将 /api 替换为 /
    rewrite ^/api(.*)$ $1 break;
    expires 24;
}
```

正常转发，请求返回状态码200。

