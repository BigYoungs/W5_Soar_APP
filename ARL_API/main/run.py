# !/usr/bin/env python
# encoding:utf-8
# 作者： BigYoung
# MyBlog： https://sec.bigyoung.cn
# 联系方式： Blog评论里留言
# 免责声明：禁止用于非法用途，一切违法行为与作者无关。

import json
import sys
from urllib.parse import urlencode

import requests
# 导入日记库，没有请先安装 pip install loguru
from loguru import logger
from requests import request

requests.packages.urllib3.disable_warnings()


def get_req(token, url, kwargs, page=1, size=10):
    '''
    包装一下啊get请求
    :param token:
    :type token:
    :param url:
    :type url:
    :param kwargs:
    :type kwargs:
    :param page:
    :type page:
    :param size:
    :type size:
    :return:
    :rtype:
    '''
    para = clean_dict(kwargs)
    # 处理一下page和size参数
    if not page:
        page = 1
    if not size:
        size = 10
    headers = {
        'accept': 'application/json',
        'Token': token
    }
    # Get请求的URL参数拼接处理
    url = url + "?"
    if para:
        data = urlencode(kwargs)
        url = url + data + "&"
    url = url.replace("domain_brute", "options.domain_brute").replace("domain_brute_type",
                                                                      "options.domain_brute_type").replace(
        "port_scan_type", "options.port_scan_type").replace("port_scan", "options.port_scan").replace(
        "service_detection", "options.service_detection").replace("service_brute", "options.service_brute").replace(
        "os_detection", "options.os_detection").replace("site_identify", "options.site_identify").replace(
        "file_leak", "options.file_leak").replace("alt_dns", "options.alt_dns").replace("search_engines",
                                                                                        "options.search_engines").replace(
        "site_spider", "options.site_spider").replace("arl_search", "options.arl_search").replace("dns_query_plugin",
                                                                                                  "options.dns_query_plugin").replace(
        "skip_scan_cdn_ip", "options.skip_scan_cdn_ip").replace("nuclei_scan", "options.nuclei_scan").replace(
        "findvhost", "options.findvhost").replace("web_info_hunter", "options.web_info_hunter")
    print(url + f"page={page}&size={size}")
    res = request("GET", url + f"page={page}&size={size}", headers=headers, verify=False).json()
    return res


def get_url(url, parameters):
    """
    拼接url与所带参数
    :param url: {str} 链接
    :param parameters: {dict} 参数
    :return: {str} 拼接后的url
    """

    if parameters:
        data = urlencode(parameters)
        url + "?" + data + "&"
    return url + "?"


