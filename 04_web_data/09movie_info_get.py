from bs4 import BeautifulSoup
from urllib.request import urlopen

# url 정보
# Tag, id, class 정보

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")

print(soup.title)
#영화 제목
Moviename = soup.find_all("dt", class_ = "tit")
allnames = []
for one in Moviename :
    Mnames = one.find("a")
    allnames.append(Mnames.text)
#print(allnames)

# 영화평점
Moviescore_1 = soup.find_all("dl", class_="info_star")
allscore = []
for one in Moviescore_1 :
    a = one.find("span", class_="num")
    allscore.append(a.text)
#print(allscore)

movieset = []
for i in range(len(allnames)) :
    movieset.append((allnames[i],allscore[i]))
#print(movieset)

# 예매율
Movierate_1 = soup.find_all("div", class_="star_t1 b_star")
allrate = []
for one in Movierate_1 :
    a = one.find("span", class_="num")
    allrate.append(a.text)
#print(allrate)

# 평점 참여명수
Movieman = soup.find_all("dl", class_="info_star")
allman = []
for one in Movieman:
    a = one.find("em")
    allman.append(a.text)
#print(allman)


import pandas as pd
#allnames, allscore, allrate, allman
dict_dat = { "영화제목":allnames,
             "평점": allscore,
             "참여명수": allman
             }
dat = pd.DataFrame(dict_dat)
print(dat)
dat.to_csv("naver_movie_info.csv", index=False)
dat.to_excel("naver_movie_info.xlsx", index=False)