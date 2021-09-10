from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


url1 = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page=1"
comments = []
basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page="

for i in range(1,6) :
    realurl = basic_url+str(i)
    page = urlopen(realurl)
    soup = BeautifulSoup(page, "html.parser")
#print(soup.title)

    reviews = soup.find_all("td", class_="title")
    #dat = list(reviews[0].children)[6].replace('\n',"")
    #dat = dat.replace('\t',"")
    #dat_comment = list(reviews[0].children)[6].strip()
    #print(dat_comment)


    for one in reviews:
        review = list(one.children)[6].strip()
        comments.append(review)

    #print(comments)
    #for i in range(len(reviews)) :
    #    dat = list(reviews[i].children)[6].strip()
    #    print(dat)

    dict_dat = {"영화댓글" : comments}
    dat = pd.DataFrame(dict_dat)
    dat.to_csv("영화댓글2.csv", index=False)
    dat.to_excel("영화댓글2.xlsx",index=False)



