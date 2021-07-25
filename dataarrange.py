import numpy as np
import pandas as pd
import os
import Single
import re

def dar(data):
    data.columns = ['赛事', '时间', '状态', '主', ':', '客', '编号', '主队', '-', '主队赔率', '主人数', '主客盘口', '客人数', '-', '客队赔率', '-', '大球赔率', '大人数', '大小盘口', '小人数', '-', '小球赔率', '客队']#, '初主', '初盘', '初客', '终主', '终盘', '终客']
    del data['-']

    root = os.getcwd()
    path_done = root + '/' + 'done' + '.xlsx'
    done_sp = pd.read_excel(path_done)
    #print(type(data))
    data_list = data["编号"].tolist()


    done_sp_list = done_sp[0].tolist()
    done_sp_list = list(map(str, done_sp_list))

    #print(done_sp_list)
    for i in done_sp_list:
        if i in data_list:
            data.drop(index = (data.loc[(data['编号'] == i)].index),inplace=True)



    path = root + '/' + 'Tdata' + '.xlsx'
    Tdata = pd.read_excel(path)
    result = Tdata.append(data, ignore_index=True)
    result['编号'] = result['编号'].astype('str')

    norepeat_df = result.drop_duplicates(subset=['编号'], keep='last')
    norepeat_df.to_excel(path, index = None)
    print(norepeat_df)
    return

def EuroandAsiaUpdata(gameid):
    root = os.getcwd()
    path_asia = root + '/' + 'data' + '/' + str(gameid) + 'Asia365bet' + '.xlsx'
    path_euro = root + '/' + 'data' + '/' + str(gameid) + 'Euro365bet' + '.xlsx'
    path_bs = root + '/' + 'data' + '/' + str(gameid) + 'BS365bet' + '.xlsx'
    if not os.path.exists(path_asia):
        Single.gamespiderAsia(gameid, 0)
    if not os.path.exists(path_euro):
        Single.gamespiderEuro(gameid, 0)
    if not os.path.exists(path_bs):
        Single.gamespiderBS(gameid, 0)
    path = root + '/' + 'Tdata' + '.xlsx'
    Udata = pd.read_excel(path)
    list_asia = pd.read_excel(path_asia)
    print(gameid)
    if len(list_asia):
        list_asia = list_asia[list_asia['变化时间'].isin(['-'])]
        #print(list_asia)
        list_asia.columns = ['编号', '主', '盘', '客', '时', '状', '-', '-']
        prime_home_asia = list_asia.iloc[-1, 1]
        prime_dish_asia = list_asia.iloc[-1, 2]
        prime_guest_asia = list_asia.iloc[-1, 3]
        final_home_asia = list_asia.iloc[0, 1]
        final_dish_asia = list_asia.iloc[0, 2]
        final_guest_asia = list_asia.iloc[0, 3]

        Udata.loc[Udata['编号'] == gameid, '初主'] = prime_home_asia
        Udata.loc[Udata['编号'] == gameid, '初盘'] = prime_dish_asia
        Udata.loc[Udata['编号'] == gameid, '初客'] = prime_guest_asia
        Udata.loc[Udata['编号'] == gameid, '终主'] = final_home_asia
        Udata.loc[Udata['编号'] == gameid, '终盘'] = final_dish_asia
        Udata.loc[Udata['编号'] == gameid, '终客'] = final_guest_asia

    list_bs = pd.read_excel(path_bs)
    if len(list_bs):
        list_bs = list_bs[list_bs['变化时间'].isin(['-'])]
        #print(list_asia)
        list_bs.columns = ['编号', '主', '盘', '客', '时', '状', '-', '-']
        prime_big_asia = list_bs.iloc[-1, 1]
        prime_dishbs_asia = list_bs.iloc[-1, 2]
        prime_small_asia = list_bs.iloc[-1, 3]
        final_big_asia = list_bs.iloc[0, 1]
        final_dishbs_asia = list_bs.iloc[0, 2]
        final_small_asia = list_bs.iloc[0, 3]

        Udata.loc[Udata['编号'] == gameid, '初大'] = prime_big_asia
        Udata.loc[Udata['编号'] == gameid, '初大小'] = prime_dishbs_asia
        Udata.loc[Udata['编号'] == gameid, '初小'] = prime_small_asia
        Udata.loc[Udata['编号'] == gameid, '终大'] = final_big_asia
        Udata.loc[Udata['编号'] == gameid, '终大小'] = final_dishbs_asia
        Udata.loc[Udata['编号'] == gameid, '终小'] = final_small_asia

    list_euro = pd.read_excel(path_euro)
    if len(list_euro):
        list_euro.columns = ['编号', '胜', '平', '负', '时', '状']
        prime_win_euro = list_euro.iloc[-1, 1]
        prime_flat_euro = list_euro.iloc[-1, 2]
        prime_lost_euro = list_euro.iloc[-1, 3]
        final_win_euro = list_euro.iloc[0, 1]
        final_flat_euro = list_euro.iloc[0, 2]
        final_lost_euro = list_euro.iloc[0, 3]

        Udata.loc[Udata['编号'] == gameid, '初胜'] = prime_win_euro
        Udata.loc[Udata['编号'] == gameid, '初平'] = prime_flat_euro
        Udata.loc[Udata['编号'] == gameid, '初负'] = prime_lost_euro
        Udata.loc[Udata['编号'] == gameid, '终胜'] = final_win_euro
        Udata.loc[Udata['编号'] == gameid, '终平'] = final_flat_euro
        Udata.loc[Udata['编号'] == gameid, '终负'] = final_lost_euro

    Udata.to_excel(path, index=None)
    return


