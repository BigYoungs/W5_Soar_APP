# !/usr/bin/env python
# encoding:utf-8
# 作者： BigYoung
# MyBlog： https://sec.bigyoung.cn
# 联系方式： Blog评论里留言
# 免责声明：禁止用于非法用途，一切违法行为与作者无关。

import json
import sys

# 导入日记库，没有请先安装 pip install loguru
import requests
from loguru import logger


def addTask(url, target, headers, scan_label):
    """
    AWVS添加任务
    :param url:
    :param target:
    :param headers:
    :param scan_label:
    :return:
    """
    try:
        url = ''.join((url, '/api/v1/targets/add'))
        data = {"targets": [{"address": target, "description": scan_label}], "groups": []}
        r = requests.post(url, headers=headers, data=json.dumps(data), timeout=30, verify=False)
        result = json.loads(r.content.decode())
        return {"status": 1, "target_id": result['targets'][0]['target_id'], "message": "success"}
    except Exception as e:
        logger.error(f"addTask异常，报错：{e}")
        return {"status": 0, "target_id": "", "message": e}


def scan(url, target, profile_id, scan_label, headers):
    """
    AWVS发起扫描
    :param url:
    :param target:
    :param profile_id:
    :param scan_label:
    :return:
    """
    scanUrl = ''.join((url, '/api/v1/scans'))
    task_result = addTask(url, target, headers, scan_label)
    if task_result["status"] == 1:
        target_id = task_result["target_id"]
        try:
            data = {"target_id": target_id, "profile_id": profile_id, "incremental": False,
                    "schedule": {"disable": False, "start_date": None, "time_sensitive": False}}
            response = requests.post(scanUrl, data=json.dumps(data), headers=headers, timeout=30, verify=False)
            result = json.loads(response.content)
            logger.info(f"AWVS 扫描任务：{target_id}, result：{response}")
            return {"status": 1, "target_id": result['target_id'], "res_json": result}
        except Exception as e:
            logger.error("目标：{0}，AWVS发起扫描异常，报错信息：{}".format(target, e))
            return {"status": 2, "result": f"AWVS发起扫描异常，报错信息:{e}"}
    else:
        return {"status": 2, "result": task_result}


async def scan_main(awvs_url, api_key, url_list, scan_type, scan_label):
    """

    :param awvs_url:  awvs的接口地址
    :param api_key:   awvs的认证token
    :param url_list:  需要发起扫描的urllist，最好带上https://
    :param scan_type: 1,2,3,4……12扫描模式
    :param scan_label: AWVS的扫描时填写的描述
    :return:
    """
    try:
        import requests, datetime, json, time
    except Exception as e:
        logger.error(
            "[{app_name}]该APP导入包失败，请先pip install 相关包，报错信息：{e}".format(
                app_name=sys._getframe().f_code.co_name, e=e))

    # 扫描模式
    mod_id = {
        "1": "11111111-1111-1111-1111-111111111111",  # 完全扫描
        "2": "11111111-1111-1111-1111-111111111112",  # 高风险漏洞
        "3": "11111111-1111-1111-1111-111111111116",  # XSS漏洞
        "4": "11111111-1111-1111-1111-111111111113",  # SQL注入漏洞
        "5": "11111111-1111-1111-1111-111111111115",  # 弱口令检测
        "6": "11111111-1111-1111-1111-111111111117",  # Crawl Only
        "7": "11111111-1111-1111-1111-111111111120",  # 恶意软件扫描
        "8": "11111111-1111-1111-1111-111111111120",  # 仅添加，这行不会生效
        "9": "apache-log4j",
        "10": "custom-Bounty",
        "11": "custom-cve",
        "12": "custom",
    }

    headers = {'Content-Type': 'application/json; charset=utf8', "X-Auth": api_key}
    add_count_suss = 0
    error_count = 0
    targets = url_list.split(',')
    targets_id = []

    # 消除提醒https访问没有证书的情况下的提醒：InsecureRequestWarning: Unverified HTTPS request
    requests.packages.urllib3.disable_warnings()

    for target in targets:
        if target:
            target = target.strip()
            # if '://' not in target and 'http' not in target:
            if 'http' not in target[0:7]:
                target = 'http://' + target

            target_state = scan(awvs_url, target, mod_id[scan_type], scan_label, headers)

            try:
                if target_state["status"] == 1:
                    add_count_suss = add_count_suss + 1
                    targets_id.append(target_state["target_id"])
                    logger.info(f"{target}已加入到扫描队列 ，第:{add_count_suss}个")
                else:
                    error_count = error_count + 1
                    logger.error(f"{target} 添加失败，第{error_count}个")
            except Exception as e:
                logger.error(f"域名：{target}，运行报错：{e}")
    return {"status": 1, "result": {
        "targets": targets,
        "targets_id": targets_id,
        "suss_count": add_count_suss,
        "err_count": error_count
    }}
