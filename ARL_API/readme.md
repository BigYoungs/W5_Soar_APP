## 【ARL API】APP使用说明

> **作者：** BigYoung
>
> **MyBlog：** https://sec.bigyoung.cn
>
> **联系方式：** Blog评论里留言
>
> **免责声明：** 禁止用于非法用途，一切违法行为与作者无关。

## 使用要求

1. 熟练使用ARL的功能后，再使用，否则极容易发生不符合预期的情况
2. 请使用对应功能时，先在ARL的在线API功能上测试好后，再使用此app功能，否则极易发生不符合预期的情况

## 动作列表

### 1. task_query

**动作名：**

任务查询

**动作描述：**

通过ARL API发起任务查询，此功能跟ARL 在线API接口的“任务查询”功能一样

查询任务详情

**参数：**

| 参数                    | 类型     | 必填  | 备注                                                   |
|-----------------------|--------|-----|------------------------------------------------------|
| **host**              | text   | `是` | ARL的地址，如：https:192.168.1.1:5003                      |
| **token**             | text   | `是` | ARL API调用的Token，需要在配置文件中配置                           |
| **name**              | text   | `否` | ARL 发起的任务名字                                          |
| **target**            | text   | `否` | ARL 发起的任务的目标                                         |
| **_id**               | text   | `否` | ARL 根据task_id查询任务详情                                  |
| **domain_brute**      | select | `否` | 是否开启【域名爆破】，选择：True 或 False                           |
| **domain_brute_type** | select | `否` | 域名爆破类型：test：测试，big：大字典                               |
| **port_scan**         | select | `否` | 是否开启【端口扫描】，选择：True 或 False                           |
| **port_scan_type**    | select | `否` | 端口扫描类型：test：测试，top100：TOP100，top100: TOP1000，all：全端口 |
| **service_detection** | select | `否` | 是否开启【？？？这个服务也不知道是干嘛的】，选择：True 或 False                |
| **os_detection**      | select | `否` | 是否开启【操作系统识别】，选择：True 或 False                         |
| **site_identify**     | select | `否` | 是否开启【站点识别】，选择：True 或 False                           |
| **site_capture**      | select | `否` | 是否开启【站点截图】，选择：True 或 False                           |
| **file_leak**         | select | `否` | 是否开启【文件泄露】，选择：True 或 False                           |
| **search_engines**    | select | `否` | 是否开启【搜索引擎调用】，选择：True 或 False                         |
| **site_spider**       | select | `否` | 是否开启【站点爬虫】，选择：True 或 False                           |
| **arl_search**        | select | `否` | 是否开启【ARL历史查询】，选择：True 或 False                        |
| **alt_dns**           | select | `否` | 是否开启【DNS字典智能生成】，选择：True 或 False                      |
| **ssl_cert**          | select | `否` | 是否开启【ssl证书获取】，选择：True 或 False                        |
| **dns_query_plugin**  | select | `否` | 是否开启【域名查询插件】，选择：True 或 False                         |
| **skip_scan_cdn_ip**  | select | `否` | 是否开启【跳过CDN】，选择：True 或 False                          |
| **nuclei_scan**       | select | `否` | 是否开启【Nuclei调用】，选择：True 或 False                       |
| **findvhost**         | select | `否` | 是否开启【Host碰撞】，选择：True 或 False                         |
| **web_info_hunter**   | select | `否` | 是否开启【WIH调用】，选择：True 或 False                          |
| **page**              | text   | `否` | 分页查询页码                                               |
| **size**              | text   | `否` | 分页查询数据量                                              |
| **all**               | select | `否` | 是否返回所有数据，选择：True 或 False                             |

**返回值：**

> **提示：**
>
> result_info里的数据是ARL 在线接口返回数据的iterm内容。
>
> result_total是搜索条件的所有数据，在线接口返回数据的total字段那内容。

