import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 붓꽃의 CSV 데이터 읽어 들이기 -- (*1)
csv = pd.read_csv('iris.csv')

# 필요한 열 추출하기 -- (*2)
# csv를 열 이름으로 분할, 현재 csv에는 가장 앞 행에 열 이름이 지정돼 있기에 이 이름을  사용해 원하는 열을 분할하는 것
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]

# 학습 전용 데이터와 테스트 전용 데이터로 나누기 -- (*3)
# train_test_split() 메서드를 사용해 훈련 전용 데이터와 학습 전용 데이터를 분할한다.
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

# 데이터 학습시키고 예측하기 -- (*4)
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 정답률 구하기 -- (*5)
ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 =", ac_score)