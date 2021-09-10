from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)


# 코스닥 지수정보 20210908_14_index.csv
KOSDAQ = soup.find("em", id="now_value").text
print ("KOSDAQ : ", KOSDAQ)


# # 시황정보 뉴스 20210908_14_news.csv
SH = soup.find_all("ul", class_="sise_report")
SH_news = SH[0].find_all("span", class_="tit")
a = []
for i in SH_news :
    a.append(i.text)
print(a)
### 시황뉴스 csv로 만들기
dat = pd.DataFrame({"시황뉴스":a})
print(dat)
dat.to_csv("SHNews.csv",index=True)


# # 시황정보 리포트 20210908_14_report.csv
SH_report = SH[1].find_all("span", class_="tit")
b = []
for i in SH_report :
    b.append(i.text)
print(b)


# 인기검색어 20210908_14_pop.csv

# 가장 많이 본 뉴스 20210908_14_cnt_news.csv

