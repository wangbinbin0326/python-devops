#!/usr/bin/env python
#-*- coding:utf-8 -*-
#1, 实现域名的解析，获取域名所有的A记录，解析IP列表
#2，对IP列表进行HTTP级别的探测
import dns.resolver
import os
import httplib

iplist=[]
appdomain="pyapp.qa.webex.com"

def get_iplist(domain=""):    #域名解析函数，解析成功IP将被追加到iplist
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception, e:
        print "dns resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)  	 #追加到iplist
    return True

def checkip(ip):
	checkurl=ip+":80"
	getcontent=""
	httplib.socket.setdefaulttimeout(5)    #定义http连接超时时间5s
	conn=httplib.HTTPConnection(checkurl)    #创建http连接对象

	try:
		conn.request("GET", "/web02/index.html", headers = {"Host": appdomain})    #发起URL请求，添加host主机头
		r=conn.getresponse()
		getcontent = r.read(9)  #获取URL页面前15个字符，以便做可用性校验
	finally:
		if getcontent=="okokok!!!":    #监控URL页的内容一般是预先定义好的 health check，比如‘OKOKOK’
			print ip+" [OK]"
		else:
			print ip+" [Error]"

if __name__=="__main__":
	if get_iplist(appdomain) and len(iplist)>0:    #条件：域名解析正确且至少返回一个IP
	    for ip in iplist:
	    	checkip(ip)
	else:
		print "dns resolver error."

