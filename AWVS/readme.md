## 【ARL API】APP使用说明

> **作者：** BigYoung
>
> **MyBlog：** https://sec.bigyoung.cn
>
> **联系方式：** Blog评论里留言
>
> **免责声明：** 禁止用于非法用途，一切违法行为与作者无关。

## 动作列表

### scan_main

**参数：**

| 参数             | 类型       | 必填  | 备注                                                                                                                                                  |
|----------------|----------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **scan_type**  | select   | `是` | 选择此次扫描发起的扫描类型，如：1:完全扫描，2:高风险漏洞，3:XSS漏洞，4:SQL注入漏洞，5:弱口令检测，6:Crawl Only，7:恶意软件扫描，8:仅添加，这行不会生效，9:apache-log4j，10:custom-Bounty，11:custom-cve，12:custom |
| **api_key**    | text     | `是` | 调用AWVS的认证token                                                                                                                                      |
| **awvs_url**   | text     | `是` | AWVS的url                                                                                                                                            |
| **url_list**   | textarea | `是` | 需要发起扫描的大量urls，以`,`分割，否则报错                                                                                                                           |
| **scan_label** | text     | `是` | AWVS发起扫描时，填写的描述，必填，用于区分扫描批次，默认是：AVWS API发起                                                                                                          |

**返回值：**

```
# 1 代表返回正常，"bf88763d-6deb-429d-8513-7f582559cc8e" 返回的是target_id，即：AVWS的任务id
{"status": 1 "result" {
        "targets": ["https://test.com", https://test2.com"],
        "targets_id": ["bf88763d-6deb-429d-8513-7f582559cc8e","bf88763d-6deb-429d-8513-7f582559cc82"]
        "suss_count": 2,
        "err_count: 0
    }
}
```

## 其他内容

使用的AWVS版本：

```shell
docker pull xrsec/awvs:v15

bash <(curl -sLk https://www.fahai.org/aDisk/Awvs/check.sh) xrsec/awvs:v15

访问地址：https://127.0.0.1:3443/#/login

账户：awvs@awvs.lan
密码：Awvs@awvs.lan
```