#파일 읽기
import wordcloud
from wordcloud import WordCloud
from matplotlib import rc


f = open("영화댓글2.csv", encoding = "utf-8")
text = f.read()
#print(text)
f.close()

rc('font', family = "NanumGothic")

wcloud = WordCloud("./D2Coding.ttf",
                   max_words=100,
                   relative_scaling=0.2).generate(text)


import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))
plt.imshow(wcloud, interpolation = "bilinear")
plt.axis("off")
plt.savefig( 'myfig.png' )
plt.show()