# bs-select

from bs4 import BeautifulSoup

# 분석 대상 HTML -- (*1)
html = """
<html>
    <body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
            <ul class="items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
    </body>
</html>
"""

# HTML 분석하기 -- (*2)
soup = BeautifulSoup(html, 'html.parser')

# 필요한 부분을 CSS 쿼리로 추출하기
# 타이틀 부분 추출하기 -- (*3)
h1 = soup.select_one("div#meigen > h1").string
# soup.select_one(선택자) = CSS 선택자로 요소 하나를 추출합니다.
print("h1 =", h1)

# 목록 부분 추출하기 -- (*4)
li_list = soup.select("div#meigen > ul.items > li")
# soup.select(선택자) = CSS 선택자로 요소 여러 개를 리스트로 추출합니다.
# soup.select(내가 원하는 조건) => 조건들 1.태그명 2.클래스명 3.id 4.속성값
# li => 모든 <li ~~>가 다 나오기 때문에 soup.select(li)하면 3개가 지정됨, soup.select(soup)[0]
# soup.select(상위태그명.클래스명>하위태그명) = 바로 아래의 태그를 선택시에는 > 기호를 사용
# soup.select(.클래스명), soup.select(#아이디명), soup.select('태그명[속성1=값1]')

for li in li_list:
    print("li =", li.string)