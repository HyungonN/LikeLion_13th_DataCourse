from selenium import webdriver

url = "http://news.naver.com"
driver = webdriver.Chrome("./chromedriver")
driver.get(url)

# 검색 입력창 x-path : //*[@id="lnb.searchForm"]/fieldset/input[1]
# 검색버튼 x-path : //*[@id="lnb.searchForm"]/fieldset/button
sel_search = driver.find_element_by_xpath('//*[@id="lnb.searchForm"]/fieldset/input[1]')
sel_button = driver.find_element_by_xpath('//*[@id="lnb.searchForm"]/fieldset/button')

#검색시키기
sel_search.send_keys("네이버")
sel_button.click()


from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

url = 'https://www.amazon.com/HP-24-inch-Computer-Processor-24-dd0010/dp/B0849GZCQR/ref=sr_1_2?dchild=1&keywords=computer&qid=1631254252&sr=8-2'
driver.get(url)
current_url = driver.current_url
all_review =[]

viewall= driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')
viewall.click()

reviewpage = driver.page_source

soup = BeautifulSoup(reviewpage, 'lxml')
reviewtext = soup.find_all("span", class_= "a-size-base review-text review-text-content")
for one in reviewtext :
    tmp = one.text.strip()
    all_review.append(tmp)
    
#print(len(all_review))    
#print(all_review)
nextpage = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
nextpage.click()

reviewpage = driver.page_source
soup = BeautifulSoup(reviewpage, 'lxml')
reviewtext = soup.find_all("span", class_= "a-size-base review-text review-text-content")
for one in reviewtext :
    tmp = one.text.strip()
    all_review.append(tmp)

#print(len(all_review))

import pandas as pd
dict_review = {"아마존 컴퓨터 리뷰": all_review}
dat = pd.DataFrame(dict_review)
dat.to_csv("아마존 컴퓨터리뷰.csv", index= False)