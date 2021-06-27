import urllib
import urllib.request
import re
import random
import time
import os
import pandas as pd
import json
import guesssp
import dataarrange
#import numpy
#抓取所需内容
user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
              'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']





def spider_score(gameid):
    stock_total = []
    for page in range(1, 2):
        url = 'http://vip.win007.com/AsianOdds_n.aspx?id=' + str(gameid) + '&l=0'  # gameid
        request = urllib.request.Request(url,
                                         headers={"User-Agent": random.choice(user_agent)})  # 随机从user_agent列表中抽取一个元素
        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:  # 异常检测
            print('page=', page, '', e.code)
        except urllib.error.URLError as e:
            print('page=', page, '', e.reason)
        #print(response)
        content = response.read().decode('utf-8')  # 读取网页内容

        #print(str(content))
        pattern = re.compile('<div class="vs"[\s\S]*')
        body = re.findall(pattern, str(content))
        #print(body[0])
        pattern = re.compile('(?<=<div class="score">).*(?=<)')
        data_page = re.findall(pattern, body[0])  # 正则匹配

        pattern = re.compile('\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
        date = re.findall(pattern, body[0])  # 正则匹配
        #print(date[0])
        list_data = [date[0]]
        #print(list_data)
        stock_total.extend(data_page)
        stock_total.extend(list_data)
        time.sleep(random.randrange(1, 2))  # 每抓一页随机休眠几秒，数值可根据实际情况改动
    stock_last = stock_total[:]
    #print(stock_last)
    return stock_last

def gamespiderAsia( gameid , betid):
    root = os.getcwd() # 获取当前路径
    stock_total=[]   #stock_total：所有页面的数据
    #gameid = 1910700
    for page in range(1,2):
        url = ['http://vip.win007.com/changeDetail/handicap.aspx?id=' + str(gameid) + '&companyid=8&l=0',
                  'http://vip.win007.com/changeDetail/handicap.aspx?id=' + str(gameid) + '&companyid=22&l=0',
                  'http://vip.win007.com/changeDetail/handicap.aspx?id=' + str(gameid) + '&companyid=1&l=0']
        request=urllib.request.Request(url=url[betid],headers={"User-Agent":random.choice(user_agent)})#随机从user_agent列表中抽取一个元素
        try:
            response=urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:            #异常检测
            print('page=',page,'',e.code)
        except urllib.error.URLError as e:
            print('page=',page,'',e.reason)
        content=response.read().decode('GBK')       #读取网页内容

        #print(content)
        #print('get page',page)                  #打印成功获取的页码
        pattern = re.compile('<span id="odds2">[\s\S]*')
        body = re.findall(pattern, str(content))
        #print(body)
        pattern = re.compile('(?<=>)([\u4E00-\u9FA5A-Za-z+\/+\:+\ (\-|\+)?\d+(\.\d+)?]+)(?=<)')
        data_page = re.findall(pattern, body[0])  # 正则匹配
        #print(data_page)
        stock_total.extend(data_page)
        time.sleep(random.randrange(1,2))        #每抓一页随机休眠几秒，数值可根据实际情况改动
    #删除空白字符
    stock_last=stock_total[:]  #stock_last为最终所要得到的数据

    num = stock_last.count("封")
    for i in range((int)(len(stock_last)+num*2)):
        if stock_last[i] == "封":
            stock_last.insert(i + 1,'-')
            stock_last.insert(i + 2,'-')

    num = stock_last.count("即")
    for i in range((int)(len(stock_last)+num*2)):
        if stock_last[i] == "即":
            stock_last.insert(i + 1,'-')
            stock_last.insert(i + 2,'-')
            i +=2
            i +=2

    num = stock_last.count("早")
    for i in range((int)(len(stock_last) + num * 2)):
        if stock_last[i] == "早":
            stock_last.insert(i + 1, '-')
            stock_last.insert(i + 2, '-')

    result = [] #result：最终数据
    # 转换成多维列表
    Hang = (int)(len(stock_last)/7)
    for y in range(0, Hang):
        for x in range(0, 7):
            if x == 0:
                result.append([])
            result[y].append(stock_last[x + y * 7])
    # 变化时间超过10分钟&&时间大于90，抓取完成。id放入donelist


    time_now = time.strftime("%Y%m%d%H%M", time.localtime())
    #print(gameid)
    #print(result)

    betstr = ['365bet', '10bet', 'aobet']
    df = pd.DataFrame(result)
    path = root + '\\' + 'data\\' + str(gameid) + 'Asia' + betstr[betid] + '.xlsx'
    df.to_excel(path, header=None)

    if len(result):
        # deadtime = result[1][5].replace("-","")
        # print(deadtime)
        # deadtime = deadtime.replace(" ", "")
        # print(deadtime)
        # deadtime = deadtime.replace(":", "")
        # print(deadtime)
        deadtime = result[1][5]
        #print(deadtime)
        if (deadtime != '-'):
            # print(deadtime)
            # if ((int)(deadtime) <= 10000000):
            #     deadtime = '20210' + deadtime
            # else:
            #     deadtime = '2021' + deadtime
            deadtime = '2021-' + deadtime
            # print(deadtime)
            deadtime_stamp = time.mktime(time.strptime(deadtime, "%Y-%m-%d %H:%M"))
            time_now_stamp = time.mktime(time.strptime(time_now, "%Y%m%d%H%M"))
            if (result[1][0] == '中场'):
                gametime = 45
            else:
                gametime = (int)(result[1][0])
            time_diff = (int)(time_now_stamp - deadtime_stamp)
            # print(gameid)
            # print(deadtime)
            # print(time_diff)
            if (((gametime >= 60) & (time_diff >= 2400))|((gametime >= 85) & (time_diff >= 600))):
                score = spider_score(gameid)
                guesssp.spider_done(gameid)
                # abc = (str)(result[1][1])
                Homescore = (int)(score[0])
                Guestscore = (int)(score[1])
                Date = score[2]
                # print('test')
                dataarrange.Singleupdata(Homescore, Guestscore, gameid, Date)

    return

def gamespiderEuro( gameid , betid):
    stock_total=[]   #stock_total：所有页面的数据
    #gameid = 1910700
    for page in range(1,2):
        url = ['http://vip.win007.com/changeDetail/1x2.aspx?id=' + str(gameid) + '&companyid=8&l=0',
               'http://vip.win007.com/changeDetail/1x2.aspx?id=' + str(gameid) + '&companyid=22&l=0',
               'http://vip.win007.com/changeDetail/1x2.aspx?id=' + str(gameid) + '&companyid=1&l=0']
        request=urllib.request.Request(url=url[betid],headers={"User-Agent":random.choice(user_agent)})#随机从user_agent列表中抽取一个元素
        try:
            response=urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:            #异常检测
            print('page=',page,'',e.code)
        except urllib.error.URLError as e:
            print('page=',page,'',e.reason)
        content=response.read().decode('GBK')       #读取网页内容

        #print(content)
        #print('get page',page)                  #打印成功获取的页码
        pattern = re.compile('<div id="out">[\s\S]*')
        body = re.findall(pattern, str(content))
        #print(body)
        pattern = re.compile('(?<=>)([\u4E00-\u9FA5A-Za-z+\/+\:+\ (\-|\+)?\d+(\.\d+)?]+)(?=<)')
        data_page = re.findall(pattern, body[0])  # 正则匹配
        #print(data_page)
        stock_total.extend(data_page)
        time.sleep(random.randrange(1,2))        #每抓一页随机休眠几秒，数值可根据实际情况改动
    #删除空白字符
    stock_last=stock_total[:]  #stock_last为最终所要得到的数据

    result = [] #result：最终数据
    # 转换成多维列表
    Hang = (int)(len(stock_last)/5)
    for y in range(0, Hang):
        for x in range(0, 5):
            if x == 0:
                result.append([])
            result[y].append(stock_last[x + y * 5])
    # 变化时间超过10分钟&&时间大于90，抓取完成。id放入donelist

    # time_now = time.strftime("%Y%m%d%H%M", time.localtime())
    # deadtime = result[1][3].replace("-", "")
    # deadtime = deadtime.replace(" ", "")
    # deadtime = deadtime.replace(":", "")
    # if (deadtime != ''):
    #     deadtime = '2020' + deadtime
    #     deadtime_stamp = time.mktime(time.strptime(deadtime, "%Y%m%d%H%M"))
    #     time_now_stamp = time.mktime(time.strptime(time_now, "%Y%m%d%H%M"))
    #     time_diff = (int)(time_now_stamp - deadtime_stamp)
    #     if ((time_diff >= 600)):
    #         guesssp.spider_done(gameid)

    # 获取当前路径
    root = os.getcwd()
    # print(time_now)

    df = pd.DataFrame(result)
    betstr = ['365bet', '10bet', 'aobet']
    path = root + '\\' + 'data\\' + str(gameid) + 'Euro' + betstr[betid] + '.xlsx'
    #print(df)
    df.to_excel(path, header=None)
    return

def gamespiderBS( gameid , betid):
    root = os.getcwd()
    stock_total=[]   #stock_total：所有页面的数据
    #gameid = 1910700
    for page in range(1,2):
        url = ['http://vip.win007.com/changeDetail/overunder.aspx?id=' + str(gameid) + '&companyid=8&l=0',
               'http://vip.win007.com/changeDetail/overunder.aspx?id=' + str(gameid) + '&companyid=22&l=0',
               'http://vip.win007.com/changeDetail/overunder.aspx?id=' + str(gameid) + '&companyid=1&l=0']
        request=urllib.request.Request(url=url[betid],headers={"User-Agent":random.choice(user_agent)})#随机从user_agent列表中抽取一个元素
        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:  # 异常检测
            print('page=', page, '', e.code)
        except urllib.error.URLError as e:
            print('page=', page, '', e.reason)
        content = response.read().decode('GBK')  # 读取网页内容  utf-8  GBK

        # print(content)
        # print('get page',page)                  #打印成功获取的页码
        pattern = re.compile('<span id="odds2">[\s\S]*')
        body = re.findall(pattern, str(content))
        # print(body)
        pattern = re.compile('(?<=>)([\u4E00-\u9FA5A-Za-z+\/+\:+\ (\-|\+)?\d+(\.\d+)?]+)(?=<)')
        data_page = re.findall(pattern, body[0])  # 正则匹配
        # print(data_page)
        stock_total.extend(data_page)
        time.sleep(random.randrange(1, 2))  # 每抓一页随机休眠几秒，数值可根据实际情况改动
    # 删除空白字符
    stock_last = stock_total[:]  # stock_last为最终所要得到的数据

    num = stock_last.count("封")
    for i in range((int)(len(stock_last) + num * 2)):
        if stock_last[i] == "封":
            stock_last.insert(i + 1, '-')
            stock_last.insert(i + 2, '-')

    num = stock_last.count("即")
    for i in range((int)(len(stock_last) + num * 2)):
        if stock_last[i] == "即":
            stock_last.insert(i + 1, '-')
            stock_last.insert(i + 2, '-')
            i += 2
            i += 2

    num = stock_last.count("早")
    for i in range((int)(len(stock_last) + num * 2)):
        if stock_last[i] == "早":
            stock_last.insert(i + 1, '-')
            stock_last.insert(i + 2, '-')

    result = []  # result：最终数据
    # 转换成多维列表
    Hang = (int)(len(stock_last) / 7)
    for y in range(0, Hang):
        for x in range(0, 7):
            if x == 0:
                result.append([])
            result[y].append(stock_last[x + y * 7])

    # time_now = time.strftime("%Y%m%d%H%M", time.localtime())
    # print(result[0][5])
    # print(result[1][5])
    #
    # deadtime = result[1][5].replace("-", "")
    # deadtime = deadtime.replace(" ", "")
    # deadtime = deadtime.replace(":", "")
    betstr = ['365bet', '10bet', 'aobet']
    df = pd.DataFrame(result)
    path = root + '\\' + 'data\\' + str(gameid) + 'BS' + betstr[betid] + '.xlsx'
    df.to_excel(path, header=None)
    return

def spider_determine(gameid):
    date = spider_score(gameid)
    if(len(date)==3):
        Homescore = date[0]
        Guestscore = date[1]
        Date = date[2]
    elif(len(date)==1):
        Date = date[0]
    #print(Date)
    time_now = time.strftime("%Y%m%d%H%M", time.localtime())
    time_now_stamp = time.mktime(time.strptime(time_now, "%Y%m%d%H%M"))
    starttime_stamp = time.mktime(time.strptime(Date, "%Y-%m-%d %H:%M"))
    time_diff = (int)(time_now_stamp - starttime_stamp)
    #print(time_diff)
    if(time_diff>=518400):
        guesssp.spider_done(gameid)
    if (time_diff > 7200):
        if (len(date) == 3):
            guesssp.spider_done(gameid)
            dataarrange.Singleupdata(Homescore, Guestscore, gameid, Date)
    if((time_diff>=-14400) & (time_diff<=2400)):
        gamespiderAsia(gameid, 0)
        gamespiderEuro(gameid, 0)
        gamespiderBS(gameid, 0)
        dataarrange.EuroandAsiaUpdata(gameid)
#spider_determine(1998672)
