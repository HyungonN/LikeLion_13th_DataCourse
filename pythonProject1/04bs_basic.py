from urllib.request import urlopen
from bs4 import BeautifulSoup


page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''
url = "https://www.naver.com"
page2 = urlopen(url)



soup = BeautifulSoup(page, "lxml")
#print(soup.title)

# print(soup.body)
# print(soup.div)
# print(soup.img)
#print(soup.a.text)
# print(type(soup.find("p")))
print(soup.find_all("p", class_="p3")[1].text)
print(soup.find_all("a")[1].text)