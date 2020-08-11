from sklearn import svm

# XOR의 계산 결과 데이터 --(*1)
# xor 연산의 입력과 결과를 2차원 리스트로 정의
xor_data = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
]

# 학습을 위해 데이터와 레이블 분리하기 --(*2)
# 입력을 학습시키기 위한 데이터 변수와 정답 레이블 변수로 나눈다.
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

# 데이터 학습시키기 -- (*3)
# svm이라는 알고리즘을 사용해 머신러닝을 수행, svm객체를 만들고, fit()메서드를 사용해 데이터를 학습시킨다.
# fit() 메서드는 첫번째 매개변수로 학습할 데이터 배열을, 두번째 매개변수로 레이블 배열을 전달한다.
clf = svm.SVC()
clf.fit(data, label)

# 데이터 예측하기 -- (*4)
# 학습한 결과를 기반으로 데이터를 예측
# predict()메서드에 예측하고 싶은 데이터 배열을 전달하면 데이터 수만큼 예측 결과를 리턴해준다.
# 둘 중 하나만 참이고, 하나는 거짓일 때 참으로, 둘다 참이거나 둘다 거짓이면 거짓으로 나온다. [거짓, 참, 참, 거짓]
pre = clf.predict(data)
print("예측결과:", pre)

# 결과 확인하기 -- (*5)
# for 반복문을 사용해 하나하나의 예측결과가 맞는지 확인하고 정답률을 계산
ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
        total += 1
print("정답률:", ok, "/", total, "=", ok/total)
