from bs4 import BeautifulSoup

soup = BeautifulSoup( "<p><a href='a.html'>test</a></p>", "html.parser")

# 분석이 제대로 됐는지 확인하기 -- (*1)
soup.prettify()

# <a>태그를 변수 a에 할당
a = soup.p.a

# attrs 속성의 자료형 확인 -- (*2)
type(a.attrs)
# dict = 딕셔너리 = 자료형

# href 속성이 있는지 확인
'href' in a.attrs
# true

# href 속성값 확인
a['href']
# 'a.html'