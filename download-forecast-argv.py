#!/usr/bin/env python3

# 라이브러리를 읽어 들입니다. --- (※1)
import sys
import urllib.request as req
import urllib.parse as parse

# 명령줄 매개변수 추출 --- (※2)
if len(sys.argv) <= 1:
    # sys.argv = 파이썬 스크립트로 넘어온 입력인자들의 리스트
    # sys.argv[0]에는 스크립트의 이름, sys.argv[1] 이후에는 명령줄 매개변수가 설정
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
    # sys.exit = 강제로 스크립트 종료하기
regionNumber = sys.argv[1]

# 매개변수를 URL 인코딩합니다. --- (※3)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

# 다운로드합니다. --- (※4)
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)