def AllBetUpdata(gameid):
    root = os.getcwd()

    path = root + '/' + 'Alldata' + '.xlsx'
    Udata = pd.read_excel(path)

    betstr = ['365bet', '10bet', 'aobet']
    for betid in range(len(betstr)):
        #print(betstr[betid])
        #print(betid)
        path_asia = root + '/' + 'data' + '/' + str(gameid) + 'Asia' + betstr[betid] + '.xlsx'
        path_euro = root + '/' + 'data' + '/' + str(gameid) + 'Euro' + betstr[betid] + '.xlsx'
        path_bs = root + '/' + 'data' + '/' + str(gameid) + 'BS' + betstr[betid] + '.xlsx'
        if not os.path.exists(path_asia):
            Single.gamespiderAsia(gameid, betid)
        if not os.path.exists(path_euro):
            Single.gamespiderEuro(gameid, betid)
        if not os.path.exists(path_bs):
            Single.gamespiderBS(gameid, betid)

        list_asia = pd.read_excel(path_asia)
        #print(gameid)
        if len(list_asia):
            list_asia = list_asia[list_asia['变化时间'].isin(['-'])]
            #print(list_asia)
            list_asia.columns = ['编号', '主', '盘', '客', '时', '状', '-', '-']
            prime_home_asia = list_asia.iloc[-1, 1]
            prime_dish_asia = list_asia.iloc[-1, 2]
            prime_guest_asia = list_asia.iloc[-1, 3]
            final_home_asia = list_asia.iloc[0, 1]
            final_dish_asia = list_asia.iloc[0, 2]
            final_guest_asia = list_asia.iloc[0, 3]

            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初主'] = prime_home_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初盘'] = prime_dish_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初客'] = prime_guest_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终主'] = final_home_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终盘'] = final_dish_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终客'] = final_guest_asia

        list_bs = pd.read_excel(path_bs)
        if len(list_bs):
            list_bs = list_bs[list_bs['变化时间'].isin(['-'])]
            #print(list_asia)
            list_bs.columns = ['编号', '主', '盘', '客', '时', '状', '-', '-']
            prime_big_asia = list_bs.iloc[-1, 1]
            prime_dishbs_asia = list_bs.iloc[-1, 2]
            prime_small_asia = list_bs.iloc[-1, 3]
            final_big_asia = list_bs.iloc[0, 1]
            final_dishbs_asia = list_bs.iloc[0, 2]
            final_small_asia = list_bs.iloc[0, 3]

            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初大'] = prime_big_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初大小'] = prime_dishbs_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初小'] = prime_small_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终大'] = final_big_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终大小'] = final_dishbs_asia
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终小'] = final_small_asia

        list_euro = pd.read_excel(path_euro)
        if len(list_euro):
            list_euro.columns = ['编号', '胜', '平', '负', '时', '状']
            prime_win_euro = list_euro.iloc[-1, 1]
            prime_flat_euro = list_euro.iloc[-1, 2]
            prime_lost_euro = list_euro.iloc[-1, 3]
            final_win_euro = list_euro.iloc[0, 1]
            final_flat_euro = list_euro.iloc[0, 2]
            final_lost_euro = list_euro.iloc[0, 3]

            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初胜'] = prime_win_euro
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初平'] = prime_flat_euro
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '初负'] = prime_lost_euro
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终胜'] = final_win_euro
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终平'] = final_flat_euro
            Udata.loc[Udata['编号'] == gameid, betstr[betid] + '终负'] = final_lost_euro

    Udata.to_excel(path, index=None)
    return

