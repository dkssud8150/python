from bs4 import BeautifulSoup
import urllib.request as req
# HTML 가져오기
url = "https://finance.naver.com/marketindex/?tabSel=exchange"
res = req.urlopen(url)
# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
# 원하는 데이터 추출하기 --- (※1)
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)

# price = soup.select("div.head_info > span.value")
# for value in price:
#    print("used/krw =", price)
# >> used/krw = [<span class="value">1,184.50</span>, <span class="value">1,115.93</span>,,,