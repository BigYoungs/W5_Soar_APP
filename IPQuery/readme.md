## APP 说明

> IP查询，支持以下功能：
>   - 查询IP是否为私有（局域网）IP，返回True、False
>   - 查询同IP**旁站**，返回旁站列表，支持ip、域名、网址
>   - 查询iP地址对应的地理位置信息，支持IP地址或者域名
> 
> 备注：旁站查询、ip地理信息，使用的是 https://www.webscan.cc/api/index.html 接口信息。

## 动作列表

### 1. 查询私有IP

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **ip**  | text | `是` | ip地址，支持IPv4，不支持IPv6 |

**返回值：**

```
True or Flase
```

### 2. 旁站查询

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **ip**  | text | `是` | ip地址，支持IPv4，不支持IPv6、域名、网址，如：https://baidu.com |

**返回值：**

```
说明：返回空值说明IP参数为填写,返回[] 值为该IP段暂无数据.

[
    {
        "domain": "dns.google.com",
        "title": "Google DNS"
    },
    {
        "domain": "dns.google",
        "title": ""
    }
]
```

### 3. 查询ip地理位置

**参数：**

|  参数   | 类型  |  必填   |  备注  |
|  ----  | ----  |  ----  |  ----  |
| **ip**  | text | `是` | domain或者ip地址 例如 www.google.com,8.8.8.8 |

**返回值：**

```
说明：返回字段ip为Error值时说明无法解析该域名或者IP地址.

{
"ip": "142.251.42.164",
"info": ""中国上海上海市电信"
}
```