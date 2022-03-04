# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:13:31 2022

@author: hjand
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 데이터 읽기
survey = pd.read_csv("c:/data/mva/survey.csv")
# 빈도수 구하기
edu_freq = pd.crosstab(index = survey.edu, columns = 'count')
edu_freq

# 케이스 라벨 지정하기
edu_freq.index = ["none", "elementary", "middle", "high", "college"]

# 막대그림 그리기
plt.bar(edu_freq.index, edu_freq["count"])

# 원그림 그리기
plt.pie(edu_freq["count"], labels=edu_freq.index)

# 파이썬 겹친막대그림
# (edu, sex) 분할표 구하기
edu_sex_tb = pd.crosstab(index=survey.edu, columns=survey.sex)
edu_sex_tb

# 케이스 및 변수이름 지정하기
edu_sex_tb.index = ["none", "elementary", "middle", "high", "college"]
edu_sex_tb.columns = ["Male", "Female"]
edu_sex_tb

# 겹친 막대그림 그리기
edu_sex_tb.plot.bar(stacked=True)

# 파이썬 한 화면에 여러 개의 그림 그리기
plt.figure()
plt.subplot(121)
plt.bar(edu_freq.index, edu_freq["count"])
plt.subplot(122)
plt.pie(edu_freq["count"], labels=edu_freq.index)

# 히스토그램 그리기
import matplotlib.pyplot as plt
plt.hist(survey["salary"])

# 줄기-잎 그림 그리기
# pip install stemgraphic (in DOS prompt)
import stemgraphic
stemgraphic.stem_graphic(survey.salary, scale=50)

# 파이썬 상자그림
import seaborn as sns
sns.boxplot(x="sex", y="salary", data=survey)


###############################
# 파이썬 이변량 그래프
###############################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 데이터 읽기
co2 = pd.read_csv("c:/data/mva/co2.csv")
co2.head(2)

# 변수이름 지정하기
co2.columns = ["seq", "x"]
co2.head(2)

# 선그리기
plt.plot(co2.seq, co2.x)
# plot of mathematical functions
x = np.arange(0,20,0.1)
y = np.exp(-x/10)*np.cos(2*x)
plt.plot(x,y)


# 데이터 읽기
USairpollution = pd.read_csv("c:/data/mva/USairpollution.csv")
USairpollution.head(3)

# SO2 변숫값 * 5
USairpollution["SO2"] = USairpollution["SO2"] * 5

# 버블차트 그리기
plt.scatter('temp', 'wind', s='SO2', alpha=0.9, data=USairpollution)
plt.xlabel("temp", size=16)
plt.ylabel("wind", size=16)
plt.title("Bubble plot")

###############################
# 파이썬 산점도 행렬
###############################
import pandas as pd
# 데이터 읽기
social = pd.read_csv("c:/data/mva/social.csv")

# (행의 수, 열의 수)
social.shape

# seaborn을 이용하여 산점도 행렬 그리기
import seaborn as sns
sns.pairplot(social)

# 상관계수 행렬 구하기 - 소수점 이하 3자리 반올림
round(social.corr(), 3)

# 파이썬 iris 산점도 행렬
iris = sns.load_dataset("iris")
iris.head()
# species로 구분된 산점도행렬 그리기 - 대각선은 각 그룹별 분포
sns.pairplot(iris, hue='species', height=2.5)