```json

{
  "status": 0,
  "result": {
    "result_info": [
      {
        '_id': '653f568f076f30d7973b6d2a',
        'name': '监控-test-test.cn',
        'target': 'test.cn',
        'start_time': '2023-10-30 15:09:03',
        'status': 'done',
        'type': 'domain',
        'task_tag': 'monitor',
        'options': {
          'domain_brute': False,
          'domain_brute_type': 'big',
          'alt_dns': True,
          'arl_search': True,
          'port_scan_type': 'test',
          'port_scan': False,
          'service_detection': True,
          'service_brute': False,
          'os_detection': True,
          'site_identify': False,
          'site_capture': False,
          'file_leak': False,
          'site_spider': False,
          'search_engines': False,
          'ssl_cert': True,
          'fofa_search': False,
          'dns_query_plugin': True,
          'web_info_hunter': False,
          'scope_id': '6481c0c4f2642294c5c8f',
          'policy_name': '子域名收集',
          'related_scope_id': '',
          'skip_scan_cdn_ip': True,
          'port_custom': '',
          'host_timeout_type': 'default',
          'host_timeout': 0,
          'port_parallelism': 5,
          'port_min_rate': 9,
          'nuclei_scan': False,
          'npoc_service_detection': True,
          'poc_config': [],
          'brute_config': []
        },
        'celery_id': 'ad715055-d570-4e2a-825a-f156de07687d',
        'service': [
          {
            'name': 'dns_query_plugin',
            'elapsed': 86.98
          },
          {
            'name': 'arl_search',
            'elapsed': 0.99
          },
          {
            'name': 'alt_dns',
            'elapsed': 643.06
          },
          {
            'name': 'ssl_cert',
            'elapsed': 0.0
          },
          {
            'name': 'find_site',
            'elapsed': 0.0
          },
          {
            'name': 'fetch_site',
            'elapsed': 0.03
          }
        ],
        'statistic': {
          'site_cnt': 0,
          'domain_cnt': 0,
          'ip_cnt': 0,
          'cert_cnt': 0,
          'service_cnt': 0,
          'fileleak_cnt': 0,
          'url_cnt': 0,
          'vuln_cnt': 0,
          'npoc_service_cnt': 0,
          'cip_cnt': 0,
          'nuclei_result_cnt': 0,
          'stat_finger_cnt': 0,
          'wih_cnt': 0
        },
        'end_time': '2023-10-30 15:22:09',
        'sync_status': 'default'
      }
      …
    ],
    "result_total": 958
  }
}
```

### 2. task_start

**动作名：**

发起任务

**动作描述：**

通过ARL API发起任务，此功能跟ARL“任务管理”页面的添加任务功能一样

**参数：**

| 参数                    | 类型     | 必填  | 备注                                                   |
|-----------------------|--------|-----|------------------------------------------------------|
| **host**              | text   | `是` | ARL的地址，如：https:192.168.1.1:5003                      |
| **token**             | text   | `是` | ARL API调用的Token，需要在配置文件中配置                           |
| **task_name**         | text   | `是` | ARL 发起的任务名字                                          |
| **target**            | text   | `是` | ARL 发起的任务的目标，目标为域名、ip，域名不要带http:// https://          |
| **domain_brute**      | select | `否` | 是否开启【域名爆破】，选择：True 或 False                           |
| **domain_brute_type** | select | `否` | 域名爆破类型：test：测试，big：大字典                               |
| **port_scan**         | select | `否` | 是否开启【端口扫描】，选择：True 或 False                           |
| **port_scan_type**    | select | `否` | 端口扫描类型：test：测试，top100：TOP100，top100: TOP1000，all：全端口 |
| **service_detection** | select | `否` | 是否开启【？？？这个服务也不知道是干嘛的】，选择：True 或 False                |
| **os_detection**      | select | `否` | 是否开启【操作系统识别】，选择：True 或 False                         |
| **site_identify**     | select | `否` | 是否开启【站点识别】，选择：True 或 False                           |
| **site_capture**      | select | `否` | 是否开启【站点截图】，选择：True 或 False                           |
| **file_leak**         | select | `否` | 是否开启【文件泄露】，选择：True 或 False                           |
| **search_engines**    | select | `否` | 是否开启【搜索引擎调用】，选择：True 或 False                         |
| **site_spider**       | select | `否` | 是否开启【站点爬虫】，选择：True 或 False                           |
| **arl_search**        | select | `否` | 是否开启【ARL历史查询】，选择：True 或 False                        |
| **alt_dns**           | select | `否` | 是否开启【DNS字典智能生成】，选择：True 或 False                      |
| **ssl_cert**          | select | `否` | 是否开启【ssl证书获取】，选择：True 或 False                        |
| **dns_query_plugin**  | select | `否` | 是否开启【域名查询插件】，选择：True 或 False                         |
| **skip_scan_cdn_ip**  | select | `否` | 是否开启【跳过CDN】，选择：True 或 False                          |
| **nuclei_scan**       | select | `否` | 是否开启【Nuclei调用】，选择：True 或 False                       |
| **findvhost**         | select | `否` | 是否开启【Host碰撞】，选择：True 或 False                         |
| **web_info_hunter**   | select | `否` | 是否开启【WIH调用】，选择：True 或 False                          |

