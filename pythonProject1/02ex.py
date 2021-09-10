from urllib.request import urlopen
from bs4 import BeautifulSoup

# url https://finance.naver.com/sise/
# tag, id, class
# 다우산업지수 dd, class : point_status
# , 나스닥 종합, S&P 500


url = "https://finance.naver.com/sise/"
page = urlopen(url)
soup2 = BeautifulSoup(page, "html.parser")
print(soup2.title)

data = soup2.find("span", class_="up")

print(data.text)