def clean_dict(dicts):
    '''
    删除dict的value为空的键值对
    :param dicts:
    :type dicts:
    :return:
    :rtype:
    '''
    for key in list(dicts.keys()):
        if not dicts.get(key):
            del dicts[key]

    if "host" in dicts.keys():
        del dicts["host"]
    if "token" in dicts.keys():
        del dicts["token"]
    if "size" in dicts.keys():
        del dicts["size"]
    if "all" in dicts.keys():
        del dicts["all"]
    if "page" in dicts.keys():
        del dicts["page"]
    return dicts


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def task_query(host, token, name=None, target=None, _id=None, status=None, task_tag=None, domain_brute=None,
                     domain_brute_type="", port_scan=None, port_scan_type=None, service_detection=None,
                     service_brute=None, os_detection=None, site_identify=None, file_leak=None, search_engines=None,
                     site_spider=None, arl_search=None, alt_dns=None, dns_query_plugin=None, skip_scan_cdn_ip=None,
                     nuclei_scan=None, findvhost=None, web_info_hunter=None, page=None, size=None, all=None):
    '''
    查询任务
    :param host:
    :type host:
    :param token:
    :type token:
    :param task_id:
    :type task_id:
    :param status:
    :type status:
    :param task_tag:
    :type task_tag:
    :param domain_brute:
    :type domain_brute:
    :param domain_brute_type:
    :type domain_brute_type:
    :param port_scan:
    :type port_scan:
    :param port_scan_type:
    :type port_scan_type:
    :param service_detection:
    :type service_detection:
    :param os_detection:
    :type os_detection:
    :param service_brute:
    :type service_brute:
    :param site_identify:
    :type site_identify:
    :param file_leak:
    :type file_leak:
    :param alt_dns:
    :type alt_dns:
    :param search_engines:
    :type search_engines:
    :param site_spider:
    :type site_spider:
    :param arl_search:
    :type arl_search:
    :param dns_query_plugin:
    :type dns_query_plugin:
    :param skip_scan_cdn_ip:
    :type skip_scan_cdn_ip:
    :param nuclei_scan:
    :type nuclei_scan:
    :param findvhost:
    :type findvhost:
    :param web_info_hunter:
    :type web_info_hunter:
    :param page:
    :type page:
    :param size:
    :type size:
    :param all:
    :type all: True # 是否返回全部的数据
    :return:
    :rtype:
    '''

    # 输出日记，生产环境会输出到指定目录
    logger.info(
        "[{app_name}]该APP执行参数为: {kwargs}".format(app_name=sys._getframe().f_code.co_name, kwargs=locals()))
    kwargs = locals()
    try:
        # 这里import 相关包
        import requests
        requests.packages.urllib3.disable_warnings()
    except Exception as e:
        logger.error(
            "[{app_name}]该APP导入包失败，请先pip install 相关包，报错信息：{e}".format(
                app_name=sys._getframe().f_code.co_name, e=e))

    try:
        # 这里写函数方法主体
        url = f"{host}/api/task/"
        response = get_req(token, url, kwargs=kwargs, page=page, size=size)
        if response["code"] == 200:
            result_list = response['items']
            page = response['page']
            size = response['size']
            total = response["total"]
            print(all)
            if all:
                while page * size < total:
                    page = page + 1
                    response = get_req(token, url, kwargs=kwargs, page=page, size=size)
                    result_list.append(response['items'])

            return {"status": 0, "result": {"result_info": result_list, "result_total": total}}
        else:
            return {"status": 1, "result": response}

    except Exception as e:
        return {"status": 2, "result": {
            "app_name": sys._getframe().f_code.co_name,
            "error_info": e
        }}


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def task_start(host, token, task_name, target, domain_brute=None, domain_brute_type="test", port_scan=None,
                     port_scan_type="test", service_detection=None, service_brute=None, os_detection=None,
                     site_identify=None, site_capture=None, file_leak=None, search_engines=None, site_spider=None,
                     arl_search=None, alt_dns=None, ssl_cert=None, dns_query_plugin=None, skip_scan_cdn_ip=None,
                     nuclei_scan=None, findvhost=None, web_info_hunter=None):
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
        pass
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

        response = request("POST", url, headers=headers, data=payload, verify=False).json()

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
        pass
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

        response = request("POST", url, headers=headers, data=payload, verify=False).json()

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
        pass
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
        response = request("GET", url, headers=headers, data=payload, verify=False).json()
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
async def get_wih(host, token, record_type=None, record_type__neq=None, record_type__not=None, content=None,
                  source=None, site=None, task_id=None, page=None, size=None, all=None):
    '''
    WEB Info Hunter 信息查询
    :param host:
    :type host:
    :param token:
    :type token:
    :param record_type:
    :type record_type:
    :param record_type__neq:
    :type record_type__neq:
    :param record_type__not:
    :type record_type__not:
    :param content:
    :type content:
    :param source:
    :type source:
    :param site:
    :type site:
    :param task_id:
    :type task_id:
    :param page:
    :type page:
    :param size:
    :type size:
    :param all:
    :type all:
    :return:
    :rtype:
    '''
    # 输出日记，生产环境会输出到指定目录
    logger.info(
        "[{app_name}]该APP执行参数为: {kwargs}".format(app_name=sys._getframe().f_code.co_name, kwargs=locals()))
    kwargs = locals()
    try:
        # 这里import 相关包
        import requests
        requests.packages.urllib3.disable_warnings()
    except Exception as e:
        logger.error("[{app_name}]该APP导入包失败，请先pip install 相关包，报错信息：{e}".format(
            app_name=sys._getframe().f_code.co_name, e=e))

    try:
        # 这里写函数方法主体
        url = f"{host}/api/wih/"
        response = get_req(token, url=url, kwargs=kwargs, page=page, size=size)
        if response["code"] == 200:
            result_list = response['items']
            page = response['page']
            size = response['size']
            total = response["total"]
            if all:
                while page * size < total:
                    page = page + 1
                    response = get_req(token, url, kwargs=kwargs, page=page, size=size)
                    result_list.append(response['items'])
            return {"status": 0, "result": {"result_info": result_list, "result_total": total}}
        else:
            return {"status": 1, "result": response}
    except Exception as e:
        return {"status": 2, "result": {
            "app_name": sys._getframe().f_code.co_name,
            "error_info": e
        }}
