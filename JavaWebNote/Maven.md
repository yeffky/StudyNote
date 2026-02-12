# Maven

## 一、依赖传递

### 1.传递性

* 直接依赖：在当前项目中通过依赖配置建立的依赖关系
* 间接依赖：被依赖的资源依赖其他资源，则当前项目间接依赖其他资源

### 2.排除依赖

主动断开依赖的资源，被排除的资源无需指定版本
\<exclutions>
\<exclution>
...
\</exclutions>
\</exclution>

## 二、依赖范围

### 1.作用范围

通过\<scope>...\</scope>控制依赖作用范围

* 主程序范围：main文件夹
* 测试范围：test文件夹
* 打包运行：package指令范围

### 2.scope

* compile：默认 log4j
* test：测试范围 junit
* provided：打包无效 servlet-api
* runtime：主程序无效 jdbc驱动

### 3.maven生命周期

为所有maven项目进行抽象和统一

#### (1)三套独立生命周期

* clean：清理
* default：核心工作，如：编译、测试、打包、安装
* site：生成报告、发布站点

#### (2)重点阶段

* clean：clean
* default：compile、test、package、install

#### (3)阶段有序

同一套生命周期中后面的阶段依赖于前面的阶段，后面的阶段运行前面的也要运行

#### (4)重点阶段的作用

* clean：移除上一次构建的文件
* compile：编译项目源代码
* test：使用合适的单元测试框架运行测试
* package：将编译后的文件打包（jar、war）
* install：安装项目到本地仓库


