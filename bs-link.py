from bs4 import BeautifulSoup 
html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
  </ul>
</body></html>
"""
# HTML 분석하기 --- (※1)
soup = BeautifulSoup(html, 'html.parser')

# find_all() 메서드로 추출하기 --- (※2)
links = soup.find_all("a")
# find_all("a"). 앵커<a>태그가 붙은 모든 것을 찾기
# soup.find_all(re.complie('^b')) = b로 시작하는 모든 태그를 찾는다.

# 링크 목록 출력하기 --- (※3)
for a in links:
    href = a.attrs['href']
    # css 클래스를 입력하면 해당 클래스를 갖는 데이터를 리턴한다.
    text = a.string
    # string = 문자열
    print(text, ">", href)

