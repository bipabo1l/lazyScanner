#! /usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os

import re
import requests
from IPy import IP
from app import app, db_connect, sys_config

port_range = [80,8080,8088]

def get_IP():
    pass
    f = open("ip.txt", "r")
    ip_range = []
    for each in f:
        ips = IP(each)
        for x in ips:
            if str(x).endswith(".0"):
                pass
            else:
                ip_range.append(str(x))
    return ip_range

def get_ip_info(ip):
    for port in port_range:
        url = "http://" + ip + ":" + str(port)
        print url
        try:
            req = requests.get(url,timeout=3,allow_redirects=True)
            s = req.text
            code = req.status_code
            if code == 200 or code == 302:
                regex =  '<title>(.*)</title>'
                for m in re.findall(regex, s):
                    print m + str(port)
                    db_connect.ip_info.save({"url":url,"title":m})
                    continue
        except requests.exceptions.ConnectionError:
            pass


def main():
    ip_range = get_IP()
    print ip_range
    if len(ip_range) > 0:
        for ip in ip_range:
            print ip
            get_ip_info(ip)

if __name__ == '__main__':
    main()