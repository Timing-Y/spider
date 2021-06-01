# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import joblib
from mail import mail
import math

import datetime


list_Hdirs = ["HModel20210120", "HModel20210121", "HModel20210122", "HModel20210123"]
list_Ddirs = ["DModel20210121"]
list_D2dirs = ["DModel20210122", "DModel20210123"]
list_Adirs = ["AModel20210124"]
list_D3dirs = ["DModel20210205"]
list_D4dirs = ["DModel20210222", "DModel20210223", "DModel20210224", "DModel20210225", "DModel20210226", "DModel20210227", "DModel20210228", "DModel20210301"]

# Press the green button in the gutter to run the script.
def pred( ):
    root = os.getcwd()
    real_path = root + '/' + 'realdata' + '.xlsx'
    train_path = root + '/' + 'traindata' + '.xlsx'
    test_path = root + '/' + 'testdata' + '.xlsx'
    nopred_path = root + '/' + 'Nopreddata' + '.xlsx'

    real_data = pd.DataFrame(pd.read_excel(test_path))
    real_data = real_data.fillna(0)
    realD4_x = real_data[
        ["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "主人数", "客人数", "主客比例", "cycle"]]
    realD3_x = real_data[
        ["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "初大", "初大小", "初小", "终大", "终大小", "终小"]]
    realD2_x = real_data[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负"]]
    realD_x = real_data[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "主客比例", "大小比例"]]  #
    real_x = real_data[
        ["主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数", "初主", "初盘", "初客", "终主", "终盘", "终客",
         "初胜", "初平", "初负", "终胜", "终平", "终负", "主客比例",
         "大小比例"]]  # "主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数",
    realA_x = real_data[
        ["主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数", "初主", "初盘", "初客", "终主", "终盘", "终客",
         "初胜", "初平", "初负", "终胜", "终平", "终负", "初大", "初大小", "初小", "终大", "终大小", "终小"]]  #
    real_y1 = real_data["主客结果"]

    test_data = pd.DataFrame(pd.read_excel(test_path))
    test_data = test_data.fillna(0)
    testD4_x = test_data[
        ["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "主人数", "客人数", "主客比例", "cycle"]]
    testD3_x = test_data[
        ["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "初大", "初大小", "初小", "终大", "终大小", "终小"]]
    testD2_x = test_data[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负"]]
    testD_x = test_data[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "主客比例", "大小比例"]]  #
    test_x = test_data[
        ["主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数", "初主", "初盘", "初客", "终主", "终盘", "终客",
         "初胜", "初平", "初负", "终胜", "终平", "终负", "主客比例",
         "大小比例"]]  # "主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数",
    testA_x = test_data[
        ["主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数", "初主", "初盘", "初客", "终主", "终盘", "终客",
         "初胜", "初平", "初负", "终胜", "终平", "终负", "初大", "初大小", "初小", "终大", "终大小", "终小"]]  #
    test_y1 = test_data["主客结果"]

    #
    #
    # test_data = pd.DataFrame(pd.read_excel(test_path))
    # test_x = test_data[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负"]]#"主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数",
    # test_y1 = test_data["主客结果"]
    #
    # data = pd.DataFrame(pd.read_excel(train_path))
    # train_x = data[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负"]]#"主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数",
    # train_y1 = data["主客结果"]
    # y2 = data["大小结果"]
    # y3 = data["胜平负结果"]
    data_nopred = pd.DataFrame(pd.read_excel(nopred_path))
    data_nopred = data_nopred.fillna(0)
    nopredD4_x = data_nopred[
        ["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "主人数", "客人数", "主客比例", "cycle"]]
    nopredD3_x = data_nopred[
        ["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "初大", "初大小", "初小", "终大", "终大小", "终小"]]
    nopredD2_x = data_nopred[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负"]]
    nopredD_x = data_nopred[["初主", "初盘", "初客", "终主", "终盘", "终客", "初胜", "初平", "初负", "终胜", "终平", "终负", "主客比例", "大小比例"]]  #
    nopred_x = data_nopred[
        ["主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数", "初主", "初盘", "初客", "终主", "终盘", "终客",
         "初胜", "初平", "初负", "终胜", "终平", "终负", "主客比例", "大小比例"]]  #
    nopredA_x = data_nopred[
        ["主队赔率", "主客盘口", "客队赔率", "主人数", "客人数", "大球赔率", "大小盘口", "小球赔率", "大人数", "小人数", "初主", "初盘", "初客", "终主", "终盘", "终客",
         "初胜", "初平", "初负", "终胜", "终平", "终负", "初大", "初大小", "初小", "终大", "终大小", "终小"]]  #
    nopred_y1 = data_nopred["主客结果"]

    # clf2 = RandomForestClassifier(n_estimators=10, max_features=math.sqrt(n_features), max_depth=None,
    #                              min_samples_split=2, bootstrap=True)
    # X_train = x[:, :150]
    # Y_train = y[:, -1]
    # X_test = data_test[:, :-1]
    # Y_test = data_test[:, -1]

    mode = 0
    allpred_path = root + '/' + 'Allpred' + '.xlsx'
    testpred_path = root + '/' + 'Nearpred' + '.xlsx'

    out_allpred = pd.DataFrame()
    out_testpred = pd.DataFrame()
    if mode == 0:
        for d in list_Hdirs:
            out_pred = []
            out_pred = pd.DataFrame()
            test_pred = []
            test_pred = pd.DataFrame()
            score_list = []
            average_score = 0
            dirs = d
            if not os.path.exists(dirs):
                os.makedirs(dirs)
            list_dir = os.listdir(dirs)
            print(list_dir)
            for num in list_dir:
                LR = joblib.load(dirs + '/' + str(num))
                data_pred = LR.predict(nopred_x)
                # data_pred = LR.predict(real_x)#aaaaaaaaaaaaa

                real_score = LR.score(real_x, real_y1)
                score_list.append(real_score)
                average_score = np.mean(score_list)

                # print('dir=' + str(dirs))
                # print('nums=' + str(num))
                # print("real_score=%f" % real_score)
                # print('average_score=' + str(average_score))
                # data_pred.append(data_pred, np.array([real_score], dtype=dtype))

                out_pred[num] = data_pred

                testdata_pred = LR.predict(test_x)

                test_pred[num] = testdata_pred

            out_pred.append(score_list)
            out_pred.loc['new_row'] = score_list
            out_pred[dirs] = out_pred.apply(lambda x: x.sum(), axis=1)
            out_pred['prob'] = out_pred[dirs] / len(list_dir)
            out_pred[dirs + "pred"] = out_pred.apply(
                lambda x: -1 if (float)(x['prob']) >= 0.65 else (1 if (float)(x['prob']) <= -0.7 else 0), axis=1)
            out_allpred[dirs] = out_pred[dirs + "pred"]
            # out_pred[dirs + "pred"] = ((out_pred[dirs + "prob"] >= 0.8) or (out_pred[dirs + "prob"] <= -0.8))
            preddata_path = root + '/' + dirs + '.xlsx'
            out_pred.to_excel(preddata_path)

            test_pred.append(score_list)
            test_pred.loc['new_row'] = score_list
            test_pred[dirs] = test_pred.apply(lambda x: x.sum(), axis=1)
            test_pred['prob'] = test_pred[dirs] / len(list_dir)
            test_pred[dirs + "pred"] = test_pred.apply(
                lambda x: -1 if (float)(x['prob']) >= 0.65 else (1 if (float)(x['prob']) <= -0.7 else 0), axis=1)
            out_testpred[dirs] = test_pred[dirs + "pred"]
            testpreddata_path = root + '/' + dirs + '.xlsx'
            test_pred.to_excel(testpreddata_path)

            curtime = datetime.datetime.now().strftime('%Y/%m%d')
            print(curtime)
            path_history = root + '/history.xlsx'
            df_history = pd.DataFrame(pd.read_excel(path_history))
            df_history.set_index('model')
            a = (df_history['model'] == dirs)
            print(a)
            b = 0
            for i in a:
                print(i)
                if i == True:
                    b = 1
            if b == 0:
                df_history = df_history.append({'model': dirs}, ignore_index=True)
            df_history.loc[df_history['model'] == dirs, curtime] = average_score
            print(df_history)
            df_history.to_excel(path_history, index=None)

        for d in list_Ddirs:
            out_pred = []
            out_pred = pd.DataFrame()
            test_pred = []
            test_pred = pd.DataFrame()
            score_list = []
            average_score = 0
            dirs = d
            if not os.path.exists(dirs):
                os.makedirs(dirs)
            list_dir = os.listdir(dirs)
            print(list_dir)
            for num in list_dir:
                LR = joblib.load(dirs + '/' + str(num))
                data_pred = LR.predict(nopredD_x)
                # data_pred = LR.predict(realD_x)#aaaaaaaaaaaaa

                real_score = LR.score(realD_x, real_y1)
                score_list.append(real_score)
                average_score = np.mean(score_list)

                # print('dir=' + str(dirs))
                # print('nums=' + str(num))
                # print("real_score=%f" % real_score)
                # print('average_score=' + str(average_score))
                # data_pred.append(data_pred, np.array([real_score], dtype=dtype))

                out_pred[num] = data_pred

                testdata_pred = LR.predict(testD_x)
                test_pred[num] = testdata_pred

            out_pred.append(score_list)
            out_pred.loc['new_row'] = score_list
            out_pred[dirs] = out_pred.apply(lambda x: x.sum(), axis=1)
            out_pred["prob"] = out_pred[dirs] / len(list_dir)
            out_pred[dirs + "pred"] = out_pred.apply(
                lambda x: -1 if (float)(x["prob"]) >= 0.65 else (1 if (float)(x["prob"]) <= -0.7 else 0), axis=1)
            out_allpred[dirs] = out_pred[dirs + "pred"]
            # out_pred[dirs + "pred"] = ((out_pred[dirs + "prob"] >= 0.8) or (out_pred[dirs + "prob"] <= -0.8))
            preddata_path = root + '/' + dirs + '.xlsx'
            out_pred.to_excel(preddata_path)

            test_pred.append(score_list)
            test_pred.loc['new_row'] = score_list
            test_pred[dirs] = test_pred.apply(lambda x: x.sum(), axis=1)
            test_pred['prob'] = test_pred[dirs] / len(list_dir)
            test_pred[dirs + "pred"] = test_pred.apply(
                lambda x: -1 if (float)(x['prob']) >= 0.65 else (1 if (float)(x['prob']) <= -0.7 else 0), axis=1)
            out_testpred[dirs] = test_pred[dirs + "pred"]
            testpreddata_path = root + '/' + dirs + '.xlsx'
            test_pred.to_excel(testpreddata_path)

            curtime = datetime.datetime.now().strftime('%Y/%m%d')
            print(curtime)
            path_history = root + '/history.xlsx'
            df_history = pd.DataFrame(pd.read_excel(path_history))
            df_history.set_index('model')
            a = (df_history['model'] == dirs)
            print(a)
            b = 0
            for i in a:
                print(i)
                if i == True:
                    b = 1
            if b == 0:
                df_history = df_history.append({'model': dirs}, ignore_index=True)
            df_history.loc[df_history['model'] == dirs, curtime] = average_score
            print(df_history)
            df_history.to_excel(path_history, index=None)

        for d in list_D2dirs:
            out_pred = []
            out_pred = pd.DataFrame()
            test_pred = []
            test_pred = pd.DataFrame()
            score_list = []
            average_score = 0
            dirs = d
            if not os.path.exists(dirs):
                os.makedirs(dirs)
            list_dir = os.listdir(dirs)
            print(list_dir)
            for num in list_dir:
                LR = joblib.load(dirs + '/' + str(num))
                data_pred = LR.predict(nopredD2_x)
                # data_pred = LR.predict(realD2_x)  #aaaaaaaaaaaaa

                real_score = LR.score(realD2_x, real_y1)
                score_list.append(real_score)
                average_score = np.mean(score_list)

                # print('dir=' + str(dirs))
                # print('nums=' + str(num))
                # print("real_score=%f" % real_score)
                # print('average_score=' + str(average_score))
                # data_pred.append(data_pred, np.array([real_score], dtype=dtype))

                out_pred[num] = data_pred

                testdata_pred = LR.predict(testD2_x)
                test_pred[num] = testdata_pred

            out_pred.append(score_list)
            out_pred.loc['new_row'] = score_list
            out_pred[dirs] = out_pred.apply(lambda x: x.sum(), axis=1)
            out_pred["prob"] = out_pred[dirs] / len(list_dir)
            out_pred[dirs + "pred"] = out_pred.apply(
                lambda x: -1 if (float)(x["prob"]) >= 0.65 else (1 if (float)(x["prob"]) <= -0.7 else 0), axis=1)
            out_allpred[dirs] = out_pred[dirs + "pred"]
            # out_pred[dirs + "pred"] = ((out_pred[dirs + "prob"] >= 0.8) or (out_pred[dirs + "prob"] <= -0.8))
            preddata_path = root + '/' + dirs + '.xlsx'
            out_pred.to_excel(preddata_path)

            test_pred.append(score_list)
            test_pred.loc['new_row'] = score_list
            test_pred[dirs] = test_pred.apply(lambda x: x.sum(), axis=1)
            test_pred['prob'] = test_pred[dirs] / len(list_dir)
            test_pred[dirs + "pred"] = test_pred.apply(
                lambda x: -1 if (float)(x['prob']) >= 0.65 else (1 if (float)(x['prob']) <= -0.7 else 0), axis=1)
            out_testpred[dirs] = test_pred[dirs + "pred"]
            testpreddata_path = root + '/' + dirs + '.xlsx'
            test_pred.to_excel(testpreddata_path)

            curtime = datetime.datetime.now().strftime('%Y/%m%d')
            print(curtime)
            path_history = root + '/history.xlsx'
            df_history = pd.DataFrame(pd.read_excel(path_history))
            df_history.set_index('model')
            a = (df_history['model'] == dirs)
            # print(a)
            b = 0
            for i in a:
                print(i)
                if i == True:
                    b = 1
            if b == 0:
                df_history = df_history.append({'model': dirs}, ignore_index=True)
            df_history.loc[df_history['model'] == dirs, curtime] = average_score
            print(df_history)
            df_history.to_excel(path_history, index=None)

        for d in list_D3dirs:
            out_pred = []
            out_pred = pd.DataFrame()
            test_pred = []
            test_pred = pd.DataFrame()
            score_list = []
            average_score = 0
            dirs = d
            if not os.path.exists(dirs):
                os.makedirs(dirs)
            list_dir = os.listdir(dirs)
            print(list_dir)
            for num in list_dir:
                LR = joblib.load(dirs + '/' + str(num))
                data_pred = LR.predict(nopredD3_x)
                # data_pred = LR.predict(realD3_x)#aaaaaaaaaaaaa

                real_score = LR.score(realD3_x, real_y1)
                score_list.append(real_score)
                average_score = np.mean(score_list)

                # print('dir=' + str(dirs))
                # print('nums=' + str(num))
                # print("real_score=%f" % real_score)
                # print('average_score=' + str(average_score))
                # data_pred.append(data_pred, np.array([real_score], dtype=dtype))

                out_pred[num] = data_pred

                testdata_pred = LR.predict(testD3_x)
                test_pred[num] = testdata_pred

            out_pred.append(score_list)
            out_pred.loc['new_row'] = score_list
            out_pred[dirs] = out_pred.apply(lambda x: x.sum(), axis=1)
            out_pred["prob"] = out_pred[dirs] / len(list_dir)
            out_pred[dirs + "pred"] = out_pred.apply(
                lambda x: -1 if (float)(x["prob"]) >= 0.65 else (1 if (float)(x["prob"]) <= -0.7 else 0), axis=1)
            out_allpred[dirs] = out_pred[dirs + "pred"]
            # out_pred[dirs + "pred"] = ((out_pred[dirs + "prob"] >= 0.8) or (out_pred[dirs + "prob"] <= -0.8))
            preddata_path = root + '/' + dirs + '.xlsx'
            out_pred.to_excel(preddata_path)

            test_pred.append(score_list)
            test_pred.loc['new_row'] = score_list
            test_pred[dirs] = test_pred.apply(lambda x: x.sum(), axis=1)
            test_pred['prob'] = test_pred[dirs] / len(list_dir)
            test_pred[dirs + "pred"] = test_pred.apply(
                lambda x: -1 if (float)(x['prob']) >= 0.65 else (1 if (float)(x['prob']) <= -0.7 else 0), axis=1)
            out_testpred[dirs] = test_pred[dirs + "pred"]
            testpreddata_path = root + '/' + dirs + '.xlsx'
            test_pred.to_excel(testpreddata_path)

            curtime = datetime.datetime.now().strftime('%Y/%m%d')
            print(curtime)
            path_history = root + '/history.xlsx'
            df_history = pd.DataFrame(pd.read_excel(path_history))
            df_history.set_index('model')
            a = (df_history['model'] == dirs)
            print(a)
            b = 0
            for i in a:
                print(i)
                if i == True:
                    b = 1
            if b == 0:
                df_history = df_history.append({'model': dirs}, ignore_index=True)
            df_history.loc[df_history['model'] == dirs, curtime] = average_score
            print(df_history)
            df_history.to_excel(path_history, index=None)

        for d in list_D4dirs:
            out_pred = []
            out_pred = pd.DataFrame()
            test_pred = []
            test_pred = pd.DataFrame()
            score_list = []
            average_score = 0
            dirs = d
            if not os.path.exists(dirs):
                os.makedirs(dirs)
            list_dir = os.listdir(dirs)
            print(list_dir)
            for num in list_dir:
                LR = joblib.load(dirs + '/' + str(num))
                data_pred = LR.predict(nopredD4_x)
                # data_pred = LR.predict(realD3_x)#aaaaaaaaaaaaa

                real_score = LR.score(realD4_x, real_y1)
                score_list.append(real_score)
                average_score = np.mean(score_list)

                # print('dir=' + str(dirs))
                # print('nums=' + str(num))
                # print("real_score=%f" % real_score)
                # print('average_score=' + str(average_score))
                # data_pred.append(data_pred, np.array([real_score], dtype=dtype))

                out_pred[num] = data_pred

                testdata_pred = LR.predict(testD4_x)
                test_pred[num] = testdata_pred

            out_pred.append(score_list)
            out_pred.loc['new_row'] = score_list
            out_pred[dirs] = out_pred.apply(lambda x: x.sum(), axis=1)
            out_pred["prob"] = out_pred[dirs] / len(list_dir)
            out_pred[dirs + "pred"] = out_pred.apply(
                lambda x: 1 if (float)(x["prob"]) >= 0.65 else (-1 if (float)(x["prob"]) <= -0.7 else 0), axis=1)
            out_allpred[dirs] = out_pred[dirs + "pred"]
            # out_pred[dirs + "pred"] = ((out_pred[dirs + "prob"] >= 0.8) or (out_pred[dirs + "prob"] <= -0.8))
            preddata_path = root + '/' + dirs + '.xlsx'
            out_pred.to_excel(preddata_path)

            test_pred.append(score_list)
            test_pred.loc['new_row'] = score_list
            test_pred[dirs] = test_pred.apply(lambda x: x.sum(), axis=1)
            test_pred['prob'] = test_pred[dirs] / len(list_dir)
            test_pred[dirs + "pred"] = test_pred.apply(
                lambda x: 1 if (float)(x['prob']) >= 0.65 else (-1 if (float)(x['prob']) <= -0.7 else 0), axis=1)
            out_testpred[dirs] = test_pred[dirs + "pred"]
            testpreddata_path = root + '/' + dirs + '.xlsx'
            test_pred.to_excel(testpreddata_path)

            curtime = datetime.datetime.now().strftime('%Y/%m%d')
            print(curtime)
            path_history = root + '/history.xlsx'
            df_history = pd.DataFrame(pd.read_excel(path_history))
            df_history.set_index('model')
            a = (df_history['model'] == dirs)
            print(a)
            b = 0
            for i in a:
                print(i)
                if i == True:
                    b = 1
            if b == 0:
                df_history = df_history.append({'model': dirs}, ignore_index=True)
            df_history.loc[df_history['model'] == dirs, curtime] = average_score
            print(df_history)
            df_history.to_excel(path_history, index=None)

        for d in list_Adirs:
            out_pred = []
            out_pred = pd.DataFrame()
            test_pred = []
            test_pred = pd.DataFrame()
            score_list = []
            average_score = 0
            dirs = d
            if not os.path.exists(dirs):
                os.makedirs(dirs)
            list_dir = os.listdir(dirs)
            print(list_dir)
            for num in list_dir:
                LR = joblib.load(dirs + '/' + str(num))
                data_pred = LR.predict(nopredA_x)
                # data_pred = LR.predict(realA_x)#aaaaaaaaaaaaa

                real_score = LR.score(realA_x, real_y1)
                score_list.append(real_score)
                average_score = np.mean(score_list)

                # print('dir=' + str(dirs))
                # print('nums=' + str(num))
                # print("real_score=%f" % real_score)
                # print('average_score=' + str(average_score))
                # data_pred.append(data_pred, np.array([real_score], dtype=dtype))

                out_pred[num] = data_pred

                testdata_pred = LR.predict(testA_x)
                test_pred[num] = testdata_pred

            out_pred.append(score_list)
            out_pred.loc['new_row'] = score_list
            out_pred[dirs] = out_pred.apply(lambda x: x.sum(), axis=1)
            out_pred["prob"] = out_pred[dirs] / len(list_dir)
            out_pred[dirs + "pred"] = out_pred.apply(
                lambda x: -1 if (float)(x["prob"]) >= 0.65 else (1 if (float)(x["prob"]) <= -0.7 else 0), axis=1)
            out_allpred[dirs] = out_pred[dirs + "pred"]
            # out_pred[dirs + "pred"] = ((out_pred[dirs + "prob"] >= 0.8) or (out_pred[dirs + "prob"] <= -0.8))
            preddata_path = root + '/' + dirs + '.xlsx'
            out_pred.to_excel(preddata_path)

            test_pred.append(score_list)
            test_pred.loc['new_row'] = score_list
            test_pred[dirs] = test_pred.apply(lambda x: x.sum(), axis=1)
            test_pred['prob'] = test_pred[dirs] / len(list_dir)
            test_pred[dirs + "pred"] = test_pred.apply(
                lambda x: -1 if (float)(x['prob']) >= 0.65 else (1 if (float)(x['prob']) <= -0.7 else 0), axis=1)
            out_testpred[dirs] = test_pred[dirs + "pred"]
            testpreddata_path = root + '/' + dirs + '.xlsx'
            test_pred.to_excel(testpreddata_path)

            curtime = datetime.datetime.now().strftime('%Y/%m%d')
            print(curtime)
            path_history = root + '/history.xlsx'
            df_history = pd.DataFrame(pd.read_excel(path_history))
            df_history.set_index('model')
            a = (df_history['model'] == dirs)
            # print(a)
            b = 0
            for i in a:
                print(i)
                if i == True:
                    b = 1
            if b == 0:
                df_history = df_history.append({'model': dirs}, ignore_index=True)
            df_history.loc[df_history['model'] == dirs, curtime] = average_score
            print(df_history)
            df_history.to_excel(path_history, index=None)
        out_allpred['sum'] = out_allpred.apply(lambda x: x.sum(), axis=1)
        out_allpred['编号'] = data_nopred['编号']
        merge_l = data_nopred[["编号", "时间", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口", "主客结果", "大小结果", "cycle"]]

        # out_allpred['sum'] = out_allpred.apply(lambda x: x.sum(), axis=1)#aaaaaaaaaaaaa
        # out_allpred['编号'] = real_data['编号']#aaaaaaaaaaaaa
        # merge_l = real_data[["编号", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口"]]#aaaaaaaaaaaaa

        out_allpred = pd.merge(merge_l,out_allpred,on='编号')
        # out_allpred = data_nopred[["编号", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口"]]
        out_allpred.to_excel(allpred_path)

        out_testpred['sum'] = out_testpred.apply(lambda x: x.sum(), axis=1)
        out_testpred['编号'] = test_data['编号']
        merge_l = test_data[
            ["编号", "时间", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口", "主客结果", "大小结果", "cycle"]]
        out_testpred = pd.merge(merge_l, out_testpred, on='编号')
        out_testpred.to_excel(testpred_path)

        curtime = datetime.datetime.now().strftime('%Y%m%d%H')
        dirs = datetime.datetime.now().strftime('%Y%m%d')
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        out_allpred = out_allpred[abs(out_allpred['sum']) >= 10]
        out_allpred['pred'] = out_allpred.apply(
            lambda x: '主' if (float)(x['sum']) >= 10 else ('客' if (float)(x['sum']) <= -14 else 0), axis=1)

        pred_path = root + '/' + dirs + '/' + curtime + 'Pred' + '.xlsx'
        out_pred = out_allpred[
            ["编号", "时间", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口", "主客结果", "大小结果", "sum", "pred"]]
        out_pred.to_excel(pred_path)
        #mail(out_pred,curtime)
'''
root = os.getcwd()
allpred_path = root + '/' + 'Allpred' + '.xlsx'
out_allpred = pd.DataFrame(pd.read_excel(allpred_path))

curtime = datetime.datetime.now().strftime('%Y%m%d%H')
dirs = datetime.datetime.now().strftime('%Y%m%d')
if not os.path.exists(dirs):
    os.makedirs(dirs)

out_allpred = out_allpred[abs(out_allpred['sum']) >= 10]
out_allpred['pred'] = out_allpred.apply(
    lambda x: '主' if (float)(x['sum']) >= 10 else ('客' if (float)(x['sum']) <= -14 else 0), axis=1)

pred_path = root + '/' + dirs + '/' + curtime + 'Pred' + '.xlsx'
out_pred = out_allpred[
    ["编号", "时间", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口", "主客结果", "大小结果", "sum", "pred"]]
out_pred.to_excel(pred_path)
mail(out_pred,curtime,pred_path)
'''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
