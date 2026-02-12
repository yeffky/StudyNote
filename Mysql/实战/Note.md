<!--
 * @Author: yeffky
 * @Date: 2025-03-04 18:45:05
 * @LastEditTime: 2025-03-06 16:25:50
-->
# Note

## 1.创建数据库，指定utf8mb4字符集

```sql
CREATE DATABASE IF NOT EXISTS `xhs_flow` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

## 2.创建表

```sql
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `id` int(11) NOT NULL,
  `content` json NULL,
  `date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
```

## 3.存储文案文本过长处理

当我尝试将一篇长文章存储进数据库时，报错如下：

```shell
[Err] 1406 - Data too long for column 'content' at row 1
```

解决方法：将`content`字段类型改为`LONGTEXT`。

```sql
ALTER TABLE `goods` MODIFY COLUMN `content` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL;
```