**返回值：**

```json
{
  'status': 0,
  'result': [
    {
      'name': 'test',
      'target': 'baidu.com',
      'start_time': '-',
      'status': 'waiting',
      'type': 'domain',
      'task_tag': 'task',
      'options': {
        'domain_brute': False,
        'domain_brute_type': 'test',
        'port_scan_type': 'test',
        'port_scan': False,
        'service_detection': False,
        'service_brute': False,
        'os_detection': False,
        'site_identify': False,
        'site_capture': False,
        'file_leak': False,
        'search_engines': False,
        'site_spider': False,
        'arl_search': False,
        'alt_dns': False,
        'ssl_cert': False,
        'dns_query_plugin': False,
        'skip_scan_cdn_ip': False,
        'nuclei_scan': False,
        'findvhost': False,
        'web_info_hunter': False
      },
      'end_time': '-',
      'service': [],
      'celery_id': '6022cac9-4cfb-4451-aa33-e42b8dc5d560',
      'task_id': '6539044129d4b4808f626369'
    }
  ]
}
```

### 3. task_sync

**动作名：**

将任务结果同步到资产组

**动作描述：**

把task_id对应的资产同步到scope_id的资产分组里

**参数：**

| 参数           | 类型   | 必填  | 备注                              |
|--------------|------|-----|---------------------------------|
| **host**     | text | `是` | ARL的地址，如：https:192.168.1.1:5003 |
| **token**    | text | `是` | ARL API调用的Token，需要在配置文件中配置      |
| **task_id**  | text | `是` | 任务id                            |
| **scope_id** | text | `是` | scope_id 资产id                   |

**返回值：**

```json
# 任务创建成功
{
'status': 0,
'result': {
"task_id": "652e8a3b9aed7884f101297b"
}
}

# 任务已经存在，staus的值是 1
{
'status': 1,
'result': {
'message': '任务资产同步处理中',
'code': 801,
'data': {
'task_id': '652e8a3b9aed7884f101297b'
}
}
}
```

### 4. poc_sync

**动作名：**

更新Poc信息

**动作描述：**

触发Poc更新功能

**参数：**

| 参数        | 类型   | 必填  | 备注                              |
|-----------|------|-----|---------------------------------|
| **host**  | text | `是` | ARL的地址，如：https:192.168.1.1:5003 |
| **token** | text | `是` | ARL API调用的Token，需要在配置文件中配置      |

**返回值：**

```json
{
  'status': 0,
  'result': {
    'plugin_cnt': 67
  }
}
```

### 5. get_wih

**动作名：**

查询敏感信息

**动作描述：**

WEB Info Hunter 敏感信息查询

**参数：**

| 参数                   | 类型     | 必填  | 备注                              |
|----------------------|--------|-----|---------------------------------|
| **host**             | text   | `是` | ARL的地址，如：https:192.168.1.1:5003 |
| **token**            | text   | `是` | ARL API调用的Token，需要在配置文件中配置      |
| **record_type**      | text   | `否` | 记录类型                            |
| **record_type__neq** | text   | `否` | 记录类型不等于（全匹配）                    |
| **record_type__not** | text   | `否` | 记录类型不包含                         |
| **content**          | text   | `否` | 内容                              |
| **source**           | text   | `否` | 来源 JS URL                       |
| **site**             | text   | `否` | 站点URL                           |
| **task_id**          | text   | `否` | 任务ID                            |
| **page**             | text   | `否` | 分页查询页码                          |
| **size**             | text   | `否` | 分页查询数据量                         |
| **all**              | select | `否` | 是否返回所有数据，选择：True 或 False        |

