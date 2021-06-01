import numpy as np
import pandas as pd
import os
import re

def dar(data):
    data.columns = ['赛事', '时间', '状态', '主', ':', '客', '编号', '主队', '-', '主队赔率', '主人数', '主客盘口', '客人数', '-', '客队赔率', '-', '大球赔率', '大人数', '大小盘口', '小人数', '-', '小球赔率', '客队']#, '初主', '初盘', '初客', '终主', '终盘', '终客']
    del data['-']

    data.replace('平手', 0, inplace = True)
    data.replace('平/半', 0.25, inplace = True)
    data.replace('半球', 0.5, inplace = True)
    data.replace('半/一', 0.75, inplace = True)
    data.replace('一球', 1, inplace = True)
    data.replace('一/球半', 1.25, inplace = True)
    data.replace('球半', 1.5, inplace = True)
    data.replace('球半/两', 1.75, inplace = True)
    data.replace('两球', 2, inplace = True)
    data.replace('两/两球半', 2.25, inplace = True)
    data.replace('两球半', 2.5, inplace = True)
    data.replace('两球半/三', 2.75, inplace = True)
    data.replace('三球', 3, inplace = True)
    data.replace('三/三球半', 3.25, inplace = True)
    data.replace('三球半', 3.5, inplace = True)
    data.replace('三球半/四', 3.75, inplace = True)
    data.replace('四球', 4, inplace = True)
    data.replace('四/四球半', 4.25, inplace=True)

    data.replace('六球半', 6.5, inplace=True)
    data.replace('六球半/七', 6.75, inplace=True)
    data.replace('七球', 7, inplace=True)
    data.replace('七/七球半', 7.25, inplace=True)

    data.replace('受平/半', -0.25, inplace = True)
    data.replace('受半球', -0.5, inplace = True)
    data.replace('受半/一', -0.75, inplace = True)
    data.replace('受一球', -1, inplace = True)
    data.replace('受一/球半', -1.25, inplace = True)
    data.replace('受球半', -1.5, inplace = True)
    data.replace('受球半/两', -1.75, inplace = True)
    data.replace('受两球', -2, inplace = True)
    data.replace('受两/两球半', -2.25, inplace = True)
    data.replace('受两球半', -2.5, inplace = True)
    data.replace('受两球半/三', -2.75, inplace = True)
    data.replace('受三球', -3, inplace = True)
    data.replace('受三/三球半', -3.25, inplace = True)
    data.replace('受三球半', -3.5, inplace = True)
    data.replace('受三球半/四', -3.75, inplace = True)
    data.replace('受四球', -4, inplace = True)

    data.replace('0.5/1', 0.75, inplace = True)
    data.replace('1/1.5', 1.25, inplace = True)
    data.replace('1.5/2', 1.75, inplace = True)
    data.replace('2/2.5', 2.25, inplace = True)
    data.replace('2.5/3', 2.75, inplace = True)
    data.replace('3/3.5', 3.25, inplace = True)
    data.replace('3.5/4', 3.75, inplace = True)
    data.replace('4/4.5', 4.25, inplace = True)
    data.replace('4.5/5', 4.75, inplace = True)
    data.replace('5/5.5', 5.25, inplace = True)
    data.replace('5.5/6', 5.75, inplace = True)

    data.replace('7/7.5', 7.25, inplace=True)
    data.replace('7.5/8', 7.75, inplace=True)

    # data['主客比例'] = data.apply(lambda x: (float)(x['主人数']) / ((float)(x['主人数']) + (float)(x['客人数']) +1), axis=1)
    # data['大小比例'] = data.apply(lambda x: (float)(x['大人数']) / ((float)(x['大人数']) + (float)(x['小人数']) +1), axis=1)
    # data['主客结果'] = data.apply(lambda x: 1 if (float)(x['主']) - (float)(x['客']) > (float)(x['主客盘口']) else (0 if (float)(x['主']) - (float)(x['客']) == (float)(x['主客盘口']) else -1), axis=1)
    # data['大小结果'] = data.apply(lambda x: 1 if (float)(x['主']) + (float)(x['客']) > (float)(x['大小盘口']) else (0 if (float)(x['主']) + (float)(x['客']) == (float)(x['主客盘口']) else -1), axis=1)
    root = os.getcwd()
    path_done = root + '/' + 'done' + '.xlsx'
    done_sp = pd.read_excel(path_done)
    #print(type(data))
    data_list = data["编号"].tolist()

    #print(data_list)
    done_sp_list = done_sp[0].tolist()
    done_sp_list = list(map(str, done_sp_list))
    #print(done_sp_list)
    for i in done_sp_list:
        if i in data_list:
            data.drop(index = (data.loc[(data['编号'] == i)].index),inplace=True)
    #print(data)


    path = root + '/' + 'Tdata' + '.xlsx'
    Tdata = pd.read_excel(path)
    result = Tdata.append(data, ignore_index=True)
    result['编号'] = result['编号'].astype('str')
    # result['主客比例'] = result.apply(lambda x: (float)(x['主人数']) / ((float)(x['主人数']) + (float)(x['客人数']) +1), axis=1)
    # result['大小比例'] = result.apply(lambda x: (float)(x['大人数']) / ((float)(x['大人数']) + (float)(x['小人数']) +1), axis=1)
    # result['主客结果'] = result.apply(lambda x: 1 if (float)(x['主']) - (float)(x['客']) > (float)(x['主客盘口']) else (0 if (float)(x['主']) - (float)(x['客']) == (float)(x['主客盘口']) else -1), axis=1)
    # result['大小结果'] = result.apply(lambda x: 1 if (float)(x['主']) + (float)(x['客']) > (float)(x['大小盘口']) else (0 if (float)(x['主']) + (float)(x['客']) == (float)(x['主客盘口']) else -1), axis=1)

    norepeat_df = result.drop_duplicates(subset=['编号'], keep='last')
    norepeat_df.to_excel(path, index = None)
    print(norepeat_df)
    return

