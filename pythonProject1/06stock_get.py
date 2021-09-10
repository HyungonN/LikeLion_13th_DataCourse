from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"

page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

#코스피 지수
kospi_info = soup.find("em", id ="now_value")
print(kospi_info.text)

#거래량 천주 정보
deal_info = soup.find("td", id="quant")
print("거래량 :", deal_info.text)
#최고거래
deal_max = soup.find("td", id="high_value")
print("장중 최고 :", deal_max.text)

#투자자별 매매 동향

investor_program_info = soup.find("dl", class_="lst_kos_info")
investor_shell_info = investor_program_info.find_all("dd", class_="dd")

print(investor_shell_info)