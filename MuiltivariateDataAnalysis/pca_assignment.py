# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:25:29 2022

@author: hjand

주성분 분석 과제
"""

### 1. 자료 가져오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
USArrests = pd.read_csv('C:/data/mva/USArrests.csv')
# 기술통계량 구하기 - 소수점 이하 2자리 반올림 표시
round(USArrests.describe(), 2)


### 2. 변수 표준화
# 분석변수 선택하기
feature = ['Murder', 'Assault', 'UrbanPop','Rape']
USArr_data = USArrests[feature]

# 변수 표준화
from sklearn.preprocessing import StandardScaler
x = StandardScaler().fit_transform(USArr_data)

### 3. 초기 주성분 분석
from sklearn.decomposition import PCA
pca_init = PCA(n_components = len(USArr_data.columns))
pca_init.fit(x)
pca_init.explained_variance_

# 스크리 그림 그리기
plt.title('Scree Plot')
plt.xlabel('Components')
plt.ylabel('Explained Variance')
plt.plot(pca_init.explained_variance_, 'o-')
plt.show()


### 4. 주성분 분석 - 주성분 수 2
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
USArr_pca = pca.fit_transform(x)
pca.explained_variance_

#주성분 분산 비율
pca.explained_variance_ratio_

# 주성분계수
np.round(pca.components_, 3)

# 주성분 점수
USArr_pca[0:7, :]




















