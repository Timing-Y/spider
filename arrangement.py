import os
import pandas as pd
import time
import datetime

def HtoD(Udata):
    Udata.replace('平手', 0, inplace=True)
    Udata.replace('平手/半球', 0.25, inplace=True)
    Udata.replace('半球', 0.5, inplace=True)
    Udata.replace('半球/一球', 0.75, inplace=True)
    Udata.replace('一球', 1, inplace=True)
    Udata.replace('一球/球半', 1.25, inplace=True)
    Udata.replace('球半', 1.5, inplace=True)
    Udata.replace('球半/两球', 1.75, inplace=True)
    Udata.replace('两球', 2, inplace=True)
    Udata.replace('两球/两球半', 2.25, inplace=True)
    Udata.replace('两球半', 2.5, inplace=True)
    Udata.replace('两球半/三球', 2.75, inplace=True)
    Udata.replace('三球', 3, inplace=True)
    Udata.replace('三球/三球半', 3.25, inplace=True)
    Udata.replace('三球半', 3.5, inplace=True)
    Udata.replace('三球半/四球', 3.75, inplace=True)
    Udata.replace('四球', 4, inplace=True)
    Udata.replace('四球/四球半', 4.25, inplace=True)
    Udata.replace('四球半', 4.5, inplace=True)
    Udata.replace('四球半/五球', 4.75, inplace=True)
    Udata.replace('五球', 5, inplace=True)
    Udata.replace('五球/五球半', 5.25, inplace=True)
    Udata.replace('五球半', 5.5, inplace=True)
    Udata.replace('五球半/六球', 5.75, inplace=True)
    Udata.replace('六球', 6, inplace=True)
    Udata.replace('六球/六球半', 6.25, inplace=True)
    Udata.replace('六球半', 6.5, inplace=True)
    Udata.replace('六球半/七球', 6.75, inplace=True)
    Udata.replace('七球', 7, inplace=True)
    Udata.replace('七球/七球半', 7.25, inplace=True)
    Udata.replace('七球半', 7.5, inplace=True)
    Udata.replace('七球半/八球', 7.75, inplace=True)

    Udata.replace('受让平手/半球', -0.25, inplace=True)
    Udata.replace('受让半球', -0.5, inplace=True)
    Udata.replace('受让半球/一球', -0.75, inplace=True)
    Udata.replace('受让一球', -1, inplace=True)
    Udata.replace('受让一球/球半', -1.25, inplace=True)
    Udata.replace('受让球半', -1.5, inplace=True)
    Udata.replace('受让球半/两球', -1.75, inplace=True)
    Udata.replace('受让两球', -2, inplace=True)
    Udata.replace('受让两球/两球半', -2.25, inplace=True)
    Udata.replace('受让两球半', -2.5, inplace=True)
    Udata.replace('受让两球半/三球', -2.75, inplace=True)
    Udata.replace('受让三球', -3, inplace=True)
    Udata.replace('受让三球/三球半', -3.25, inplace=True)
    Udata.replace('受让三球半', -3.5, inplace=True)
    Udata.replace('受让三球半/四球', -3.75, inplace=True)
    Udata.replace('受让四球', -4, inplace=True)
    Udata.replace('受让四球/四球半', -4.25, inplace=True)
    Udata.replace('受让四球半', -4.5, inplace=True)
    Udata.replace('受让四球半/五球', -4.75, inplace=True)
    Udata.replace('受让五球', -5, inplace=True)
    Udata.replace('受让五球/五球半', -5.25, inplace=True)
    Udata.replace('受让五球半', -5.5, inplace=True)
    Udata.replace('受让五球半/六球', -5.75, inplace=True)
    Udata.replace('受让六球', -6, inplace=True)
    Udata.replace('受让六球/六球半', -6.25, inplace=True)
    Udata.replace('受让六球半', -6.5, inplace=True)
    Udata.replace('受让六球半/七球', -6.75, inplace=True)
    Udata.replace('受让七球', -7, inplace=True)
    Udata.replace('受让七球/七球半', -7.25, inplace=True)
    Udata.replace('受让七球半', -7.5, inplace=True)
    Udata.replace('受让七球半/八球', -7.75, inplace=True)

    Udata.replace('平手', 0, inplace = True)
    Udata.replace('平/半', 0.25, inplace = True)
    Udata.replace('半球', 0.5, inplace = True)
    Udata.replace('半/一', 0.75, inplace = True)
    Udata.replace('一球', 1, inplace = True)
    Udata.replace('一/球半', 1.25, inplace = True)
    Udata.replace('球半', 1.5, inplace = True)
    Udata.replace('球半/两', 1.75, inplace = True)
    Udata.replace('两球', 2, inplace = True)
    Udata.replace('两/两球半', 2.25, inplace = True)
    Udata.replace('两球半', 2.5, inplace = True)
    Udata.replace('两球半/三', 2.75, inplace = True)
    Udata.replace('三球', 3, inplace = True)
    Udata.replace('三/三球半', 3.25, inplace = True)
    Udata.replace('三球半', 3.5, inplace = True)
    Udata.replace('三球半/四', 3.75, inplace = True)
    Udata.replace('四球', 4, inplace = True)
    Udata.replace('四/四球半', 4.25, inplace=True)
    Udata.replace('四球半', 4.5, inplace=True)
    Udata.replace('四球半/五', 4.75, inplace=True)
    Udata.replace('五球', 5, inplace=True)
    Udata.replace('五/五球半', 5.25, inplace=True)
    Udata.replace('五球半', 5.5, inplace=True)
    Udata.replace('五球半/六', 5.75, inplace=True)
    Udata.replace('六球', 6, inplace=True)
    Udata.replace('六/六球半', 6.25, inplace=True)
    Udata.replace('六球半', 6.5, inplace=True)
    Udata.replace('六球半/七', 6.75, inplace=True)
    Udata.replace('七球', 7, inplace=True)
    Udata.replace('七/七球半', 7.25, inplace=True)
    Udata.replace('七球半', 7.5, inplace=True)
    Udata.replace('七球半/八', 7.75, inplace=True)


    Udata.replace('受平/半', -0.25, inplace = True)
    Udata.replace('受半球', -0.5, inplace = True)
    Udata.replace('受半/一', -0.75, inplace = True)
    Udata.replace('受一球', -1, inplace = True)
    Udata.replace('受一/球半', -1.25, inplace = True)
    Udata.replace('受球半', -1.5, inplace = True)
    Udata.replace('受球半/两', -1.75, inplace = True)
    Udata.replace('受两球', -2, inplace = True)
    Udata.replace('受两/两球半', -2.25, inplace = True)
    Udata.replace('受两球半', -2.5, inplace = True)
    Udata.replace('受两球半/三', -2.75, inplace = True)
    Udata.replace('受三球', -3, inplace = True)
    Udata.replace('受三/三球半', -3.25, inplace = True)
    Udata.replace('受三球半', -3.5, inplace = True)
    Udata.replace('受三球半/四', -3.75, inplace = True)
    Udata.replace('受四球', -4, inplace = True)
    Udata.replace('受四/四球半', -4.25, inplace=True)
    Udata.replace('受四球半', -4.5, inplace=True)
    Udata.replace('受四球半/五', -4.75, inplace=True)
    Udata.replace('受五球', -5, inplace=True)
    Udata.replace('受五/五球半', -5.25, inplace=True)
    Udata.replace('受五球半', -5.5, inplace=True)
    Udata.replace('受五球半/六', -5.75, inplace=True)
    Udata.replace('受六球', -6, inplace=True)
    Udata.replace('受六/六球半', -6.25, inplace=True)
    Udata.replace('受六球半', -6.5, inplace=True)
    Udata.replace('受六球半/七', -6.75, inplace=True)
    Udata.replace('受七球', -7, inplace=True)
    Udata.replace('受七/七球半', -7.25, inplace=True)
    Udata.replace('受七球半', -7.5, inplace=True)
    Udata.replace('受七球半/八', -7.75, inplace=True)

    Udata.replace('0.5/1', 0.75, inplace=True)
    Udata.replace('1/1.5', 1.25, inplace=True)
    Udata.replace('1.5/2', 1.75, inplace=True)
    Udata.replace('2/2.5', 2.25, inplace=True)
    Udata.replace('2.5/3', 2.75, inplace=True)
    Udata.replace('3/3.5', 3.25, inplace=True)
    Udata.replace('3.5/4', 3.75, inplace=True)
    Udata.replace('4/4.5', 4.25, inplace=True)
    Udata.replace('4.5/5', 4.75, inplace=True)
    Udata.replace('5/5.5', 5.25, inplace=True)
    Udata.replace('5.5/6', 5.75, inplace=True)
    Udata.replace('6/6.5', 6.25, inplace=True)
    Udata.replace('6.5/7', 6.75, inplace=True)
    Udata.replace('7/7.5', 7.25, inplace=True)
    Udata.replace('7.5/8', 7.75, inplace=True)
    Udata.replace('8/8.5', 8.25, inplace=True)
    Udata.replace('8.5/9', 8.75, inplace=True)

    return Udata

