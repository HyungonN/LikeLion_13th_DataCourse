print("test")

from urllib.request import urlopen
from bs4 import BeautifulSoup


### 우리가 가져올 URL
### 내가 원하는 정보의 위치(span, id)
### url : https://finance.naver.com/sise/
### tag : <span id="KOSPI_now">


url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)

### 구체적인 html 확인하고, 구조화
soup1 = BeautifulSoup(page, "html.parser")
KOSPI = soup1.find("span", id="KOSPI_now")
KOSDAQ = soup1.find("span", id="KOSDAQ_now")
KOSPI200 = soup1.find("span", id="KPI200_now")

top10 = soup1.find("ul", id="popularItemList")
print("KOSPI지수 : ", KOSPI.text)
print("KOSDAQ지수 : ",KOSDAQ.text)
print("KOSPI200지수 : ",KOSPI200.text)
print(top10.text)