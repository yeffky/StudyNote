# 项目负责内容

主要负责页面设计、UI设计以及页面点击与跳转逻辑部分代码的编写。

## 一、MainActivity

设置了Navigation，并编写了NavigationUtils工具类用于进行fragment跳转。（注：Fragment相对于Activity来说更加碎片化，生命周期环节更多）
改写了navView的菜单点击事件，根据选中的menuId触发对应导航事件，使用FragmentManager类来管理fragment，并使用NavigationUtils中编写的showFragment方法来跳转fragment。

## 二、HomeFragment

首页主体有GridView组成，每个Grid显示一个管理的应用。初始化页面时需要绑定视图与响应事件。（例如应用点击事件会触发Activity跳转、授权事件、并启动相应的一些hook函数。

## 三、SceneFragment

涉及到场景加载，通过SQLite动态查询场景数据，并生成相应视图。主要通过Adapter实现。将场景列表（SceneDataList）传入Adapter并根据插入、删除、刷新等更新视图。

