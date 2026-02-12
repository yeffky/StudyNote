# HBase

## 一、HBase基础架构

![本地路径](\image.png "架构图")

### 1.Master

通过zk监控管理RegionServer，元数据变化的接口，管理hbase:meta

### 2.RegionServer

管理Region

### 3.HDFS集群

存储表格数据，每张表对应一个文件夹

### 4.Region

有若干Store，存储HFile
