# coding=utf-8
import time
import urllib2

import math
from bson import ObjectId
from flask import render_template, request, json, url_for, session, redirect
from app import app, db_connect, sys_config
import flask_excel as excel

from app.get_ipinfo import get_ip_info

int_ip = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])
ip_int = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])

def get_ips(ip1,ip2):
    ip_range = []
    ip1_num = ip_int(ip1)
    ip2_num = ip_int(ip2)
    for i in range(ip1_num,ip2_num+1):
        ip_range.append(int_ip(i))
    print ip_range
    return ip_range

@app.route('/')
@app.route('/scanner/find', methods=['GET', 'POST'])
def find():
    """
    查询结果展示页面
    :return: 
    """
    currentPage = request.args.get('page', 1)
    currentPage = int(currentPage)
    condition = {}
    params = {}
    numPerPage = 10  # 每页显示100条
    pageNumShown = 10  # 最多显示10个页码

    if request.method == 'POST':
        params = request.form
        ip_range = request.form.get('ip_range', None)
        if ip_range and ip_range != '':
            condition['ip_range'] = ip_range

            # 分页
    if currentPage < 1:
        currentPage = 1

    offsetPage = (int(currentPage) - 1) * numPerPage
    model = db_connect.ip_info.find(condition)
    totalCount = model.count()
    page_num = int(math.ceil(totalCount / numPerPage))
    items = model.skip(offsetPage).limit(numPerPage)
    info = {"items": items, "totalCount": totalCount, "currentPage": currentPage, "numPerPage": numPerPage,
            "pageNumShown": pageNumShown,
            "params": params, "page_num": page_num}
    return render_template('find.html', info=info)

@app.route('/newScanTask', methods=['GET', 'POST'])
def newScanTask():
    """
    新增扫描任务页面
    """
    return render_template('newScanTask.html')

@app.route('/do_scan', methods=['POST'])
def do_scan():
    if request.method == 'POST':
        #ip1 = request.form['ip1']
        #ip2 = request.form['ip2']
        ip1 = request.form.get('ip1',None)
        ip2 = request.form.get('ip2',None)
        ip1_str = str(ip1)
        ip2_str = str(ip2)
        print ip1_str,ip2_str
        ip_list = get_ips(ip1_str,ip2_str)
        if len(ip_list) > 0:
            for ip in ip_list:
                get_ip_info(ip)
            result = {"status": 1, "msg": "任务加入成功"}
            return json.dumps(result)
        else:
            result = {"status": 0, "msg": "任务加入失败"}
            return json.dumps(result)

@app.route('/subDomainScan', methods=['GET', 'POST'])
def subDomainScan():
    if request.method == 'GET':
        return render_template('subDomainScan.html')
    elif request.method == 'POST':
        domain = request.form.get('domain',None)
        print domain
        return json.dumps(domain)