def EuroandAsiaUpdata(gameid):
    root = os.getcwd()
    path_asia = root + '/' + 'data' + '/' + str(gameid) + 'Asia365bet' + '.xlsx'
    path_euro = root + '/' + 'data' + '/' + str(gameid) + 'Euro365bet' + '.xlsx'
    path_bs = root + '/' + 'data' + '/' + str(gameid) + 'BS365bet' + '.xlsx'
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


    Udata.replace('平手', 0, inplace = True)
    Udata.replace('平手/半球', 0.25, inplace = True)
    Udata.replace('半球', 0.5, inplace = True)
    Udata.replace('半球/一球', 0.75, inplace = True)
    Udata.replace('一球', 1, inplace = True)
    Udata.replace('一球/球半', 1.25, inplace = True)
    Udata.replace('球半', 1.5, inplace = True)
    Udata.replace('球半/两球', 1.75, inplace = True)
    Udata.replace('两球', 2, inplace = True)
    Udata.replace('两球/两球半', 2.25, inplace = True)
    Udata.replace('两球半', 2.5, inplace = True)
    Udata.replace('两球半/三球', 2.75, inplace = True)
    Udata.replace('三球', 3, inplace = True)
    Udata.replace('三球/三球半', 3.25, inplace = True)
    Udata.replace('三球半', 3.5, inplace = True)
    Udata.replace('三球半/四球', 3.75, inplace = True)
    Udata.replace('四球', 4, inplace = True)
    Udata.replace('四球/四球半', 4.25, inplace=True)
    Udata.replace('四球半', 4.5, inplace=True)
    Udata.replace('四球半/五球', 4.75, inplace=True)

    Udata.replace('六球半', 6.5, inplace=True)
    Udata.replace('六球半/七球', 6.75, inplace=True)
    Udata.replace('七球', 7, inplace=True)
    Udata.replace('七球/七球半', 7.25, inplace=True)

    Udata.replace('0.5/1', 0.75, inplace = True)
    Udata.replace('1/1.5', 1.25, inplace = True)
    Udata.replace('1.5/2', 1.75, inplace = True)
    Udata.replace('2/2.5', 2.25, inplace = True)
    Udata.replace('2.5/3', 2.75, inplace = True)
    Udata.replace('3/3.5', 3.25, inplace = True)
    Udata.replace('3.5/4', 3.75, inplace = True)
    Udata.replace('4/4.5', 4.25, inplace = True)
    Udata.replace('4.5/5', 4.75, inplace = True)
    Udata.replace('5/5.5', 5.25, inplace = True)

    Udata.replace('5.5/6', 5.75, inplace = True)

    Udata.replace('7/7.5', 7.25, inplace=True)
    Udata.replace('7.5/8', 7.75, inplace=True)

    Udata.replace('受让平手/半球', -0.25, inplace = True)
    Udata.replace('受让半球', -0.5, inplace = True)
    Udata.replace('受让半球/一球', -0.75, inplace = True)
    Udata.replace('受让一球', -1, inplace = True)
    Udata.replace('受让一球/球半', -1.25, inplace = True)
    Udata.replace('受让球半', -1.5, inplace = True)
    Udata.replace('受让球半/两球', -1.75, inplace = True)
    Udata.replace('受让两球', -2, inplace = True)
    Udata.replace('受让两球/两球半', -2.25, inplace = True)
    Udata.replace('受让两球半', -2.5, inplace = True)
    Udata.replace('受让两球半/三球', -2.75, inplace = True)
    Udata.replace('受让三球', -3, inplace = True)
    Udata.replace('受让三球/三球半', -3.25, inplace = True)
    Udata.replace('受让三球半', -3.5, inplace = True)
    Udata.replace('受让三球半/四球', -3.75, inplace = True)
    Udata.replace('受让四球', -4, inplace = True)
    Udata.replace('受让四球/四球半', -4.25, inplace=True)
    Udata.replace('受让四球半', -4.5, inplace=True)
    Udata.replace('受让四球半/五球', -4.75, inplace=True)
    Udata.to_excel(path, index=None)
    return

def Singleupdata(Homescore, Guestscore, gameid, Date):
    root = os.getcwd()
    path = root + '/' + 'Tdata' + '.xlsx'
    Udata = pd.read_excel(path)

    print(gameid)
    print((str)(Homescore)+':'+(str)(Guestscore))
    Udata.loc[Udata['编号'] == gameid, '主'] = Homescore
    Udata.loc[Udata['编号'] == gameid, '客'] = Guestscore
    Udata.loc[Udata['编号'] == gameid, '状态'] = '完场'
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
