# W5_Soar_APP项目介绍

> 作者是开发新手，高手轻喷！

存放W5 Soar的APP，有自己开发的，有网上收集的。

本项目是基于[W5 Soar](https://w5.io/)使用，如只想使用Python的功能，可以下载App的源代码，功能可以直接使用。

如需沟通，请提issues。

# APP使用教程

https://w5.io/help/dev/dev6.html

# 已实现APP

## [ARL_API](./ARL_API)

通过ARL的接口，发起ARL的任务，具体功能，查看：ARL_API/readme.md

## [AWVS](./AWVS)

通过AWVS接口，发起扫描任务，具体功能，查看：AWVS/readme.md

此APP参考文档：https://github.com/0xmin/awvs-scan

## [IPQuery](./IPQuery)

IP相关的功能，已实现如下功能，具体功能，查看：IPQuery/readme.md

1. 查询是否是私有IP
2. 旁站查询
3. 查询ip地理位置

# 版本记录

> 每个app的版本记录，可以在app目录下的readme.md中查看。这里记录整体的版本记录。

## V0.1.2 AWVS 查询新增漏洞数

**使用场景：**

配合定时器使用，可以实现定时推送awvs发现的漏洞。

## V0.1.1 增加ARL_API接口功能

**新增功能：**

ARL_API增加查询WIH信息接口功能，详情查看：ARL_API/readme.md

**修复内容：** 

修复ARL_API的任务查询接口功能

**优化内容：**

优化ARL_API的接口实现

## V0.1.0 发布三个app

每个app的用法，可以在app目录下的readme.md中查看。

1. ARL_API
 
3. AWVS

4. IPQuery

 
# 致谢

感谢Github上的各种开源项目，帮我节省了不少时间。
