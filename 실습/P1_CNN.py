# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:14:15 2020

@author: WITLab
"""

# baseline cnn model for mnist
from numpy import mean  # 평균치
from numpy import std  # 표준편차
from matplotlib import pyplot as plt  # 그림 도시
from keras.datasets import mnist  # 데이터 셋
from keras.utils import to_categorical  # one hot encoding
from keras.models import Sequential  # 모델 유형 (레이어 연속)
from keras.layers import Conv2D  # Conv 레이어
from keras.layers import MaxPooling2D  # MaxPool레이어
from keras.layers import Flatten  # Flatten 레이터
from keras.layers import Dense  # Dense(ANN) 레이터
from keras.optimizers import SGD  # 손실함수 최소기법 (Stochastic gredient descent)

# %%
# load train and test dataset                              # mnist로부터 데이터 셋 로드
(trainX, trainY), (testX, testY) = mnist.load_data()
# summarize loaded dataset      # 데이터 셋 정보(dimension)
print('Train: X=%s, y=%s' % (trainX.shape, trainY.shape))
print('Test: X=%s, y=%s' % (testX.shape, testY.shape))
# plot first few images
for i in range(9):  # 입력 샘플 데이터 가시화
    # define subplot
    plt.subplot(330 + 1 + i)
    # plot raw pixel data
    plt.imshow(trainX[i], cmap=plt.get_cmap('gray'))
# show the figure
plt.show()
# %%
# reshape dataset to have a single channel             # 입력 데이터 dimension 조정 ( 갯수 감안 28 x 28 -> 28 x 28 x 1(채널수, 흑백) )
trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
testX = testX.reshape((testX.shape[0], 28, 28, 1))
# one hot encode target values
trainY = to_categorical(trainY)  # 츨력 데이터 one hot encoding
testY = to_categorical(testY)
# convert from integers to floats
trainX = trainX.astype('float32')  # 입력 데이터 유형 float로 변환
testX = testX.astype('float32')
# normalize to range 0-1
trainX = trainX / 255.0  # 입력 0~1로 범위 조정
testX = testX / 255.0
# %%
# define cnn model

model = Sequential()  # 모델 유형을 레이어 연속으로
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))  # Conv 레이더
model.add(MaxPooling2D((2, 2)))  # MaxPool 레이어
model.add(Flatten())  # Flatten 레이어
model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))  # ANN 레이어
model.add(Dense(10, activation='softmax'))  # ANN 레이어
model.summary()  # 파라미터 요약
# compile model
opt = SGD(lr=0.01, momentum=0.9)  # 최적화 기법
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])  # 모델 완성 및 컴파일

# %%
history = model.fit(trainX, trainY, epochs=10, batch_size=64, verbose=1)  # 모델 학습
# %%
import numpy as np  # numpy를 np 호출

# %% Predict the probability distribution for number between 0-9
Predicted = model.predict(testX)  # 모델 시험
# get the number with maximum probability
PredY_class = np.argmax(Predicted, axis=1)  # 0~9 중 확률치가 최대치인 값 선택
# Convert predictions classes to one hot vectors
# %%
for i in range(9):  # 샘플 결과 가시화
    # define subplot
    plt.subplot(330 + 1 + i)
    # plot raw pixel data
    plt.imshow(testX[i].reshape(28, 28), cmap=plt.get_cmap('gray'))
    plt.title('Predicted label {}'.format(PredY_class[i]))
# show the figure
plt.show()
# %%


