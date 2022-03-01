# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:48:48 2022

@author: hjand
"""

import numpy as np
import pandas as pd
# read data
survey = pd.read_csv("c:/data/mva/survey.csv")
survey.head(3)

# mean
survey["age"].mean()

# sd
survey["age"].std()

# 범주형 변수로 변환하기
survey["sex"] = survey["sex"].astype("category")
survey["job"] = survey["job"].astype("category")
survey["edu"] = survey["edu"].astype("category")
survey.marriage = survey.marriage.astype("category")

# 연속인 변수의 기술통계량 구하기
survey.iloc[:, 1:].describe()

# 나이에 대한 (성별, 결혼상태, 성별x결혼상태) 평균 및 표준편차
agestat_by_sex = survey.groupby("sex")["age"].describe()
agestat_by_sex

agestat_by_sex["mean"] # 표준편차 : std

#(sex, marriage)를 그룹으로 age의 기술통계량 구하기
agestat_by_sex_marriage = survey.groupby(["sex","marriage"])["age"].describe()
agestat_by_sex_marriage

agestat_by_sex_marriage["mean"] # 표준편차:std

# 분할표
sex_freq = pd.crosstab(index=survey.sex, columns='count')
sex_freq

# (sex, edu)의 분할표 구하기
sex_edu_table = pd.crosstab(index=survey.sex, columns=survey.edu)
sex_edu_table

# (sex, edu)의 분할표 - 카이제곱 검정
from scipy.stats import chi2_contingency

chi2_contingency(sex_edu_table)
