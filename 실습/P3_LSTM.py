#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:23:17 2019

@author: WITLab
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:04:01 2019

@author: navin
"""
# import required package 
import numpy as np                          # numpy 모듈 np로 호출
import pandas as pd                         # pandas 모듈 pd로 호출
import matplotlib.pyplot as plt             # matplot 모듈 plt로 호출
import keras                                # Keras 모듈 호출
from keras.models import Sequential         # Keras 모델 중 Sequmetial 호출
from keras.layers import Dense, LSTM        # Dense, LSTM 호출
#%%

df=pd.read_csv('P3_Input_CI.csv')           # CSV화일 열기

df=df['CI_seoul_in']                        # 'CI_seoul_in' 컬럼 추출
df=pd.DataFrame(df)                         # 새로운 데이터프레임으로 정의
df.columns=['Ci']                           # 컬럼 이름을 변경(CI_seoul_in --> Ci)
# since it is Time series prediction 
# train test split 80:20 ratio
train = df['Ci'][0:13825]                   # 학습 데이터 할당
test = df['Ci'][13825:17280]                # 시험 데이터 할당 
#%%

#plot input dataset
plt.figure(figsize=(18,8))                  # 그림 크기
plt.plot(df)                                # 데이터 도시
ticks=[i*1440 for i in range (0,13)]        # 그림에서 X축 값 표시 지점
labels=[str(i) for i in range(1,14)]        # 그림에서 X축 값 [1, 2, 3,...,13] --> day 
plt.xticks(ticks, labels)                   # 그림에 표시
plt.xlabel('Day')                           # 그림 X축 이름(단위)
plt.ylabel('Congestion Index')              # 그림 Y축 이름(단위)
plt.grid()                                  # 그림에 grid표시
plt.show()                                  # 도시
#%%


n_step=120                                  # 입력 샘플수
x_train, y_train = [], []                   # 변수 설정

#create the sequence of Input and output for Train data
for i in range(n_step,len(train)-20):
    x_train.append(train[i-n_step:i])       # 입력값에 대한 인덱스 ([0:119],[1:120],[2:121],...)
    y_train.append(train[i+20])             # 출력값에 대해나 인덱스 --> (120+20)} :(140,141,142,.....)
#%%

# Reshape to 3 dimension to work with LSTM model
x_train, y_train = np.array(x_train), np.array(y_train)              # 변수를 어레이로 전환
x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1)) # 입력 샘플수, 샘플당 변수(120), 변수의 차수 등으로 형태 변환
#%%

# create the LSTM network
model = Sequential()
model.add(LSTM(units=100, activation='relu', return_sequences=True, input_shape=(x_train.shape[1],1)))    # LSTM layer
model.add(LSTM(units=100, activation='relu'))                                                             # LSTM layer
model.add(Dense(1))                                                                                       # Dense (ANN) layer
model.compile( optimizer='adam',loss='mse',)                                                              # Compiler 
model.summary()                                                                                           # summary of the model

# Train the model 
model.fit(x_train, y_train, epochs=5 ,batch_size=100, verbose=1)                                          # Model train

# Create of Input sequence for Test data
X_test = []
y_test=[]
for i in range(n_step,len(test) ):                    # 시험 입력 데이터 X_test ([13825:13825+120],[13826:13826+20],...)
    X_test.append(test[i-n_step:i])  
X_test = np.array(X_test)                             # 시험 입력 데이터를 어레이로 변환
X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))   # 입력 샘플수, 샘플당 변수(120), 변수의 차수 등으로 형태 변환


y_test=test[140:]                                     # 시험 출력 범위 (120+ 20)
y_test=np.array(y_test)                               # 어레이로 변환

CI_per = model.predict(X_test)                        # 모델 시험
ci=CI_per.reshape(CI_per.shape[0])                    # (total sample,1 --> total sample) 단일 차수로 변환
 
#%%
#Calculating Error
mse=(np.mean(np.power((y_test-CI_per),2)))           # mean square error 계산
rms=np.sqrt(np.mean(np.power((y_test-CI_per),2)))    # root mean square error 계산
print(mse)
print(rms)
#%%
ci=pd.DataFrame(CI_per)                              # 예측치 결과표 생성
ci.columns=['Pred']                                  # 이름 재설정
ci.shape

#%%

train1 =df['Ci'][:13825]                             #train data                   
test1 = df['Ci'][13825:17280]                        #test data 
pred=ci['Pred'][:]                                   #predicted data

#Visualization of result 
plt.figure(figsize=(16,8))
#plot function
x=[i for i in range(0,17300)]                                        # X-axis positions 
plt.plot(x[:13825],train, label='train')                             # plot train data from 0 to 13825 X-axis position
plt.plot(x[13825:17280],test, label='actual_test')                   # plot test data from 13825 to 17280 X-axis position
plt.plot(x[13825+140:17300 ],pred, label='LSTM_predicted_test')      # plot test data from 13825+140 to 17280+140 X-axis position
#postion to place the label in X-axis
ticks=[i*1440 for i in range (0,13)]                                 # define label location along X-axis, after each 1440 i.e., 1 day 

labels=[str(i) for i in range(0,13)]                                 # name of label [1, 2, 3,..., 13]
plt.xticks(ticks, labels)                                            # print day number along X-axis 
plt.grid()                                                           # display gridlines
plt.title('LSTM model Prediction')                                   # title of the figure
plt.xlabel('Day')                                                    # X-axis data label
plt.ylabel('Congestion Index')                                       # Y-axis data label
plt.legend()                                                         # display the line color: line name 
plt.show()                                                           # show figure
#%%

#Visualization of test and predicted data 

plt.figure(figsize=(16,8))
plt.plot(x[13825:17280], test1,label='actual_test data')            
plt.plot(x[13825+120:17280 ], pred, label='LSTM_predicted data')    
ticks=[i*1440 for i in range (10,13)]
labels=[str(i) for i in range(10,13)]
plt.xticks(ticks, labels)
plt.grid()
plt.title('LSTM model Forecast')
plt.xlabel('Day')
plt.ylabel('Congestion Index')
plt.legend()
plt.show()
#%%


# In[ ]:




