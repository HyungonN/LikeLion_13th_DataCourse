from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time

url_base = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=134963&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
comments = []
for i in range(1,50) :
    url = url_base + str(i)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup.title)

    reviews = soup.find_all("div", class_="score_reple")
    
    for one in reviews :
        comments.append(one.find_all('span')[1].text.strip())
    time.sleep(0.5)
print(comments)



dict_dat = {"영화댓글" : comments}
dat = pd.DataFrame(dict_dat)
dat.to_csv("영화댓글2.csv", index=False)
dat.to_excel("영화댓글2.xlsx",index=False)