def Singleupdata(Homescore, Guestscore, gameid, Date, type):
    root = os.getcwd()
    path = root + '/' + 'Tdata' + '.xlsx'
    Udata = pd.read_excel(path)

    print(gameid)
    print((str)(Homescore)+':'+(str)(Guestscore))
    Udata.loc[Udata['编号'] == gameid, '主'] = Homescore
    Udata.loc[Udata['编号'] == gameid, '客'] = Guestscore
    if(type==0):
        Udata.loc[Udata['编号'] == gameid, '状态'] = '完场'
    elif (type == 1):
        Udata.loc[Udata['编号'] == gameid, '状态'] = '比赛中'
    Udata.loc[Udata['编号'] == gameid, '时间'] = Date
    # Udata['主客比例'] = Udata.apply(lambda x: (float)(x['主人数']) / ((float)(x['主人数']) + (float)(x['客人数']) + 1), axis=1)
    # Udata['大小比例'] = Udata.apply(lambda x: (float)(x['大人数']) / ((float)(x['大人数']) + (float)(x['小人数']) + 1), axis=1)
    # Udata['主客结果'] = Udata.apply(lambda x: 1 if (float)(x['主']) - (float)(x['客']) > (float)(x['主客盘口']) else (0 if (float)(x['主']) - (float)(x['客']) == (float)(x['主客盘口']) else -1), axis=1)
    # Udata['大小结果'] = Udata.apply(lambda x: 1 if (float)(x['主']) + (float)(x['客']) > (float)(x['大小盘口']) else (0 if (float)(x['主']) + (float)(x['客']) == (float)(x['主客盘口']) else -1), axis=1)

    #EuroandAsiaUpdata(gameid)

    norepeat_df = Udata.drop_duplicates(subset=['编号'], keep='last')

    norepeat_df.to_excel(path, index=None)
    print('finish')
    return

# def Querylist():
#     root = os.getcwd()
#     path_done = root + '\\' + 'done' + '.xlsx'
#     path_read = root + '\\' + 'read' + '.xlsx'
#     done_sp = pd.read_excel(path_done)
#     read_sp = pd.read_excel(path_read)
#     done_sp_list = done_sp[0].tolist()
#     read_sp_list = read_sp[0].tolist()
#     new_wait_sp = []
#     for i in done_sp_list:
#         if i not in read_sp_list:
#
#             if i not in new_wait_sp:
#                 new_wait_sp.append(i)
#     for i in range(len(new_wait_sp)):
#         EuroandAsia(new_wait_sp[i])
#     #new_wait_sp_df = pd.DataFrame(new_wait_sp)
#     #new_wait_sp_df.to_excel(path_read, header=True, index=None)  # , startrow=len(old))
#     #return new_wait_sp
#     return
#
