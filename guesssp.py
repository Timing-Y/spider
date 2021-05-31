import urllib
import urllib.request
import re
import random
import time
import os
import pandas as pd
import numpy as np
import dataarrange
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
#stock_total=[]   #stock_total：所有页面的数据

def spider(  ):
    stock_total = [] #stock_total：所有页面的数据
    for page in range(1,2):
        #url='http://quote.stockstar.com/stock/ranklist_a_3_1_'+str(page)+'.html'
        url = 'http://guess2.win007.com/'
        #url = 'https://wenzi.zhibo8.cc/zhibo/nba/2018/1211131079.htm'
        #url = 'http://www.taobao.com/'
        request=urllib.request.Request(url=url,headers={"User-Agent":random.choice(user_agent)})#随机从user_agent列表中抽取一个元素
        try:
            response=urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:            #异常检测
            print('page=',page,'',e.code)
        except urllib.error.URLError as e:
            print('page=',page,'',e.reason)
        content=response.read().decode('UTF-8')       #读取网页内容
        #print(content)
        #print('get page',page)                  #打印成功获取的页码
        pattern = re.compile('<div class="match"[\s\S]* <h2 class="r_tit_bt"')
        body = re.findall(pattern, str(content))
        pattern = re.compile('(?<=>)[\u4E00-\u9FA5A-Za-z+\/(\-|\+)?\d+(\.\d+)?]+(?=<)|(?<=home_)[0-9]*|\d{2}-\d{2} \d{2}:\d{2}')
        #print(body)
        data_page = re.findall(pattern, body[0])  # 正则匹配
        pattern = re.compile('(?<=home_)([0-9]*)')
        game_id = re.findall(pattern, body[0])  # 正则匹配
        #print(data_page)
        #print(game_id)
        stock_total.extend(data_page)
        time.sleep(random.randrange(1,2))        #每抓一页随机休眠几秒，数值可根据实际情况改动
    #删除空白字符
    #print(stock_total)
    stock_last=stock_total[:]  #stock_last为最终所要得到的数据
    #print(stock_last)
    #print(len(stock_last)/9)
    num = stock_last.count("未")
    for i in range((int)(len(stock_last)+num*3)):
        if stock_last[i] == "未":
            stock_last.insert(i+1,'0')
            stock_last.insert(i+2,'-')
            stock_last.insert(i+3,'0')
    num = stock_last.count("推迟")
    for i in range((int)(len(stock_last) + num * 3)):
        if stock_last[i] == "推迟":
            stock_last.insert(i + 1, '0')
            stock_last.insert(i + 2, '-')
            stock_last.insert(i + 3, '0')
    #print(len(stock_last))
    result = [] #result：最终数据
    Hang = (int)(len(stock_last)/29)
    # 转换成多维列表
    for y in range(0, Hang):
        for x in range(0, 29):
            if x == 0:
                result.append([])
            result[y].append(stock_last[x + y * 29])

    time_now = time.strftime("%Y%m%d", time.localtime())
    #获取当前路径
    root = os.getcwd()
    path = root + '\\' + time_now + '.xlsx'
    df = pd.DataFrame(result)
    df[1] = ['2021-%s' % i for i in df[1]]
    #print(df)
    df = df.drop([6, 27, 28, 24, 25, 26], axis=1)
    #print(df)
    dataarrange.dar(df)
    #df.to_excel(path, header = None, index = None)
    return game_id

def arrange( newid ):
    newid_t = []
    for i in newid:
        newid_t.append(int(i))
    # newid = newid_t
    root = os.getcwd()
    path_wait = root + '\\' + 'wait' + '.xlsx'
    path_done = root + '\\' + 'done' + '.xlsx'
    wait_sp = pd.read_excel(path_wait)
    done_sp = pd.read_excel(path_done)
    done_sp_list = done_sp[0].tolist()
    wait_sp_list = wait_sp[0].tolist()  # list
    wait_sp_list.extend(newid_t)
    new_wait_sp = []
    for i in wait_sp_list:
        if i not in done_sp_list:
            if i not in new_wait_sp:
                new_wait_sp.append(i)
    #print(new_wait_sp)
    new_wait_sp_df = pd.DataFrame(new_wait_sp)
    new_wait_sp_df.to_excel(path_wait, header=True, index=None)#, startrow=len(old))
    return new_wait_sp

def spider_done( id ):
    root = os.getcwd()
    path_done = root + '\\' + 'done' + '.xlsx'
    done_sp = pd.read_excel(path_done)
    done_sp_list = done_sp[0].tolist()
    done_sp_list.append(id)
    new_done_sp_df = pd.DataFrame(done_sp_list)
    new_done_sp_df.to_excel(path_done, header=True, index=None)  # , startrow=len(old))
    return