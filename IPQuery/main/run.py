# !/usr/bin/env python
# encoding:utf-8
from loguru import logger  # 导入日记库，没有请先安装 pip install loguru


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def check_ip(ip):
    # 输出日记，生产环境会输出到指定目录
    logger.info("[Check_IP] 该 APP 执行参数为: {ip}", ip=ip)

    try:
        # 判断是否为局域网IP
        result = False
        if ip.startswith('10.'):
            result = True
        elif ip.startswith('172.'):
            if ip[7:11] in ('16', '17', '18', '19', '20'):
                result = True
        elif ip.startswith('192.'):
            if ip[6:8] == '16':
                result = True
        return {"status": 0, "result": result}

    except Exception as e:
        logger.error("[Check_IP] 查询检查失败:{e}", e=e)
        return {"status": 2, "result": "ip检查失败"}


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def ip_info(ip):
    # 输出日记，生产环境会输出到指定目录

    logger.info("[Check_IP] 该 APP 执行参数为: {ip}", ip=ip)
    try:
        import requests
    except Exception as e:
        logger.error("[IPQuery] 该APP[ip_info]功能，导入三方包出错，，报错信息：{info}", info=e)

    try:

        url = "http://api.webscan.cc/?action=getip&domain={ip}".format(ip=ip)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return {"status": 0, "result": response.json()}

    except Exception as e:
        logger.error("[IPQuery] 该APP[ip_info]功能，查询检查失败:{e}", e=e)
        return {"status": 2, "result": "ip检查失败"}


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def side_station(ip):
    # 输出日记，生产环境会输出到指定目录

    logger.info("[Check_IP] 该 APP 执行参数为: {ip}", ip=ip)
    try:
        import requests
    except Exception as e:
        logger.error("[IPQuery] 该APP[side_station]功能，导入三方包出错，，报错信息：{info}", info=e)

    try:

        url = "http://api.webscan.cc/?action=query&ip={ip}".format(ip=ip)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return {"status": 0, "result": response.json()}

    except Exception as e:
        logger.error("[IPQuery] 该APP[side_station]功能，查询检查失败:{e}", e=e)
        return {"status": 2, "result": "ip检查失败"}
