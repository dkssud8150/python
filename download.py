import urllib.request
import urllib.parse

# API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
API = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"
values = {                     #dictionary 자료형 : key-value 쌍
    'zone' : '281858200'
}
# 매개변수 작성: <key> : <value>


params = urllib.parse.urlencode(values)
# 매개변수는 urlencode함수로 인코딩해야 함.
# urlencode() = url코드로 바꾸어준다.

url = API + "?" + params
print("url = ", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
# --------------------------------------------------------------------

import urllib.request
import urllib.parse

# API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
API = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"
values = {                     #dictionary 자료형 : key-value 쌍
    'stnId' : '108' "&" '20200723'
}
# 매개변수가 여러 개일 경우 "&"로 구분

params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url = ", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)