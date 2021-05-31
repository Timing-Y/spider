import os
import numpy as np
import pandas as pd

gameid1 = 1956223
gameid2 = 1913930
betid = 1
betstr = ['365bet', '10bet', 'aobet']
root = os.getcwd()
path1 = root + '\\' + 'data\\' + str(gameid1) + 'Euro' + betstr[betid] + '.xlsx'
path2 = root + '\\' + 'data\\' + str(gameid2) + 'Euro' + betstr[betid] + '.xlsx'
sp_result1 = pd.read_excel(path1)
sp_result2 = pd.read_excel(path2)
#print(sp_result)
print(sp_result1.corr(method='pearson', min_periods=1))
print(sp_result1.corr(method='spearman', min_periods=1))
print(sp_result2.corr(method='pearson', min_periods=1))
print(sp_result2.corr(method='spearman', min_periods=1))
#print(np.corrcoef(sp_result1['和局'], sp_result2['和局']))
#dfab.A.corr(dfab.B)