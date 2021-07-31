# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import datetime
import os
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    root = os.getcwd()
    nearpred_path = root + '/' + 'Mergepred' + '.xlsx'
    copypred_path = root + '/' + 'Copypred' + '.xlsx'
    allpred_path = root + '/' + 'Allpred' + '.xlsx'

    nearpred = pd.DataFrame(pd.read_excel(nearpred_path,index_col=0))
    copypred = pd.DataFrame(pd.read_excel(copypred_path,index_col=0))
    allpred = pd.DataFrame(pd.read_excel(allpred_path,index_col=0))


    result = allpred.append(nearpred, ignore_index=True)
    result['编号'] = result['编号'].astype('str')

    result_df = result.drop_duplicates(subset=['编号'], keep='last')
    result_df = result_df.sort_values(by='时间',ascending=False)
    result_df = result_df.reset_index(drop=True)

    Near_pred = result_df

    for num in range(14, 31):
        Near_pred[(str)(num)] = Near_pred.apply(lambda x: 0 if x[num] == 0 else 1 if x['主客结果'] == x[num] else -1,
                                                axis=1)
    Near_pred['predsum'] = Near_pred.apply(lambda x: x[32:49].sum(), axis=1)

    Near_pred = Near_pred.reset_index(drop=True)
    Near_pred = Near_pred[["时间", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口", "cycle", "sum", "predsum"]]

    Average_pred = Near_pred.reset_index(drop=True)

    Near_pred['predave'] = 0
    Near_pred['predave40'] = 0
    Near_pred['predave60'] = 0
    Near_pred['predtrend'] = 0
    # print(Near_pred)
    while (Average_pred.shape[0] >= 50):
        Average_pred = Average_pred.reset_index(drop=True)
        Transfer = Average_pred["cycle"][0]
        Average_pred = Average_pred[Average_pred["cycle"] != Average_pred["cycle"][0]]
        Average_pred = Average_pred.reset_index(drop=True)
        T1_pred = Average_pred[Average_pred["cycle"] != Average_pred["cycle"][0]]
        T1_pred = T1_pred.reset_index(drop=True)
        ave1 = T1_pred["predsum"][0:20].mean()
        ave50 = T1_pred["predsum"][0:40].mean()
        ave100 = T1_pred["predsum"][0:60].mean()
        Near_pred['predave'] = Near_pred.apply(lambda x: ave1 if x["cycle"] == Transfer else x['predave'], axis=1)
        Near_pred['predave40'] = Near_pred.apply(lambda x: ave50 if x["cycle"] == Transfer else x['predave40'], axis=1)
        Near_pred['predave60'] = Near_pred.apply(lambda x: ave100 if x["cycle"] == Transfer else x['predave60'],
                                                  axis=1)
        T_pred = T1_pred[T1_pred["cycle"] != T1_pred["cycle"][0]]
        ave2 = T_pred["predsum"][0:20].mean()
        Near_pred['predtrend'] = Near_pred.apply(lambda x: ave1 - ave2 if x["cycle"] == Transfer else x['predtrend'],
                                                 axis=1)

    Near_pred['predscreen'] = Near_pred.apply(lambda x: 1 if x["predsum"] > 11 else -1 if x["predsum"] < -11 else 0,
                                              axis=1)
    Near_pred['pred'] = Near_pred.apply(lambda x: 1 if x["sum"] > 11 else -1 if x["sum"] < -11 else 0,
                                              axis=1)

    Near_pred['F1step1'] = Near_pred.apply(
        lambda x: 0 if (abs(x["predave"]) < 0.5) else x["pred"] if (abs(x["predave"]) <= 2) else 0, axis=1)
    Near_pred['F1step2'] = Near_pred.apply(lambda x: x["F1step1"] if x["predave"] > x["predtrend"] else 0, axis=1)
    Near_pred['F1step3'] = Near_pred.apply(lambda x: x["F1step1"] if x["predave"] <= x["predtrend"] else 0, axis=1)
    Near_pred['F1step4'] = Near_pred.apply(lambda x: x["F1step3"] if x["predave"] < -1.5 else 0, axis=1)
    Near_pred['F1step5'] = Near_pred.apply(lambda x: -x["F1step3"] if x["predave"] > 1 else 0, axis=1)
    Near_pred['F1step6'] = Near_pred.apply(lambda x: -x["F1step3"] if abs(x["predave"]) <= 1 else 0, axis=1)
    Near_pred['F1step7'] = Near_pred.apply(lambda x: x["F1step2"] + x["F1step4"] + x["F1step5"] + x["F1step6"], axis=1)

    Near_pred['F2step1'] = Near_pred.apply(lambda x: -x["pred"] if x["predave"] > 2 else 0, axis=1)
    Near_pred['F2step2'] = Near_pred.apply(lambda x: x["pred"] if x["predave"] < -2 else 0, axis=1)
    Near_pred['F2step3'] = Near_pred.apply(lambda x: x["F2step1"] if x["predtrend"] > 0.5 else 0, axis=1)
    Near_pred['F2step4'] = Near_pred.apply(lambda x: x["F2step2"] if x["predtrend"] > 0 else 0, axis=1)
    Near_pred['F2step5'] = Near_pred.apply(lambda x: x["F2step3"] + x["F2step4"], axis=1)

    Near_pred['Doublepred'] = Near_pred.apply(lambda x: x["predscreen"] if x["pred"] == x['F2step5'] else -x["predscreen"], axis=1)
    Near_pred['Normalpred'] = Near_pred.apply(lambda x: x["predscreen"] if x["pred"] == x['F1step7'] else -x["predscreen"], axis=1)

    Near_pred['Double'] = Near_pred.apply(lambda x: "主x2" if x["F2step5"] == 1 else "客x2" if x["F2step5"] == -1 else 0, axis=1)
    Near_pred['Normal'] = Near_pred.apply(lambda x: "主" if x["F1step7"] == 1 else "客" if x["F1step7"] == -1 else 0, axis=1)
    Near_pred.drop(index = (Near_pred.loc[(Near_pred['状态'] == "完场")].index),inplace=True)
    Near_pred = Near_pred[
        ["时间", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口", "cycle", 'sum', 'predave', 'predave40', 'predave60', "Normal", "Double"]]

    Near_pred.drop(index=(Near_pred.loc[(abs(Near_pred['sum']) <= 11)].index), inplace=True)
    Near_pred.drop(index=(Near_pred.loc[(Near_pred['Normal'] == 0) & (Near_pred['Double'] == 0)].index), inplace=True)

    out_pred = Near_pred[
        ["时间", "赛事", "状态", "主", ":", "客", "主队", "客队", "主客盘口", "大小盘口", "Normal", "Double"]]
    out_pred = out_pred.sort_values(by='时间', ascending=True)

    if (len(Near_pred) >= 1):
        data_html = Near_pred.to_html()
        ret = mail.mail(data_html, curtime, 1)

    if (len(out_pred) >= 1):
        data_html = out_pred.to_html()
        ret = mail.mail(data_html, curtime, 1)

    #Near_pred.to_excel(copypred_path)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
