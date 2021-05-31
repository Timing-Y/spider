import os
import pandas as pd
import time

def arrangement():
    root = os.getcwd()
    path_Tdata = root + '\\' + 'Tdata' + '.xlsx'
    Tdata = pd.read_excel(path_Tdata)

    Tdata['主客比例'] = Tdata.apply(lambda x: round((float)(x['主人数']) / ((float)(x['主人数']) + (float)(x['客人数']) +1),2), axis=1)
    Tdata['大小比例'] = Tdata.apply(lambda x: round((float)(x['大人数']) / ((float)(x['大人数']) + (float)(x['小人数']) +1),2), axis=1)



    timestart = '202101010000'

    Tdata['cycle'] = Tdata.apply(lambda x: (int)((time.mktime(
        time.strptime(str(x['时间']), "%Y-%m-%d %H:%M")) - time.mktime(
        time.strptime(str(timestart), "%Y%m%d%H%M"))) / 14400), axis=1)

    Tdata.sort_values('时间', inplace=True)
    Tdata.to_excel(path_Tdata, index=None)

    waitpred_data = Tdata.drop(index=(Tdata.loc[(Tdata['状态'] == "完场")].index), inplace=False)

    #print(waitpred_data)
    path_pred = root + '\\' + 'Nopreddata' + '.xlsx'
    waitpred_data.to_excel(path_pred, index = None)
    Tdata.drop(index = (Tdata.loc[(Tdata['状态'] != "完场")].index),inplace=True)

    Tdata['主客结果'] = Tdata.apply(lambda x: 1 if (float)(x['主']) - (float)(x['客']) > (float)(x['主客盘口']) else -1, axis=1)#(0 if (float)(x['主']) - (float)(x['客']) == (float)(x['主客盘口']) else -1)
    Tdata['大小结果'] = Tdata.apply(lambda x: 1 if (float)(x['主']) + (float)(x['客']) > (float)(x['大小盘口']) else -1, axis=1)#(0 if (float)(x['主']) + (float)(x['客']) == (float)(x['主客盘口']) else -1)
    Tdata['胜平负结果'] = Tdata.apply(lambda x: 1 if (float)(x['主']) > (float)(x['客']) else (0 if (float)(x['主']) == (float)(x['客']) else -1), axis=1)#

    path_real = root + '\\' + 'realdata' + '.xlsx'
    Tdata.to_excel(path_real, index = None)
    #print(Tdata)
    train_data = Tdata.iloc[:-200]
    tets_data = Tdata.iloc[-200:]
    path_train = root + '\\' + 'traindata' + '.xlsx'
    train_data.to_excel(path_train, index = None)
    path_test = root + '\\' + 'testdata' + '.xlsx'
    tets_data.to_excel(path_test, index = None)
    #print(train_data)
    #print(tets_data)
