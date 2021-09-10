from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"

page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

tmp_news = soup.find_all("ul", class_="sise_report")
tmp_li_all = tmp_news[0].find_all("span", class_="tit")

news = []
for one in tmp_li_all:
    news.append(one.text)
    print(one.text)


#시황정보 리포트
import pandas as pd
dat = pd.DataFrame( {"시황뉴스":news})
print(dat)
dat.to_csv("news.csv", index=True)

dat.to_excel("news.xlsx", index=False)