def arrangement():
    root = os.getcwd()
    path_Tdata = root + '\\' + 'Tdata' + '.xlsx'
    Tdata = pd.read_excel(path_Tdata)

    Tdata = HtoD(Tdata)

    Tdata = Tdata.drop(index=(Tdata.loc[(Tdata['状态'] == "待定")].index), inplace=False)
    Tdata = Tdata.drop(index=(Tdata.loc[(Tdata['状态'] == "推迟")].index), inplace=False)

    Tdata['主客比例'] = Tdata.apply(lambda x: round((float)(x['主人数']) / ((float)(x['主人数']) + (float)(x['客人数']) +1),2), axis=1)
    Tdata['大小比例'] = Tdata.apply(lambda x: round((float)(x['大人数']) / ((float)(x['大人数']) + (float)(x['小人数']) +1),2), axis=1)

    Tdata = Tdata.replace("&nbsp;",0)

    timestart = '202101010000'

    Tdata['cycle'] = Tdata.apply(lambda x: (int)((time.mktime(
        time.strptime(str(x['时间']), "%Y-%m-%d %H:%M")) - time.mktime(
        time.strptime(str(timestart), "%Y%m%d%H%M"))) / 14400), axis=1)

    Tdata.sort_values('时间', inplace=True)
    Tdata.to_excel(path_Tdata, index=None)

    waitpred_data = Tdata.drop(index=(Tdata.loc[(Tdata['状态'] == "完场")].index), inplace=False)

    #print(waitpred_data)

    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    waitpred_data['nowtime'] = waitpred_data.apply(lambda x: (int)((time.mktime(
        time.strptime(str(x['时间']), "%Y-%m-%d %H:%M")) - time.mktime(
        time.strptime(str(nowtime), "%Y-%m-%d %H:%M"))) / 14400), axis=1)
    waitpred_data = waitpred_data.loc[waitpred_data["nowtime"] >= -10]
    waitpred_data = waitpred_data.loc[waitpred_data["nowtime"] <= 0]

    waitpred_data = waitpred_data.drop(['nowtime'],axis=1)


    path_pred = root + '\\' + 'Nopreddata' + '.xlsx'
    waitpred_data.to_excel(path_pred, index = None)
    Tdata.drop(index = (Tdata.loc[(Tdata['状态'] != "完场")].index),inplace=True)

    Tdata['主客结果'] = Tdata.apply(lambda x: 1 if (float)(x['主']) - (float)(x['客']) >= (float)(x['主客盘口']) else -1, axis=1)#(0 if (float)(x['主']) - (float)(x['客']) == (float)(x['主客盘口']) else -1)
    Tdata['大小结果'] = Tdata.apply(lambda x: 1 if (float)(x['主']) + (float)(x['客']) >= (float)(x['大小盘口']) else -1, axis=1)#(0 if (float)(x['主']) + (float)(x['客']) == (float)(x['主客盘口']) else -1)
    Tdata['胜平负结果'] = Tdata.apply(lambda x: 1 if (float)(x['主']) > (float)(x['客']) else (0 if (float)(x['主']) == (float)(x['客']) else -1), axis=1)#

    path_real = root + '\\' + 'realdata' + '.xlsx'
    Tdata.to_excel(path_real, index = None)
    #print(Tdata)
    train_data = Tdata.iloc[:-50]
    tets_data = Tdata.iloc[-50:]
    path_train = root + '\\' + 'traindata' + '.xlsx'
    train_data.to_excel(path_train, index = None)
    path_test = root + '\\' + 'testdata' + '.xlsx'
    tets_data.to_excel(path_test, index = None)