**返回值：**
> **提示：**
>
> result_info里的数据是ARL 在线接口返回数据的iterm内容。
>
> result_total是搜索条件的所有数据，在线接口返回数据的total字段那内容。

```json
{
  "status": 0,
  "result": {
    'result_info': [
      {
        '_id': '654321053674c08d2ab5fd29',
        'record_type': 'password',
        'content': 'FORGET_PASSWORD:"forget"',
        'site': 'https://test.com',
        'source': 'https://test.com/public/js/vendor.cc5a825.js',
        'fnv_hash': '12574789310169570990',
        'task_id': '654317c89a3f3d194e65bf53'
      },
      {
        '_id': '654321053674c08d2ab5fce0',
        'record_type': 'password',
        'content': 'Change_password:"Change"',
        'site': 'https://test.com',
        'source': 'https://test.com/app.js',
        'fnv_hash': '3581941523742694988',
        'task_id': '654317c89a3f3d194e65bf53'
      },
      {
        '_id': '654321053674c08d2ab5fc2b',
        'record_type': 'password',
        'content': 'againNewPassword:"Confirm"',
        'site': 'https://test.com',
        'source': 'https://ctest.com/app.js',
        'fnv_hash': '18288388580908371',
        'task_id': '654317c89a3f3d194e65bf53'
      },
      {
        '_id': '654321043674c08d2ab5f65e',
        'record_type': 'password',
        'content': 'FORGET_PASSWORD:"forgetPassword"',
        'site': 'https://test.com',
        'source': 'https://test.com/public/js/vendor.cc5a825.js',
        'fnv_hash': '7688182886446109769',
        'task_id': '654317c89a3f3d194e65bf53'
      },
      {
        '_id': '654321033674c08d2ab5efca',
        'record_type': 'password',
        'content': 'monitorPassword:"sssssss"',
        'site': 'https://test.com',
        'source': 'https://test.com/public/js/main.1f7d395.js',
        'fnv_hash': '657975459136915897',
        'task_id': '654317c89a3f3d194e65bf53'
      },
      {
        '_id': '654321033674c08d2ab5ef6a',
        'record_type': 'password',
        'content': 'password:"ssssssss"',
        'site': 'https://test.com',
        'source': 'https://test.com/static/js/main.48337977.chunk.js',
        'fnv_hash': '7178680373892925726',
        'task_id': '654317c89a3f3d194e65bf53'
      },
      {
        '_id': '654321023674c08d2ab5ea48',
        'record_type': 'password',
        'content': 'loginPassword:"Wwwwww"',
        'site': 'https://test.com',
        'source': 'https://test.com/public/js/main.1f7d395.js',
        'fnv_hash': '6007363605616763182',
        'task_id': '654317c89a3f3d194e65bf53'
      },
      {
        '_id': '65421539076f30d7973b7317',
        'record_type': 'password',
        'content': 'password":"ssssss"',
        'site': 'https://test.com',
        'source': 'https://test.com/static/js/2.c2f5eb94.chunk.js',
        'fnv_hash': '7895490485063149250',
        'task_id': '65420487b016aa4d4535ae5d'
      },
      {
        '_id': '6540b54f732ef1ca543b9554',
        'record_type': 'password',
        'content': 'monitorPassword:"aaaaaaaa"',
        'site': 'https://test.com',
        'source': 'https://test.com/eva-new/public/js/main.1f7d395.js',
        'fnv_hash': '657975459136915897',
        'task_id': '6540b230b016aa4d4535ae5a'
      },
      {
        '_id': '6540b54f732ef1ca543b9553',
        'record_type': 'password',
        'content': 'loginPassword:"xxxxxxx"',
        'site': 'https://test.com',
        'source': 'https://test.com/public/js/main.1f7d395.js',
        'fnv_hash': '6007363605616763182',
        'task_id': '6540b230b016aa4d4535ae5a'
      }
    ],
    'result_total': 17
  }
}
```