# Git

## 1. git上传到远程仓库

### 1.1. 创建远程仓库

1. 登录github
2. 点击右上角+号，选择New repository
3. 填写仓库名称，选择是否公开，填写描述，点击Create repository

### 1.2. 将本地仓库上传到远程仓库

1. 在本地仓库的根目录下打开git bash
2. 输入命令`git remote add origin https://github.com/username/repository.git`，将本地仓库与远程仓库关联起来
3. 输入命令`git push -u origin master`，将本地仓库的内容推送到远程仓库

### 1.3. 回退历史版本

1. 查看历史版本：`git log`
2. 回退到指定版本：`git reset --hard HEAD^`，其中`HEAD^`表示上一个版本，`HEAD^^`表示上上一个版本，`HEAD~100`表示上100个版本
3. 查看当前版本：`git reflog`，可以查看每次命令的记录，包括回退的版本
4. 回退到指定版本：`git reset --hard commit_id`，其中`commit_id`是版本号的前几位即可，不需要全部输入

### 1.4. 回退到远程仓库版本

```git reset --hard origin/master // origin代表你远程仓库的名字，master代表分支名```

### 1.5. 撤销修改
