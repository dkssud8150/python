import pandas as pd
from sklearn import svm, metrics

# xor 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
]

# 입력을 학습 전용 데이터와 테스터 전용 데이터로 분류하기 --(*1)
# pandas모듈의 dataFrame 기능을 사용
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.loc[:,0:1] # 데이터
xor_label = xor_df.loc[:,2] # 레이블

# 데이터 학습과 예측하기 --(*2)
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기 -- (*3)
# metrics.accuracy_score()함수를 사용하면 정답률을 이처럼 쉽게 구할 수 있다.
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)
