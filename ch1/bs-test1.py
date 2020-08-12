# 라이브러리 읽어 들이기 --- (※1)
from bs4 import BeautifulSoup
# 분석하고 싶은 HTML --- (※2)
html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""
# HTML 분석하기 --- (※3)
soup = BeautifulSoup(html, 'html.parser')
# python 내장 html.parser 을 사용, 분석에 용이하게 변환

# 원하는 부분 추출하기 --- (※4)
h1 = soup.html.body.h1
# body에 있는 h1 태그를 찾아 h1 객체에 넣는다.
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
# next_sibling을 두번 쓴 이유는 한번만 쓰면 닫는 태그인 </p> 태그를 찾아간다.
# .next_sibling을 한번만 쓰면 '</p>뒤에 있는 공백이나 줄바꿈이 출력된다.

# 이전으로 찾아가려면 previous_sibling을 이용한다.

# 요소의 글자 출력하기 --- (※5)
print("h1 = " + h1.string)
print("p  = " + p1.string)
print("p  = " + p2.string)