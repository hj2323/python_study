###########################
### 주성분 분석
###########################

### 1. 자료 가져오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
heptathlon = pd.read_csv('/Users/hj1/Desktop/mva/heptathlon.csv')
heptathlon = pd.read_csv('C:/data/mva/heptathlon.csv')

# 기술통계량 구하기 - 소수점 이하 2자리 반올림 표시
round(heptathlon.describe(), 2)

### 2. 변수변환 및 변수 표준화
# 변환: 변수최댓값 - 변숫값
heptathlon.hurdles = np.max(heptathlon.hurdles) - heptathlon.hurdles
heptathlon.run200m = np.max(heptathlon.run200m) - heptathlon.run200m
heptathlon.run800m = np.max(heptathlon.run800m) - heptathlon.run800m

# 분석변수 선택하기
feature = ['hurdles', 'highjump', 'shot','run200m','longjump', 'javelin', 'run800m']
hep_data = heptathlon[feature]
# hep_data = heptathlon.iloc[:, 1:8] # 모든 케이스에 대해서 1부터 8까지 
# hep_data = heptathlon.iloc[:, 1:-1] #[1:-1] -1이 마지막열이라는 것을 나타내줌

# 변수 표준화
from sklearn.preprocessing import StandardScaler
x = StandardScaler().fit_transform(hep_data)

### 3. 초기 주성분 분석
from sklearn.decomposition import PCA
pca_init = PCA(n_components = len(hep_data.columns))
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
hep_pca = pca.fit_transform(x)

pca.explained_variance_

pca.explained_variance_ratio

# 주성분계수
np.round(pca.components_, 3)

# 주성분 점수
hep_pca[0:5, :]



