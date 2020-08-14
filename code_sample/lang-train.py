from sklearn import svm, metrics
import glob, os.path, re, json

# 텍스트를 읽어 들이고 출현 빈도 조사하기 --- (※1)
def check_freq(fname):
    name = os.path.basename(fname)
    # os.path.basename(path) = 입력받은 경로의 기본이름=원래이름(basename)=fname을 반환
    lang = re.match(r'^[a-z]{2,}', name).group()
    # re.match('정규표현식 패턴', '텍스트') = 텍스트에서 정규 표현식 패턴에 해당하는 값을 찾음
    # re.compile('정규 표현식 패턴') = 정규 표현식 패턴에 해당하는 패턴 객체 생성
    # search = 텍스트에서 찾음, findall = 패턴에 해당하는 값을 찾아서 리스트로 반환
    # spilt = 해당하는 값을 찾아서 부분 문자열로 자르고 리스트로 반환, sub = 해당하는 값을 찾아서 바꿀 글자로 바꾼다.
    with open(fname, "r", encoding="utf-8") as f:
    # with open()으로 파일을 읽으면 exception 발생해도 닫아줌
    # fname 이라는 데이터를 불러와 f에 저장
        text = f.read() # 텍스트를 불러옴23
    text = text.lower() # 소문자 변환

    # 숫자 세기 변수(cnt) 초기화하기
    cnt = [0 for n in range(0, 26)]
    # for in list = 코드를 필요한만큼 반복해서 실행, 순회할 리스트가 정해져 있을 때 사용
    # for in range = 순회할 횟수가 정해져 있을 때 사용, 시작 숫자를 지정해주지 않으면 0부터 시작,
    # range(0, 2) = 시작과 끝, 끝 숫자는 포함x, range(1, 10, 3) = 세번째 숫자는 숫자 사이의 거리를 말한다.
    code_a = ord("a")
    code_z = ord("z") # ord() = 문자를 정수로 반환하는 것

    # 알파벳 출현 횟수 구하기 --- (※2)
    for ch in text: # text 함수를 for문 하여 ch에 넣는다.
        n = ord(ch)
        if code_a <= n <= code_z: # a~z 사이에 있을 때
            cnt[n - code_a] += 1

    # 정규화하기 --- (※3)
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    # map(function, itarable) = 함수와 파라미터를 맵핑해줌 func = return*2 => map(func,[1,2] = [2,4]
    # lambda 인자 : 표현식
    # [i for i in a if i>4] = filter(lambda x: x>4,a)
    # list(map(lambda x:x+2, range(2))) = [2,3]
    return (freq, lang)
    
# 각 파일 처리하기
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    # glob = 파일들의 리스트를 뽑을 때 사용, 파일의 경로명을 이용해서 불러옴, glob lib의 glob함수
    # glob.glob('./[0-9].txt') = ['./1.txt','./2.txt'...]
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        # append = r[0] 자체를 원소로 freqs에 추가한다. extend = r[0]를 iterable의 각 항목 들을 넣는다.
        # x.append(y) = [... , ['funck', 'finck']], x.extend(y) = [... , 'funck', finck']
        # y= funck일때 append = [... , 'funck'], extend = [... , 'f', 'u',...,'k']
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}
data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")

# 이후를 대비해서 JSON으로 결과 저장하기
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)
    # ./lang/freq.json 이름의 파일을 쓰기(w)모드로 열어놓고 json.dump로 직렬화해서
    # json으로 내보내고자 하는 객체 [data,test]를 직렬화된 데이터가 쓰여질 파일 fp에 쓰기 = fp.json

# 학습하기 --- (※4)
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 예측하기 --- (※5)
predict = clf.predict(test["freqs"])

# 결과 테스트하기 --- (※6)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)

