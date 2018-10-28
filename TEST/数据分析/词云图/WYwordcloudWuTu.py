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
Date:2018/10/11
QQ:1217750958
"""
__author__ = 'LS'

import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

l = ''
f = open('37196629.txt', 'r',encoding = 'utf8')
for i in f:
    l += f.read()

result = jieba.analyse.textrank(l, topK=250, withWeight=True)
keyworlds = dict()
for i in result:
    keyworlds[i[0]] = i[1]

# print(keyworlds)

# image = Image.open('lironghao.jpg')
# graph = np.array(image)
wc = WordCloud(font_path='msyh.ttc', background_color='White', max_font_size=50,max_words=300)#mask = graph)
wc.generate_from_frequencies(keyworlds)
#image_color = ImageColorGenerator(graph)
plt.imshow(wc)
#plt.imshow(wc.recolor(color_func=image_color))
plt.axis('off')
plt.show()
wc.to_file('1.jpg')
