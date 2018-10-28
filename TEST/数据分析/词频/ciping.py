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

import jieba

article = open('37196629.txt','r',encoding = 'utf8').read()
dele = {'。','！','？','的','“','”','（','）',' ','》','《','，'}
jieba.add_word('不为谁而作的歌')
words = list(jieba.cut(article))
articleDict = {}
articleSet = set(words)-dele
for w in articleSet:
    if len(w)>1:
        articleDict[w] = words.count(w)

articlelist = sorted(articleDict.items(),key = lambda x:x[1], reverse = True)


with open('ciping.txt','w+') as f:
    for i in range(30):
        f.write(str(articlelist[i]) + '\n')
        

   # print(articlelist[i])

print ("词频分析完毕！")