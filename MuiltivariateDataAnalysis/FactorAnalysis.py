# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:22:56 2022

@author: hjand

인자 분석(factor analysis)
### dataset : Positive Health Inventory(PHI)
### method : 주성분 인자법(principal factor method)
###실제로 인자분석을 이행할때는 그 분야에 대해 잘 알고 있어야 한다. 변수에대해서도 잘알고 분야에 대한 지식이 있어야 결과를 분석할 수 있다. 
"""

### 1. 자료 읽기 및 요약 통계량
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 데이터 읽기
med = pd.read_csv("c:/data/mva/medFactor.csv")
med.head(3)

# 기술통계량 구하기
med.describe()

#dos window -> pip install factor_analyzer
### 2. 초기 인자분석 실행하기

# 인자분석 적정성 검정 (추가)
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
chi_square_value,p_value=calculate_bartlett_sphericity(med)
chi_square_value, p_value # 기본적으로 파이썬의 값은 튜플로 보낸다
#(341.2089876475221, 6.4362758343486854e-43)
#p 값이 굉장히 작아서 귀무가설을 기각한다 ->유의하다
from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(med)
kmo_model #0.6840306201730828-> 인자분석을 해도 되겠구나, 유의성 검정 통과

# 초기 인자분석
from factor_analyzer import FactorAnalyzer
fa = FactorAnalyzer(rotation=None)
help(FactorAnalyzer)
# help(FactorAnalyzer): 클래스 코드 보기
fa.fit(med)
# 고윳값 구하기
ev, v = fa.get_eigenvalues()
ev

# 스크리 그림 그리기
plt.scatter(range(1, med.shape[1]+1), ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalues')
plt.grid()
plt.show()

### 3. varimax 인자회전
# 인자 수를 3으로 한 인자분석 – 인자회전 Varimax
fa_varimax = FactorAnalyzer(n_factors=3, rotation='varimax', method='principal')
fa_varimax.fit(med)
# 인자적재계수
fa_varimax.loadings_

# 인자 공통성(communality)
fa_varimax.get_communalities()

# 인자고유분산: 1-공통성
fa_varimax.get_uniquenesses()

# 인자분산
fa_varimax.get_factor_variance()

### 4. oblimin 인자회전
fa_obm = FactorAnalyzer(n_factors=3, rotation='oblimin', method='principal')
fa_obm.fit(med)
# 인자적재계수
fa_obm.loadings_

# 인자 공통성(communality)
fa_obm.get_communalities()

# 인자고유분산: 1-공통성
fa_obm.get_uniquenesses()

# 인자분산
fa_obm.get_factor_variance()
