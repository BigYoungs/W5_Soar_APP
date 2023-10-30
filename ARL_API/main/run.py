# !/usr/bin/env python
# encoding:utf-8
# 作者： BigYoung
# MyBlog： https://sec.bigyoung.cn
# 联系方式： Blog评论里留言
# 免责声明：禁止用于非法用途，一切违法行为与作者无关。

import sys

# 导入日记库，没有请先安装 pip install loguru
from loguru import logger


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def task_query(host, token, task_id):
    '''
    任务信息查询
    :param host:
    :param token:
    :param task_id:
    :return:
    '''
    # 输出日记，生产环境会输出到指定目录
    logger.info(
        "[{app_name}]该APP执行参数为: {kwargs}".format(app_name=sys._getframe().f_code.co_name, kwargs=locals()))
    try:
        # 这里import 相关包
        import requests
    except Exception as e:
        logger.error(
            "[{app_name}]该APP导入包失败，请先pip install 相关包，报错信息：{e}".format(
                app_name=sys._getframe().f_code.co_name, e=e))

    try:
        # 这里写函数方法主体
        url = f"{host}/api/task/?_id={task_id}"

        payload = {}
        headers = {
            'accept': 'application/json',
            'Token': token
        }

        response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

        if response["code"] == 200:
            return {"status": 0, "result": response["items"]}
        else:
            return {"status": 1, "result": response}

    except Exception as e:
        return {"status": 2, "result": {
            "app_name": sys._getframe().f_code.co_name,
            "error_info": e
        }}


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def task_start(host, token, task_name, target, domain_brute=False, domain_brute_type="test", port_scan=False,
                     port_scan_type="test",
                     service_detection=False, service_brute=False, os_detection=False, site_identify=False,
                     site_capture=False, file_leak=False,
                     search_engines=False, site_spider=False, arl_search=False, alt_dns=False, ssl_cert=False,
                     dns_query_plugin=False,
                     skip_scan_cdn_ip=False, nuclei_scan=False, findvhost=False, web_info_hunter=False):
    '''
    任务提交，此功能跟ARL“任务管理”页面的添加任务功能一样
    :param host:  # ARL的地址
    :param token: # ARL API调用的Token
    "name": "task name", # ARL 任务名字
    "target": "www.nicemiss.cn", # 任务目标，支持IP、ip段、域名
    "domain_brute": true, # 是否开启域名爆破
    "domain_brute_type": "test", # 域名爆破类型，测试：test，大字典：big
    "port_scan_type": "test", # 端口扫描类型，测试：test，TOP100：top100，TOP1000：top1000，全端口：all
    "port_scan": true, # 是否开启端口扫描
    "service_detection": false, # 是否开启服务识别
    "service_brute": false, # 是否？？？
    "os_detection": false,  # 是否开始操作系统识别
    "site_identify": false, # 是否开启站点识别
    "site_capture": false,  # 是否开启站点截图
    "file_leak": false,     # 是否开启泄露
    "search_engines": false,    # 是否开启搜索引擎调用
    "site_spider": false,       # 是否开启站点爬虫
    "arl_search": false,        # 是否开启ARL历史查询
    "alt_dns": false,           # 是否开启 ？？？
    "ssl_cert": false,          # 是否开启ssl证书获取
    "dns_query_plugin": false,  # 是否开启 域名查询插件
    "skip_scan_cdn_ip": false,  # 是否开启跳过CDN
    "nuclei_scan": false,       # 是否开启调用Nuclei
    "findvhost": false,         # 是否开启Host碰撞
    "web_info_hunter": true     # 是否开启WIH调用
    :return:{
              "code": 200,
              "message": "success",
              "items": [
                {
                  "name": "task name",
                  "target": "www.test.cn",
                  "start_time": "-",
                  "status": "waiting",
                  "type": "domain",
                  "task_tag": "task",
                  "options": {
                    "domain_brute": true,
                    "domain_brute_type": "test",
                    "port_scan_type": "test",
                    "port_scan": true,
                    "service_detection": false,
                    "service_brute": false,
                    "os_detection": false,
                    "site_identify": false,
                    "site_capture": false,
                    "file_leak": false,
                    "search_engines": false,
                    "site_spider": false,
                    "arl_search": false,
                    "alt_dns": false,
                    "ssl_cert": false,
                    "dns_query_plugin": false,
                    "skip_scan_cdn_ip": false,
                    "nuclei_scan": false,
                    "findvhost": false,
                    "web_info_hunter": true
                  },
                  "end_time": "-",
                  "service": [],
                  "celery_id": "33e885cf-e831-45ec-b2f5-8eb6c9a17acf",
                  "task_id": "6538acf9f5954d593059186d"
                }
              ]
            }
    '''
    # 输出日记，生产环境会输出到指定目录
    logger.info(
        "[{app_name}]该APP执行参数为: {kwargs}".format(app_name=sys._getframe().f_code.co_name, kwargs=locals()))
    try:
        # 这里import 相关包
        import requests
        import json
    except Exception as e:
        logger.error(
            "[{app_name}]该APP导入包失败，请先pip install 相关包，报错信息：{e}".format(
                app_name=sys._getframe().f_code.co_name, e=e))

    try:
        # 这里写函数方法主体
        url = f"{host}/api/task/"

        payload = json.dumps({
            "name": task_name,
            "target": target,
            "domain_brute": domain_brute,
            "domain_brute_type": domain_brute_type,
            "port_scan_type": port_scan_type,
            "port_scan": port_scan,
            "service_detection": service_detection,
            "service_brute": service_brute,
            "os_detection": os_detection,
            "site_identify": site_identify,
            "site_capture": site_capture,
            "file_leak": file_leak,
            "search_engines": search_engines,
            "site_spider": site_spider,
            "arl_search": arl_search,
            "alt_dns": alt_dns,
            "ssl_cert": ssl_cert,
            "dns_query_plugin": dns_query_plugin,
            "skip_scan_cdn_ip": skip_scan_cdn_ip,
            "nuclei_scan": nuclei_scan,
            "findvhost": findvhost,
            "web_info_hunter": web_info_hunter
        })
        headers = {
            'accept': 'application/json',
            'Token': token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()

        if response["code"] == 200:
            return {"status": 0, "result": response["items"]}
        else:
            return {"status": 1, "result": response}

    except Exception as e:
        return {"status": 2, "result": {
            "app_name": sys._getframe().f_code.co_name,
            "error_info": e
        }}


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def task_sync(host, token, task_id, scop_id):
    '''
    将任务结果同步到资产组
    :param host:
    :param token:
    :param task_id: 任务的ID
    :param scop_id: 资产组的ID
    :return:
    '''
    # 输出日记，生产环境会输出到指定目录
    logger.info(
        "[{app_name}]该APP执行参数为: {kwargs}".format(app_name=sys._getframe().f_code.co_name, kwargs=locals()))
    try:
        # 这里import 相关包
        import requests
        import json
    except Exception as e:
        logger.error(
            "[{app_name}]该APP导入包失败，请先pip install 相关包，报错信息：{e}".format(
                app_name=sys._getframe().f_code.co_name, e=e))

    try:
        # 这里写函数方法主体
        url = "{host}/api/task/sync/".format(host=host)
        payload = json.dumps({
            "task_id": task_id,
            "scope_id": scop_id
        })
        headers = {
            'accept': 'application/json',
            'Token': token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()

        if response["code"] == 200:
            return {"status": 0, "result": response["data"]}
        else:
            return {"status": 1, "result": response}

    except Exception as e:
        return {"status": 2, "result": {
            "app_name": sys._getframe().f_code.co_name,
            "error_info": e
        }}


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def poc_sync(host, token):
    '''
    更新POC信息
    :param host:
    :param token:
    :return:
    '''
    # 输出日记，生产环境会输出到指定目录
    logger.info(
        "[{app_name}]该APP执行参数为: {kwargs}".format(app_name=sys._getframe().f_code.co_name, kwargs=locals()))
    try:
        # 这里import 相关包
        import requests
    except Exception as e:
        logger.error(
            "[{app_name}]该APP导入包失败，请先pip install 相关包，报错信息：{e}".format(
                app_name=sys._getframe().f_code.co_name, e=e))

    try:
        # 这里写函数方法主体
        url = f"{host}/api/poc/sync/"
        payload = {}
        headers = {
            'accept': 'application/json',
            'Token': token
        }
        response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()
        if response["code"] == 200:
            return {"status": 0, "result": response["data"]}
        else:
            return {"status": 1, "result": response}

    except Exception as e:
        return {"status": 2, "result": {
            "app_name": sys._getframe().f_code.co_name,
            "error_info": e
        }}
