from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=134963&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=5"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

reviews = soup.find_all("div", class_="score_reple")
print(list(reviews)[0].span)