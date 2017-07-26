# coding=utf-8
import time
import urllib2
from bson import ObjectId
from flask import render_template, request, json, url_for, session, redirect
from app import app, db_connect, sys_config
import flask_excel as excel

@app.route('/')
@app.route('/scanner/find', methods=['GET', 'POST'])
def find():
    """
    查询结果展示页面
    :return: 
    """
    condition = {}
    info = db_connect.ip_info.find(condition)
    print info
    return render_template('find.html', info=info)

@app.route('/newScanTask', methods=['GET', 'POST'])
def newScanTask():
    """
    新增扫描任务页面
    """
    return render_template('newScanTask.html')
