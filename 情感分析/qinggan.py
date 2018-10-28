#!/usr/bin/python3
# -*- coding: utf-8 -*-
# /**
#  *                    _ooOoo_
#  *                   o8888888o
#  *                   88" . "88
#  *                   (| -_- |)
#  *                    O\ = /O
#  *                ____/`---'\____
#  *              .   ' \\| |// `.
#  *               / \\||| : |||// \
#  *             / _||||| -:- |||||- \
#  *               | | \\\ - /// | |
#  *             | \_| ''\---/'' | |
#  *              \ .-\__ `-` ___/-. /
#  *           ___`. .' /--.--\ `. . __
#  *        ."" '< `.___\_<|>_/___.' >'"".
#  *       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#  *         \ \ `-. \_ __\ /__ _/ .-` / /
#  * ======`-.____`-.___\_____/___.-`____.-'======
#  *                    `=---='
#  *
#  * .............................................
#  *          佛祖保佑             永无BUG
#  */

"""
Project:LS  

"""
__author__ = 'LS'

# encoding: utf-8

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt



comment = []
with open('test.txt', mode='r',encoding = 'gbk') as f:
    rows = f.readlines()
    for row in rows:
        if row not in comment:
            comment.append(row.strip('\n'))


def snowanalysis(self):
    sentimentslist = []
    with open('qinggan.txt', 'w+', encoding='utf8') as q:
        for li in self:
            s = SnowNLP(li)
            q.write(li + '\n')
            q.write(str(s.sentiments) + '\n\n')
            sentimentslist.append(s.sentiments)
        # print (li)
        # print  (s.sentiments)
        # print ('\n')
    #sentimentslist.append(s.sentiments)
    print ('情感文件分析完毕！')
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.05))
    #plt.hist(sentimentslist, bins=256, normed=1,edgecolor='None',facecolor='red')
    plt.show()

# def write(self):
#     for li in self:
#         s = SnowNLP(li)
#         with open('qinggan.txt','w+',encoding = 'utf8') as q:
#             q.write(li + '\n')
#             q.write(str(s.sentiments) + '\n\n')

    # print ('情感文件分析完毕！')

if __name__ == '__main__':
    #write(comment)
    snowanalysis(comment)
