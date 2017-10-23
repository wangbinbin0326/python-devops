#!/usr/bin/env python
import smtplib
import string

HOST = "smtp.gmail.com"    #定义smtp主机
SUBJECT = "Test email from Python" 
TO = "wang_bin_bin@hotmail.com"
FROM = "wang_bin_bin0326@gmail.com"
text = "Send the email by Python smtplib!!!"
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
    ), "\r\n")

server = smtplib.SMTP()    #创建一个SMTP()对象
server.connect(HOST, "25")    #通过connect方法连接smtp主机
server.starttls()    #启动安全传输模式
server.login("wang_bin_bin0326@gmail.com","CCM%lab123")    #邮箱账号登陆校验
server.sendmail(FROM, [TO], BODY)    #邮件发送
server.quit()    #断开smtp连接