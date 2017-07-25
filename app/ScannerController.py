# coding=utf-8
import time
import urllib2
from bson import ObjectId
from flask import render_template, request, json, url_for, session, redirect
from app import app, db_connect, sys_config
import flask_excel as excel


@app.route('/scanner/find', methods=['GET', 'POST'])
def find():
    """
    测试数据库查询
    :return: 
    """
    obj_id = request.args.get('object_id')
    print obj_id
    info = db_connect.ip_info.find_one({"_id": ObjectId(obj_id)})
    print info
    return render_template('find.html', info=info)