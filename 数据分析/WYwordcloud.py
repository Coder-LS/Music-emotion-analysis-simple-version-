import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

l = ''
f = open('1293886117.txt', 'r',encoding = 'utf8')
for i in f:
    l += f.read()

result = jieba.analyse.textrank(l, topK=250, withWeight=True)
keyworlds = dict()
for i in result:
    keyworlds[i[0]] = i[1]

# print(keyworlds)

image = Image.open('lironghao.jpg')
graph = np.array(image)
wc = WordCloud(font_path='msyh.ttc', background_color='White', max_font_size=50,max_words=300,mask = graph)
wc.generate_from_frequencies(keyworlds)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis('off')
plt.show()
wc.to_file('8.jpg')
