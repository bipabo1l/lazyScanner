#! /usr/bin/python
# -*- coding: utf-8 -*-
import optparse
import os
from IPy import IP

def main():
    pass
    f = open("ip.txt","r")
    ip_range = []
    for each in f:
        print each
        ips = IP(each)
        for X in ips:
            if X.endswith(".0"):
                pass
            else:
                print X



if __name__ == '__main__':
    parser = optparse.OptionParser("Usage: %prog [options] target")
    parser.add_option("-t", "--target", dest="TARGET", help="write single target")
    parser.add_option("-f", "--file", dest="FILE", help="write the file of ip")
    (options, args) = parser.parse_args()  # args获取默认命令的值
    ip = options.TARGET  # 获取target值
    file = options.FILE  # 获取文件名
    main()