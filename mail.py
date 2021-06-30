#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart


my_sender = 'huozhihuiyi@126.com'  # 发件人邮箱账号
my_pass = 'WAVPQHXGLGUAYZXC'  # 发件人邮箱密码
my_user = '641678112@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail(data,time,state):
    ret = True
    try:

        message = MIMEMultipart()
        message['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = time  # 邮件的主题，也可以说是标题

        # 邮件正文内容
        if state == 1:
            message.attach(MIMEText(data, 'HTML', 'utf-8'))
        elif state == 2:
        # 构造附件1，传送当前目录下的 test.txt 文件
            att1 = MIMEText(open((str)(data), 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="1.xlsx"'
            message.attach(att1)


        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
