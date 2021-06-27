# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os,time
import random
import guesssp
import Single
import dataarrange
import arrangement
import pred
from retrying import retry
from shutil import copyfile



#@retry
def test():
    gameid = guesssp.spider()
    new_sp = guesssp.arrange(gameid)
    for i in range(len(new_sp)):
        Single.spider_determine(new_sp[i])

        time.sleep(random.randrange(1, 2))
        # print(new_sp[i])
    arrangement.arrangement()
    pred.pred()
    backups(1)

def backups(type):
    root = os.getcwd()
    flile_name = root + '\\' + 'backups' + '.xlsx'
    backups_name = root + '\\' + 'Tdata' + '.xlsx'
    if type == 1:
        copyfile(backups_name, flile_name)
    elif type == 2:
        copyfile(flile_name, backups_name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #while(1):
    test()
    #backups()

    # step = 1
    # if step == 1:
    #     gameid = guesssp.spider()
    #     new_sp = guesssp.arrange(gameid)
    #     for i in range(len(new_sp)):
    #         Single.gamespiderAsia(new_sp[i], 0)
    #         Single.gamespiderEuro(new_sp[i], 0)
    #         Single.gamespiderBS(new_sp[i], 0)
    #         dataarrange.EuroandAsiaUpdata(new_sp[i])
    #         #Single.gamespiderAsia(new_sp[i], 1)
    #         #Single.gamespiderEuro(new_sp[i], 1)
    #         #Single.gamespiderAsia(new_sp[i], 2)
    #         #Single.gamespiderEuro(new_sp[i], 2)
    #         time.sleep(random.randrange(1, 2))
    #         # print(new_sp[i])
    #     arrangement.arrangement()
    #     pred.pred()
    # elif step == 2:




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
