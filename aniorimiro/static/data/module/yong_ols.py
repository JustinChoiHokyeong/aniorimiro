# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='malgun gothic') # 한글 깨짐 방지
import warnings
warnings.filterwarnings(action='ignore')# 경고출력안하기
import time
import scipy.stats as stats
from sklearn.preprocessing import LabelEncoder
import statsmodels.formula.api as smf

# # Colab 한글 깨짐 현상 방지
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

pd.options.display.float_format = '{:.5f}'.format
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# 데이터 불러오기
df2019 = pd.read_csv('../re_preprocess/sangdata/서울시_우리마을가게_상권분석서비스(신_상권_추정매출)_2019년.csv', encoding='euc-kr')
df2020 = pd.read_csv('../re_preprocess/sangdata/서울시_우리마을가게_상권분석서비스(신_상권_추정매출)_2020년.csv', encoding='euc-kr')
df2021 = pd.read_csv('../re_preprocess/sangdata/서울시_우리마을가게_상권분석서비스(신_상권_추정매출)_2021년.csv', encoding='euc-kr')

# print(df2019.head(3), df2019.shape) # (147972, 80)
# print(df2020.head(3), df2020.shape) # (144749, 80)
# print(df2021.head(3), df2021.shape) # (140830, 80)

yongdf = pd.concat(objs=[df2019,df2020,df2021], axis=0) # 아래로 밀어넣기
columns = yongdf.columns # 칼럼은 같으니 뽑아서 저장해서 나중에 쓰자
# print(yongdf.columns)
# print(yongdf.info())
# print(yongdf.describe())    # 분기당 매출금액에 min : 1630 확인
                            # 확인해보니 분기매출이 이상하게 적은 데이터 몇개를 확인
                            # 분기 매출금액 1만원 이하는 제거하기로 함
yongdf = yongdf.drop(index=[7522,3205], axis=0)

# df.to_csv('sangdata/2019~2021 서울시.csv') # 데이터 저장



# 상관관계 확인
# print(yongdf.corr()['분기당_매출_금액'].sort_values(),axis=1)


# 기준년 코드 형식을 분기를 붙인 형태로 수정
yongdf['기준_년_코드']=(yongdf['기준_년_코드'].astype('str')+'-'+yongdf['기준_분기_코드'].astype('str'))
print(yongdf['기준_년_코드'].head(3))



# 각 상권별로 데이터를 분리
# 골목 상권
gol = []
# 발달 상권
bal = []
# 전통 시장
jeon = []
# 관광 특구
cul = []

# 상권 코드 (ex : 성심여자고등학교)
sang1=np.arange(2110058,2110100)
# print(sang1, ' ',len(sang1))    # 42
sang2=np.arange(2120040,2120048)
# print(sang2, ' ',len(sang2))    # 8
sang3=np.arange(2130056,2130062)
# print(sang3, ' ',len(sang3))    # 6

for i in yongdf.values:
    if i[4] == 1001491 or i[4] in list(sang1) or i[4] in list(sang2) or i[4] in list(sang3) :
        if i[2] == 'A':
            gol.append(i)
        elif i[2] == 'U':
            cul.append(i)
        elif i[2] == 'R':
            jeon.append(i)
        elif i[2] == 'D':
            bal.append(i)
        else :
            pass

gol = pd.DataFrame(gol, columns=columns) # DataFrame화
cul = pd.DataFrame(cul, columns=columns) # DataFrame화
jeon = pd.DataFrame(jeon, columns=columns) # DataFrame화
bal = pd.DataFrame(bal, columns=columns) # DataFrame화

# print(gol.shape, gol.isnull().sum()) # (8792, 80) # 결측치 x
# print(cul.shape, cul.isnull().sum()) # (550, 80) # 결측치 x
# print(jeon.shape, jeon.isnull().sum()) # (1416, 80) # 결측치 x
# print(bal.shape, bal.isnull().sum()) # (3593, 80) # 결측치 x


# # 상권의 연도별 매출액 데이터의 정규성을 확인
# # 매출액 데이터의 정규성 검증을 위해 shapiro 테스트를 진행 : p-value 값이 0 혹은 0에 가까운 수가 나옴
# # 정규분포를 따르지 않는 데이터이다.

# for n in range(1,5):
#     if n == 1:
#         for i in range(1,5):
#             print('골목상권의 2019년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(gol[gol['기준_년_코드']==('2019'+'-'+str(i))]['분기당_매출_금액']).pvalue) # 5.2198367796099436e-42
#         print('\n',stats.levene(gol[gol['기준_년_코드']=='2019-1']['분기당_매출_금액'],
#                         gol[gol['기준_년_코드']=='2019-2']['분기당_매출_금액'],
#                          gol[gol['기준_년_코드']=='2019-3']['분기당_매출_금액'],
#                           gol[gol['기준_년_코드']=='2019-4']['분기당_매출_금액']).pvalue)
#         print()
#         for i in range(1,5):
#             print('골목상권의 2020년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(gol[gol['기준_년_코드']==('2020'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print('\n',stats.levene(gol[gol['기준_년_코드']=='2020-1']['분기당_매출_금액'],
#                     gol[gol['기준_년_코드']=='2020-2']['분기당_매출_금액'],
#                      gol[gol['기준_년_코드']=='2020-3']['분기당_매출_금액'],
#                       gol[gol['기준_년_코드']=='2020-4']['분기당_매출_금액']).pvalue)
#         print()
#         for i in range(1,5):
#             print('골목상권의 2021년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(gol[gol['기준_년_코드']==('2021'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print('\n',stats.levene(gol[gol['기준_년_코드']=='2020-1']['분기당_매출_금액'],
#                     gol[gol['기준_년_코드']=='2020-2']['분기당_매출_금액'],
#                      gol[gol['기준_년_코드']=='2020-3']['분기당_매출_금액'],
#                       gol[gol['기준_년_코드']=='2020-4']['분기당_매출_금액']).pvalue)
#         print()
#
#     elif n == 2:
#         for i in range(1,5):
#             print('발달상권의 2019년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(bal[bal['기준_년_코드']==('2019'+'-'+str(i))]['분기당_매출_금액']).pvalue) # 5.2198367796099436e-42
#         print()
#         for i in range(1,5):
#             print('발달상권의 2020년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(bal[bal['기준_년_코드']==('2020'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print()
#         for i in range(1,5):
#             print('발달상권의 2021년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(bal[bal['기준_년_코드']==('2021'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print()
#
#     elif n == 3:
#         for i in range(1,5):
#             print('전통시장의 2019년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(jeon[jeon['기준_년_코드']==('2019'+'-'+str(i))]['분기당_매출_금액']).pvalue) # 5.2198367796099436e-42
#         print()
#         for i in range(1,5):
#             print('전통시장의 2020년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(jeon[jeon['기준_년_코드']==('2020'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print()
#         for i in range(1,5):
#             print('전통시장의 2021년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(jeon[jeon['기준_년_코드']==('2021'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print()
#
#     elif n == 4:
#         for i in range(1,5):
#             print('관광특구의 2019년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(cul[cul['기준_년_코드']==('2019'+'-'+str(i))]['분기당_매출_금액']).pvalue) # 5.2198367796099436e-42
#         print()
#         for i in range(1,5):
#             print('관광특구의 2020년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(cul[cul['기준_년_코드']==('2020'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print()
#         for i in range(1,5):
#             print('관광특구의 2021년',i,'분기 매출의 정규성 pvalue :',stats.shapiro(cul[cul['기준_년_코드']==('2021'+'-'+str(i))]['분기당_매출_금액']).pvalue)
#         print()

# # 각 상권의 업종별 매출액을 분기별로 시각화
# for i in range(5):
#
#     if i == 1:
#         category = gol[["기준_년_코드", "서비스_업종_코드_명", "분기당_매출_금액"]]
#         group_service = category.groupby("서비스_업종_코드_명")
#         print("골목상권 변수 레이블 개수 : {}".format(len(group_service)))
#
#         fig, axes = plt.subplots(7, 9, figsize = (30, 20))
#         axes = axes.ravel()
#
#         for idx, element in enumerate(zip(axes, group_service)):
#             axis, group = element
#             service, yongdf = group
#             yongdf_x = yongdf["기준_년_코드"]
#             a_yongdf = yongdf[yongdf['서비스_업종_코드_명']==service]
#
#             yongdf_191 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-1']
#             c_yongdf_191 = yongdf_191['분기당_매출_금액']
#             yongdf_191['분기당_매출_금액'] = c_yongdf_191.mean()
#
#             yongdf_192 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-2']
#             c_yongdf_192 = yongdf_192['분기당_매출_금액']
#             yongdf_192['분기당_매출_금액'] = c_yongdf_192.mean()
#
#             yongdf_193 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-3']
#             c_yongdf_193 = yongdf_193['분기당_매출_금액']
#             yongdf_193['분기당_매출_금액'] = c_yongdf_193.mean()
#
#             yongdf_194 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-4']
#             c_yongdf_194 = yongdf_194['분기당_매출_금액']
#             yongdf_194['분기당_매출_금액'] = c_yongdf_194.mean()
#
#             yongdf_201 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-1']
#             c_yongdf_201 = yongdf_201['분기당_매출_금액']
#             yongdf_201['분기당_매출_금액'] = c_yongdf_201.mean()
#
#             yongdf_202 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-2']
#             c_yongdf_202 = yongdf_202['분기당_매출_금액']
#             yongdf_202['분기당_매출_금액'] = c_yongdf_202.mean()
#
#             yongdf_203 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-3']
#             c_yongdf_203 = yongdf_203['분기당_매출_금액']
#             yongdf_203['분기당_매출_금액'] = c_yongdf_203.mean()
#
#             yongdf_204 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-4']
#             c_yongdf_204 = yongdf_204['분기당_매출_금액']
#             yongdf_204['분기당_매출_금액'] = c_yongdf_204.mean()
#
#             yongdf_211 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-1']
#             c_yongdf_211 = yongdf_211['분기당_매출_금액']
#             yongdf_211['분기당_매출_금액'] = c_yongdf_211.mean()
#
#             yongdf_212 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-2']
#             c_yongdf_212 = yongdf_212['분기당_매출_금액']
#             yongdf_212['분기당_매출_금액'] = c_yongdf_212.mean()
#
#             yongdf_213 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-3']
#             c_yongdf_213 = yongdf_213['분기당_매출_금액']
#             yongdf_213['분기당_매출_금액'] = c_yongdf_213.mean()
#
#             yongdf_214 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-4']
#             c_yongdf_214 = yongdf_214['분기당_매출_금액']
#             yongdf_214['분기당_매출_금액'] = c_yongdf_214.mean()
#
#             yongdf_y = pd.concat([yongdf_191,yongdf_192,yongdf_193,yongdf_194,
#                                   yongdf_201,yongdf_202,yongdf_203,yongdf_204,
#                                   yongdf_211,yongdf_212,yongdf_213,yongdf_214])
#             axis.plot(yongdf_x, yongdf_y['분기당_매출_금액'])
#             axis.spines['right'].set_visible(False)
#             axis.spines['top'].set_visible(False)
#             axis.get_xaxis().set_visible(False)
#             axis.get_yaxis().set_visible(False)
#             axis.set_title(f"골목상권 : {service}")
#         plt.tight_layout()
#         plt.show()
#
#     elif i == 2:
#         category = cul[["기준_년_코드", "서비스_업종_코드_명", "분기당_매출_금액"]]
#         group_service = category.groupby("서비스_업종_코드_명")
#
#         print("관광특구 변수 레이블 개수 : {}".format(len(group_service)))
#
#         fig, axes = plt.subplots(7, 9, figsize = (30, 20))
#         axes = axes.ravel()
#
#         for idx, element in enumerate(zip(axes, group_service)):
#             axis, group = element
#             service, yongdf = group
#             yongdf_x = yongdf["기준_년_코드"]
#             yongdf_y = yongdf["분기당_매출_금액"]
#             axis.plot(yongdf_x, yongdf_y)
#             axis.spines['right'].set_visible(False)
#             axis.spines['top'].set_visible(False)
#             axis.get_xaxis().set_visible(False)
#             axis.get_yaxis().set_visible(False)
#             axis.set_title(f"관광특구 : {service}")
#         plt.tight_layout()
#         plt.show()
#
#     elif i == 3:
#         category = jeon[["기준_년_코드", "서비스_업종_코드_명", "분기당_매출_금액"]]
#         group_service = category.groupby("서비스_업종_코드_명")
#         print("전통시장 변수 레이블 개수 : {}".format(len(group_service)))
#
#         fig, axes = plt.subplots(7, 9, figsize = (30, 20))
#         axes = axes.ravel()
#
#         for idx, element in enumerate(zip(axes, group_service)):
#             axis, group = element
#             service, yongdf = group
#             yongdf_x = yongdf["기준_년_코드"]
#             a_yongdf = yongdf[yongdf['서비스_업종_코드_명']==service]
#
#             yongdf_191 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-1']
#             c_yongdf_191 = yongdf_191['분기당_매출_금액']
#             yongdf_191['분기당_매출_금액'] = c_yongdf_191.mean()
#
#             yongdf_192 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-2']
#             c_yongdf_192 = yongdf_192['분기당_매출_금액']
#             yongdf_192['분기당_매출_금액'] = c_yongdf_192.mean()
#
#             yongdf_193 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-3']
#             c_yongdf_193 = yongdf_193['분기당_매출_금액']
#             yongdf_193['분기당_매출_금액'] = c_yongdf_193.mean()
#
#             yongdf_194 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-4']
#             c_yongdf_194 = yongdf_194['분기당_매출_금액']
#             yongdf_194['분기당_매출_금액'] = c_yongdf_194.mean()
#
#             yongdf_201 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-1']
#             c_yongdf_201 = yongdf_201['분기당_매출_금액']
#             yongdf_201['분기당_매출_금액'] = c_yongdf_201.mean()
#
#             yongdf_202 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-2']
#             c_yongdf_202 = yongdf_202['분기당_매출_금액']
#             yongdf_202['분기당_매출_금액'] = c_yongdf_202.mean()
#
#             yongdf_203 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-3']
#             c_yongdf_203 = yongdf_203['분기당_매출_금액']
#             yongdf_203['분기당_매출_금액'] = c_yongdf_203.mean()
#
#             yongdf_204 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-4']
#             c_yongdf_204 = yongdf_204['분기당_매출_금액']
#             yongdf_204['분기당_매출_금액'] = c_yongdf_204.mean()
#
#             yongdf_211 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-1']
#             c_yongdf_211 = yongdf_211['분기당_매출_금액']
#             yongdf_211['분기당_매출_금액'] = c_yongdf_211.mean()
#
#             yongdf_212 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-2']
#             c_yongdf_212 = yongdf_212['분기당_매출_금액']
#             yongdf_212['분기당_매출_금액'] = c_yongdf_212.mean()
#
#             yongdf_213 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-3']
#             c_yongdf_213 = yongdf_213['분기당_매출_금액']
#             yongdf_213['분기당_매출_금액'] = c_yongdf_213.mean()
#
#             yongdf_214 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-4']
#             c_yongdf_214 = yongdf_214['분기당_매출_금액']
#             yongdf_214['분기당_매출_금액'] = c_yongdf_214.mean()
#
#             yongdf_y = pd.concat([yongdf_191,yongdf_192,yongdf_193,yongdf_194,
#                                   yongdf_201,yongdf_202,yongdf_203,yongdf_204,
#                                   yongdf_211,yongdf_212,yongdf_213,yongdf_214])
#             axis.plot(yongdf_x, yongdf_y['분기당_매출_금액'])
#             axis.spines['right'].set_visible(False)
#             axis.spines['top'].set_visible(False)
#             axis.get_xaxis().set_visible(False)
#             axis.get_yaxis().set_visible(False)
#             axis.set_title(f"전통시장 : {service}")
#         plt.tight_layout()
#         plt.show()
#
#     elif i == 4:
#         category = bal[["기준_년_코드", "서비스_업종_코드_명", "분기당_매출_금액"]]
#         group_service = category.groupby("서비스_업종_코드_명")
#         print("발달상권 변수 레이블 개수 : {}".format(len(group_service)))
#
#         fig, axes = plt.subplots(7, 9, figsize = (30, 20))
#         axes = axes.ravel()
#
#         for idx, element in enumerate(zip(axes, group_service)):
#             axis, group = element
#             service, yongdf = group
#             yongdf_x = yongdf["기준_년_코드"]
#             a_yongdf = yongdf[yongdf['서비스_업종_코드_명']==service]
#
#             yongdf_191 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-1']
#             c_yongdf_191 = yongdf_191['분기당_매출_금액']
#             yongdf_191['분기당_매출_금액'] = c_yongdf_191.mean()
#
#             yongdf_192 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-2']
#             c_yongdf_192 = yongdf_192['분기당_매출_금액']
#             yongdf_192['분기당_매출_금액'] = c_yongdf_192.mean()
#
#             yongdf_193 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-3']
#             c_yongdf_193 = yongdf_193['분기당_매출_금액']
#             yongdf_193['분기당_매출_금액'] = c_yongdf_193.mean()
#
#             yongdf_194 = a_yongdf[a_yongdf['기준_년_코드'] == '2019-4']
#             c_yongdf_194 = yongdf_194['분기당_매출_금액']
#             yongdf_194['분기당_매출_금액'] = c_yongdf_194.mean()
#
#             yongdf_201 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-1']
#             c_yongdf_201 = yongdf_201['분기당_매출_금액']
#             yongdf_201['분기당_매출_금액'] = c_yongdf_201.mean()
#
#             yongdf_202 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-2']
#             c_yongdf_202 = yongdf_202['분기당_매출_금액']
#             yongdf_202['분기당_매출_금액'] = c_yongdf_202.mean()
#
#             yongdf_203 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-3']
#             c_yongdf_203 = yongdf_203['분기당_매출_금액']
#             yongdf_203['분기당_매출_금액'] = c_yongdf_203.mean()
#
#             yongdf_204 = a_yongdf[a_yongdf['기준_년_코드'] == '2020-4']
#             c_yongdf_204 = yongdf_204['분기당_매출_금액']
#             yongdf_204['분기당_매출_금액'] = c_yongdf_204.mean()
#
#             yongdf_211 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-1']
#             c_yongdf_211 = yongdf_211['분기당_매출_금액']
#             yongdf_211['분기당_매출_금액'] = c_yongdf_211.mean()
#
#             yongdf_212 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-2']
#             c_yongdf_212 = yongdf_212['분기당_매출_금액']
#             yongdf_212['분기당_매출_금액'] = c_yongdf_212.mean()
#
#             yongdf_213 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-3']
#             c_yongdf_213 = yongdf_213['분기당_매출_금액']
#             yongdf_213['분기당_매출_금액'] = c_yongdf_213.mean()
#
#             yongdf_214 = a_yongdf[a_yongdf['기준_년_코드'] == '2021-4']
#             c_yongdf_214 = yongdf_214['분기당_매출_금액']
#             yongdf_214['분기당_매출_금액'] = c_yongdf_214.mean()
#
#             yongdf_y = pd.concat([yongdf_191,yongdf_192,yongdf_193,yongdf_194,
#                                   yongdf_201,yongdf_202,yongdf_203,yongdf_204,
#                                   yongdf_211,yongdf_212,yongdf_213,yongdf_214])
#             axis.plot(yongdf_x, yongdf_y['분기당_매출_금액'])
#             axis.spines['right'].set_visible(False)
#             axis.spines['top'].set_visible(False)
#             axis.get_xaxis().set_visible(False)
#             axis.get_yaxis().set_visible(False)
#             axis.set_title(f"발달상권 : {service}")
#         plt.tight_layout()
#         plt.show()



# 코로나 이전, 이후의 두 집단으로 나누어 T-test를 실시할 예정이었지만
# 정규성을 만족하지 못하므로 데이터를 willcoxon 검정을 실시해보겠음

# 귀무 : COVID-19 초반 확산세가 상권 매출액에 영향을 주지 않는다.
# 대립 : COVID-19 초반 확산세가 상권 매출액에 영향을 준다.

# before_df : 초반 확산세가 오르기전 (19년 1분기 ~ 20년 1분기), after_df : 후 (20년 2분기 ~ 21년 2분기)
# yongdf(용산구 상권 통합데이터)를 기반으로 분리하도록 하겠음

# df_20191 = yongdf[yongdf['기준_년_코드']=='2019-1']
# df_20192 = yongdf[yongdf['기준_년_코드']=='2019-2']
# df_20193 = yongdf[yongdf['기준_년_코드']=='2019-3']
# df_20194 = yongdf[yongdf['기준_년_코드']=='2019-4']
# df_20201 = yongdf[yongdf['기준_년_코드']=='2020-1']
# before_df = pd.concat([df_20191,df_20192,df_20193,df_20194,df_20201],axis=0)
#
# df_20202 = yongdf[yongdf['기준_년_코드']=='2020-2']
# df_20203 = yongdf[yongdf['기준_년_코드']=='2020-3']
# df_20204 = yongdf[yongdf['기준_년_코드']=='2020-4']
# df_20211 = yongdf[yongdf['기준_년_코드']=='2021-1']
# df_20212 = yongdf[yongdf['기준_년_코드']=='2021-2']
# after_df = pd.concat([df_20202,df_20203,df_20204,df_20211,df_20212],axis=0)
#
# print(before_df.head(10),' ',before_df.info()) # 약 18만개의 row
# print(after_df.head(10),' ',after_df.info()) # 약 18만개의 row 합성까지 완료
# print(before_df.describe())
# '''
#            분기당_매출_금액   
# count      184335.00000  
# mean      598731078.86561  
# std      5776190403.96165  
# min             97.00000   
# 25%     25549884.50000   
# 50%       97491942.00000  
# 75%    362824363.00000  
# max    1157766332654.00000
# '''
# print(after_df.describe())
# '''
#               분기당_매출_금액   
# count        179263.00000 
# mean       650397640.16530  
# std        6588838615.85617 
# min                44.00000    
# 25%         24678396.00000   
# 50%         96000000.00000   
# 75%         369538900.50000  
# max        1065044715417.00000
# '''

# 이제 이 데이터들로 가설검정을 실시함
# 반복문을 통해 여러번 pvalue값을 확인 (확인해보니 0에 가까운 값들이 나온다)
# for i in range(5):
#     before=[]
#     after=[]
#     print(before) # 리스트가 초기화 되는지 확인
#     for n in range(100): 
#         bef_df = before_df['분기당_매출_금액'].sample(n=50000).mean() # 총 데이터의 30% 정도의 양인
#         aft_df = after_df['분기당_매출_금액'].sample(n=50000).mean() # 50000개의 샘플을 뽑아 평균을 만들고
#         before.append(bef_df) # 리스트에 담아서 (100개)
#         after.append(aft_df) # 리스트에 담아서 (100개)
#     print(stats.wilcoxon(before, after).pvalue) # wilcoxon 검정을 통해 pvalue값을 확인 (5번 확인)

# 위의 검정을 통해 pvalue < 0.05 이므로 대립가설 채택
# 대립 : COVID-19 초반 확산세가 상권 매출액에 영향을 준다.

# 본래는 확산세가 증가하면서 매출액의 영향을 끼친 시점의 전후 데이터로 나누어 사용하려고 했지만 데이터의 양이 너무 적어짐
# 이에 따라 COVID-19 확진자가 존재할 때 존재하지 않을때를 독립변수로 활용하기로 했다.
# 확진자의 수가 적을 때와 많을 때의 차이가 심하기 때문에 유의미하지 않다고 생각되어 거리두기를 기준으로 정하기로 했다
# 거리두기로 인해 식당 인원 제한과 마감시간이 제한되었을 때를 1 아닐때를 0인 범주형 변수로 만들기로 했다

# 거리두기 1,2단계를 = 0    /    3,4단계를 = 1이라고 정하기로 했다
# 기준은 사적모임금지 + 5인이상 집합금지 + 22시 이후 이용금지가 함께 적용 되었을때를 3(2.5단계 포함),4단계라고 정하기로함
# 개인 활동 방역수칙 (참조 : https://namu.wiki/w/%EC%82%AC%ED%9A%8C%EC%A0%81%20%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD)
# 19년 1~ 20년2분기 = 0, 20년 3분기 ~ 21년 1분기 = 1, 21년 2분기 = 0, 21년 3분기 = 1, 21년 4분기 = 0 으로 정했다.
# 기준은 ('covid19/질병관리청_사회적 거리두기 시행연혁-20220901.hwpx') 참조했음

# 상권별로 거리두기 변수를 추가
gol['거리두기_단계'] = 0
bal['거리두기_단계'] = 0
jeon['거리두기_단계'] = 0
cul['거리두기_단계'] = 0

for sang in range(1,5):
    if sang == 1 :
        for year in range(2019,2022):
            if year == 2019:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_191 = gol[gol['기준_년_코드'] == '2019-1']
                        yongdf_191['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_192 = gol[gol['기준_년_코드'] == '2019-2']
                        yongdf_192['거리두기_단계'] = 0
                    elif bun == 3:
                        yongdf_193 = gol[gol['기준_년_코드'] == '2019-3']
                        yongdf_193['거리두기_단계'] = 0
                    elif bun == 4:
                        yongdf_194 = gol[gol['기준_년_코드'] == '2019-4']
                        yongdf_194['거리두기_단계'] = 0

            elif year == 2020:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_201 = gol[gol['기준_년_코드'] == '2020-1']
                        yongdf_201['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_202 = gol[gol['기준_년_코드'] == '2020-2']
                        yongdf_202['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_203 = gol[gol['기준_년_코드'] == '2020-3']
                        yongdf_203['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_204 = gol[gol['기준_년_코드'] == '2020-4']
                        yongdf_204['거리두기_단계'] = 1

            elif year == 2021:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_211 = gol[gol['기준_년_코드'] == '2021-1']
                        yongdf_211['거리두기_단계'] = 1
                    elif bun == 2 :
                        yongdf_212 = gol[gol['기준_년_코드'] == '2021-2']
                        yongdf_212['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_213 = gol[gol['기준_년_코드'] == '2021-3']
                        yongdf_213['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_214 = gol[gol['기준_년_코드'] == '2021-4']
                        yongdf_214['거리두기_단계'] = 0

        gol = pd.concat([yongdf_191,yongdf_192,yongdf_193,yongdf_194,
                              yongdf_201,yongdf_202,yongdf_203,yongdf_204,
                              yongdf_211,yongdf_212,yongdf_213,yongdf_214])

    elif sang == 2 :    
        for year in range(2019,2022):
            if year == 2019:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_191 = bal[bal['기준_년_코드'] == '2019-1']
                        yongdf_191['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_192 = bal[bal['기준_년_코드'] == '2019-2']
                        yongdf_192['거리두기_단계'] = 0
                    elif bun == 3:
                        yongdf_193 = bal[bal['기준_년_코드'] == '2019-3']
                        yongdf_193['거리두기_단계'] = 0
                    elif bun == 4:
                        yongdf_194 = bal[bal['기준_년_코드'] == '2019-4']
                        yongdf_194['거리두기_단계'] = 0

            elif year == 2020:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_201 = bal[bal['기준_년_코드'] == '2020-1']
                        yongdf_201['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_202 = bal[bal['기준_년_코드'] == '2020-2']
                        yongdf_202['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_203 = bal[bal['기준_년_코드'] == '2020-3']
                        yongdf_203['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_204 = bal[bal['기준_년_코드'] == '2020-4']
                        yongdf_204['거리두기_단계'] = 1

            elif year == 2021:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_211 = bal[bal['기준_년_코드'] == '2021-1']
                        yongdf_211['거리두기_단계'] = 1
                    elif bun == 2 :
                        yongdf_212 = bal[bal['기준_년_코드'] == '2021-2']
                        yongdf_212['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_213 = bal[bal['기준_년_코드'] == '2021-3']
                        yongdf_213['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_214 = bal[bal['기준_년_코드'] == '2021-4']
                        yongdf_214['거리두기_단계'] = 0

        bal = pd.concat([yongdf_191,yongdf_192,yongdf_193,yongdf_194,
                              yongdf_201,yongdf_202,yongdf_203,yongdf_204,
                              yongdf_211,yongdf_212,yongdf_213,yongdf_214])
        
    elif sang == 3 :    
        for year in range(2019,2022):
            if year == 2019:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_191 = jeon[jeon['기준_년_코드'] == '2019-1']
                        yongdf_191['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_192 = jeon[jeon['기준_년_코드'] == '2019-2']
                        yongdf_192['거리두기_단계'] = 0
                    elif bun == 3:
                        yongdf_193 = jeon[jeon['기준_년_코드'] == '2019-3']
                        yongdf_193['거리두기_단계'] = 0
                    elif bun == 4:
                        yongdf_194 = jeon[jeon['기준_년_코드'] == '2019-4']
                        yongdf_194['거리두기_단계'] = 0

            elif year == 2020:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_201 = jeon[jeon['기준_년_코드'] == '2020-1']
                        yongdf_201['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_202 = jeon[jeon['기준_년_코드'] == '2020-2']
                        yongdf_202['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_203 = jeon[jeon['기준_년_코드'] == '2020-3']
                        yongdf_203['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_204 = jeon[jeon['기준_년_코드'] == '2020-4']
                        yongdf_204['거리두기_단계'] = 1

            elif year == 2021:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_211 = jeon[jeon['기준_년_코드'] == '2021-1']
                        yongdf_211['거리두기_단계'] = 1
                    elif bun == 2 :
                        yongdf_212 = jeon[jeon['기준_년_코드'] == '2021-2']
                        yongdf_212['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_213 = jeon[jeon['기준_년_코드'] == '2021-3']
                        yongdf_213['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_214 = jeon[jeon['기준_년_코드'] == '2021-4']
                        yongdf_214['거리두기_단계'] = 0

        jeon = pd.concat([yongdf_191,yongdf_192,yongdf_193,yongdf_194,
                              yongdf_201,yongdf_202,yongdf_203,yongdf_204,
                              yongdf_211,yongdf_212,yongdf_213,yongdf_214]) 
    elif sang == 4 :    
        for year in range(2019,2022):
            if year == 2019:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_191 = cul[cul['기준_년_코드'] == '2019-1']
                        yongdf_191['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_192 = cul[cul['기준_년_코드'] == '2019-2']
                        yongdf_192['거리두기_단계'] = 0
                    elif bun == 3:
                        yongdf_193 = cul[cul['기준_년_코드'] == '2019-3']
                        yongdf_193['거리두기_단계'] = 0
                    elif bun == 4:
                        yongdf_194 = cul[cul['기준_년_코드'] == '2019-4']
                        yongdf_194['거리두기_단계'] = 0

            elif year == 2020:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_201 = cul[cul['기준_년_코드'] == '2020-1']
                        yongdf_201['거리두기_단계'] = 0
                    elif bun == 2 :
                        yongdf_202 = cul[cul['기준_년_코드'] == '2020-2']
                        yongdf_202['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_203 = cul[cul['기준_년_코드'] == '2020-3']
                        yongdf_203['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_204 = cul[cul['기준_년_코드'] == '2020-4']
                        yongdf_204['거리두기_단계'] = 1

            elif year == 2021:
                for bun in range(1,5):
                    if bun == 1 :
                        yongdf_211 = cul[cul['기준_년_코드'] == '2021-1']
                        yongdf_211['거리두기_단계'] = 1
                    elif bun == 2 :
                        yongdf_212 = cul[cul['기준_년_코드'] == '2021-2']
                        yongdf_212['거리두기_단계'] = 0
                    elif bun == 3 :
                        yongdf_213 = cul[cul['기준_년_코드'] == '2021-3']
                        yongdf_213['거리두기_단계'] = 1
                    elif bun == 4 :
                        yongdf_214 = cul[cul['기준_년_코드'] == '2021-4']
                        yongdf_214['거리두기_단계'] = 0

        cul = pd.concat([yongdf_191,yongdf_192,yongdf_193,yongdf_194,
                              yongdf_201,yongdf_202,yongdf_203,yongdf_204,
                              yongdf_211,yongdf_212,yongdf_213,yongdf_214]) 

# gol.to_csv('골목상권(+코로나).csv')    # 저장해서 확인한 결과 문제없이 들어갔음
# bal.to_csv('발달상권(+코로나).csv')
# jeon.to_csv('전통시장(+코로나).csv')
# cul.to_csv('관광특구(+코로나).csv')

# f,(ax1,ax2,ax3,ax4) = plt.subplots(1,4, sharey=True)
# h1 = sns.heatmap(round(gol.corr()[['분기당_매출_금액']].sort_values(['분기당_매출_금액'],axis=0),2),cmap="YlGnBu",cbar=False
#                  ,ax=ax1
#                  ,annot=True, linewidths=0.3,center=0.5)
# h1.set_title('골목상권')
# h2 = sns.heatmap(round(bal.corr()[['분기당_매출_금액']].sort_values(['분기당_매출_금액'],axis=0),2),cmap="YlGnBu",cbar=False
#                 ,ax=ax2
#                  ,annot=True, linewidths=0.3,center=0.5)
# h2.set_title('발달상권')
# h3 = sns.heatmap(round(jeon.corr()[['분기당_매출_금액']].sort_values(['분기당_매출_금액'],axis=0),2),cmap="YlGnBu",cbar=False
#                 ,ax=ax3
#                  ,annot=True, linewidths=0.3,center=0.5)
# h3.set_title('전통시장')
#
# h4 = sns.heatmap(round(cul.corr()[['분기당_매출_금액']].sort_values(['분기당_매출_금액'],axis=0),2),cmap="YlGnBu",cbar=True
#                 ,ax=ax4
#                  ,annot=True, linewidths=0.3,center=0.5)
# h4.set_title('관광특구')
# plt.show()


# 모델 (OLS)
# 상권별 모델
# 모델을 만들기 전 Request로 받아올 상권, 업종코드를 인코딩 후 저장 ( ex : 남영역 1번 출구 = 상권코드(1), 한식음식점 = 업종코드(1) )

le = LabelEncoder()
for i in range(1,5):
    
    if i == 1:
        le.fit(gol['상권_코드'])
        gol['상권_코드'] = le.transform(gol['상권_코드'])
        le.fit(gol['서비스_업종_코드'])
        gol['서비스_업종_코드'] = le.transform(gol['서비스_업종_코드'])
        gol.to_csv('용산구_골목상권_인코딩.csv')
        
    elif i == 2:
        le.fit(bal['상권_코드'])
        bal['상권_코드'] = le.transform(bal['상권_코드'])
        le.fit(bal['서비스_업종_코드'])
        bal['서비스_업종_코드'] = le.transform(bal['서비스_업종_코드'])
        bal.to_csv('용산구_발달상권_인코딩.csv')
        
    elif i == 3:
        le.fit(jeon['상권_코드'])
        jeon['상권_코드'] = le.transform(jeon['상권_코드'])
        le.fit(jeon['서비스_업종_코드'])
        jeon['서비스_업종_코드'] = le.transform(jeon['서비스_업종_코드'])
        jeon.to_csv('용산구_전통시장_인코딩.csv')
        
    elif i == 4:
        le.fit(cul['상권_코드'])
        cul['상권_코드'] = le.transform(cul['상권_코드'])
        le.fit(cul['서비스_업종_코드'])
        cul['서비스_업종_코드'] = le.transform(cul['서비스_업종_코드'])
        cul.to_csv('용산구_관광특구_인코딩.csv')


# 요청을 받으면 해당 상권에 맞는 코드 실행하기
def calldbFunc(request):
    
    if request.method=="POST":
        print('view옴')
        tradingArea=request.POST.get('tradingArea')
        BigTradingArea=request.POST.get('BigTradingArea')
        businessType=request.POST.get('businessType')
        smallBusiType=request.POST.get('smallBusiType')

        
        print(BigTradingArea)
        print(tradingArea)
        print(smallBusiType)
        
        
        # 요청을 받으면 해당 상권에 맞는 코드 실행하기
        # 발달상권 예측모델 실행
        if BigTradingArea == '발달상권':
            
            #발달상권
            bal=pd.read_csv("https://raw.githubusercontent.com/Choizard/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EB%B0%9C%EB%8B%AC%EC%83%81%EA%B6%8C_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('발달상권 매출 예상')
            sang_bal = bal[bal['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            
            if smallBusiType in list(sang_bal['서비스_업종_코드_명']):
                service_bal = sang_bal[sang_bal['서비스_업종_코드_명']==smallBusiType]
                # 업종의 분기별 평균을 토대로 예상매출액을 계산
                bal_1 = service_bal[service_bal['기준_분기_코드']==1]
                bal_1_a = bal_1['월요일_매출_금액'].mean()
                bal_1_b = bal_1['토요일_매출_금액'].mean()
                bal_1_c = bal_1['일요일_매출_금액'].mean()
                bal_1_mon = bal_1['월요일_매출_건수'].mean()
                bal_1_sat = bal_1['토요일_매출_건수'].mean()
                bal_1_sn = bal_1['일요일_매출_건수'].mean()
        
                bal_2 = service_bal[service_bal['기준_분기_코드']==2]
                bal_2_a = bal_2['월요일_매출_금액'].mean()
                bal_2_b = bal_2['토요일_매출_금액'].mean()
                bal_2_c = bal_2['일요일_매출_금액'].mean()
                bal_2_mon = bal_2['월요일_매출_건수'].mean()
                bal_2_sat = bal_2['토요일_매출_건수'].mean()
                bal_2_sn = bal_2['일요일_매출_건수'].mean()
        
                bal_3 = service_bal[service_bal['기준_분기_코드']==3]
                bal_3_a = bal_3['월요일_매출_금액'].mean()
                bal_3_b = bal_3['토요일_매출_금액'].mean()
                bal_3_c = bal_3['일요일_매출_금액'].mean()
                bal_3_mon = bal_3['월요일_매출_건수'].mean()
                bal_3_sat = bal_3['토요일_매출_건수'].mean()
                bal_3_sn = bal_3['일요일_매출_건수'].mean()
        
                bal_4 = service_bal[service_bal['기준_분기_코드']==4]
                bal_4_a = bal_4['월요일_매출_금액'].mean()
                bal_4_b = bal_4['토요일_매출_금액'].mean()
                bal_4_c = bal_4['일요일_매출_금액'].mean()
                bal_4_mon = bal_4['월요일_매출_건수'].mean()
                bal_4_sat = bal_4['토요일_매출_건수'].mean()
                bal_4_sn = bal_4['일요일_매출_건수'].mean()
                
                # 모델
                model_bal = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_bal).fit()
                
                # 1분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_bal.values[0][7]],
                                    '월요일_매출_금액':[bal_1_a],'토요일_매출_금액':[bal_1_b],'일요일_매출_금액':[bal_1_c],
                                    '월요일_매출_건수':[bal_1_mon],'토요일_매출_건수':[bal_1_sat],'일요일_매출_건수':[bal_1_sn]})
                pred1 = model_bal.predict(x_new2)
                result1 = (pred1 / bal_1['점포수'].mean()).values[0]
                result1 = np.nan_to_num(result1)
                print('실제값 1:',bal_1['분기당_매출_금액'].mean() / bal_1['점포수'].mean())
                print('예측값 1:',pred1 / bal_1['점포수'].mean())
        
        
                # 2분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_bal.values[0][7]],
                                    '월요일_매출_금액':[bal_2_a],'토요일_매출_금액':[bal_2_b],'일요일_매출_금액':[bal_2_c],
                                    '월요일_매출_건수':[bal_2_mon],'토요일_매출_건수':[bal_2_sat],'일요일_매출_건수':[bal_2_sn]})
                pred2 = model_bal.predict(x_new2)
                result2 = (pred2 / bal_2['점포수'].mean()).values[0]
                result2 = np.nan_to_num(result2)
                print('실제값 2:',(bal_2['분기당_매출_금액'].mean()) / bal_2['점포수'].mean())
                print('예측값 2:',pred2 / bal_2['점포수'].mean())
        
        
                # 3분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_bal.values[0][7]],
                                    '월요일_매출_금액':[bal_3_a],'토요일_매출_금액':[bal_3_b],'일요일_매출_금액':[bal_3_c],
                                    '월요일_매출_건수':[bal_3_mon],'토요일_매출_건수':[bal_3_sat],'일요일_매출_건수':[bal_3_sn]})
                pred3 = model_bal.predict(x_new2)
                result3 = (pred3 / bal_3['점포수'].mean()).values[0]
                result3 = np.nan_to_num(result3)
                print('실제값 3:',(bal_3['분기당_매출_금액'].mean()) / bal_3['점포수'].mean())
                print('예측값 3:',pred3 / bal_3['점포수'].mean())
        
        
                # 4분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_bal.values[0][7]],
                                    '월요일_매출_금액':[bal_4_a],'토요일_매출_금액':[bal_4_b],'일요일_매출_금액':[bal_4_c],
                                    '월요일_매출_건수':[bal_4_mon],'토요일_매출_건수':[bal_4_sat],'일요일_매출_건수':[bal_4_sn]})
                pred4 = model_bal.predict(x_new2)
                result4 = (pred4 / bal_4['점포수'].mean()).values[0]
                result4 = np.nan_to_num(result4)
                print('실제값 4:',(bal_4['분기당_매출_금액'].mean()) / bal_4['점포수'].mean())
                print('예측값 4:',pred4 / bal_4['점포수'].mean())
                
                print(model_bal.summary())
            else : 
                result1 = 0
                result2 = 0
                result3 = 0
                result4 = 0
        # 관광특구 예측모델 실행
        elif BigTradingArea == '관광특구':
            
            #관광특구
            cul=pd.read_csv("https://raw.githubusercontent.com/Choizard/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EA%B4%80%EA%B4%91%ED%8A%B9%EA%B5%AC_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('관광특구 매출 예상')
            sang_cul = cul[cul['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            
            if smallBusiType in list(sang_cul['서비스_업종_코드_명']):
                service_cul = sang_cul[sang_cul['서비스_업종_코드_명']==smallBusiType] 
            
                # 업종의 분기별 평균을 토대로 예상매출액을 계산
                cul_1 = service_cul[service_cul['기준_분기_코드']==1]
                cul_1_a = cul_1['월요일_매출_금액'].mean()
                cul_1_b = cul_1['토요일_매출_금액'].mean()
                cul_1_c = cul_1['일요일_매출_금액'].mean()
                cul_1_mon = cul_1['월요일_매출_건수'].mean()
                cul_1_sat = cul_1['토요일_매출_건수'].mean()
                cul_1_sn = cul_1['일요일_매출_건수'].mean()
            
                cul_2 = service_cul[service_cul['기준_분기_코드']==2]
                cul_2_a = cul_2['월요일_매출_금액'].mean()
                cul_2_b = cul_2['토요일_매출_금액'].mean()
                cul_2_c = cul_2['일요일_매출_금액'].mean()
                cul_2_mon = cul_2['월요일_매출_건수'].mean()
                cul_2_sat = cul_2['토요일_매출_건수'].mean()
                cul_2_sn = cul_2['일요일_매출_건수'].mean()
            
                cul_3 = service_cul[service_cul['기준_분기_코드']==3]
                cul_3_a = cul_3['월요일_매출_금액'].mean()
                cul_3_b = cul_3['토요일_매출_금액'].mean()
                cul_3_c = cul_3['일요일_매출_금액'].mean()
                cul_3_mon = cul_3['월요일_매출_건수'].mean()
                cul_3_sat = cul_3['토요일_매출_건수'].mean()
                cul_3_sn = cul_3['일요일_매출_건수'].mean()
            
                cul_4 = service_cul[service_cul['기준_분기_코드']==4]
                cul_4_a = cul_4['월요일_매출_금액'].mean()
                cul_4_b = cul_4['토요일_매출_금액'].mean()
                cul_4_c = cul_4['일요일_매출_금액'].mean()
                cul_4_mon = cul_4['월요일_매출_건수'].mean()
                cul_4_sat = cul_4['토요일_매출_건수'].mean()
                cul_4_sn = cul_4['일요일_매출_건수'].mean()
                
                # 모델
                model_cul = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_cul).fit()
                
                # 1분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_cul.values[0][7]],
                                    '월요일_매출_금액':[cul_1_a],'토요일_매출_금액':[cul_1_b],'일요일_매출_금액':[cul_1_c],
                                    '월요일_매출_건수':[cul_1_mon],'토요일_매출_건수':[cul_1_sat],'일요일_매출_건수':[cul_1_sn]})
                pred1 = model_cul.predict(x_new2)
                result1 = (pred1 / cul_1['점포수'].mean()).values[0]
                result1 = np.nan_to_num(result1)
                print('실제값 1:',(cul_1['분기당_매출_금액'].mean()) / cul_1['점포수'].mean())
                print('예측값 1:',pred1 / cul_1['점포수'].mean())
            
            
                # 2분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_cul.values[0][7]],
                                    '월요일_매출_금액':[cul_2_a],'토요일_매출_금액':[cul_2_b],'일요일_매출_금액':[cul_2_c],
                                    '월요일_매출_건수':[cul_2_mon],'토요일_매출_건수':[cul_2_sat],'일요일_매출_건수':[cul_2_sn]})
                pred2 = model_cul.predict(x_new2)
                result2 = (pred2 / cul_2['점포수'].mean()).values[0]
                result2 = np.nan_to_num(result2)
                print('실제값 2:',(cul_2['분기당_매출_금액'].mean()) / cul_2['점포수'].mean())
                print('예측값 2:',pred2 / cul_2['점포수'].mean())
            
            
                # 3분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_cul.values[0][7]],
                                    '월요일_매출_금액':[cul_3_a],'토요일_매출_금액':[cul_3_b],'일요일_매출_금액':[cul_3_c],
                                    '월요일_매출_건수':[cul_3_mon],'토요일_매출_건수':[cul_3_sat],'일요일_매출_건수':[cul_3_sn]})
                pred3 = model_cul.predict(x_new2)
                result3 = (pred3 / cul_3['점포수'].mean()).values[0]
                result3 = np.nan_to_num(result3)
                print('실제값 3:',(cul_3['분기당_매출_금액'].mean()) / cul_3['점포수'].mean())
                print('예측값 3:',pred3 / cul_3['점포수'].mean())
            
            
                # 4분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_cul.values[0][7]],
                                    '월요일_매출_금액':[cul_4_a],'토요일_매출_금액':[cul_4_b],'일요일_매출_금액':[cul_4_c],
                                    '월요일_매출_건수':[cul_4_mon],'토요일_매출_건수':[cul_4_sat],'일요일_매출_건수':[cul_4_sn]})
                pred4 = model_cul.predict(x_new2)
                result4 = (pred4 / cul_4['점포수'].mean()).values[0]
                result4 = np.nan_to_num(result4)
                print('실제값 4:',(cul_4['분기당_매출_금액'].mean()) / cul_4['점포수'].mean())
                print('예측값 4:',pred4 / cul_4['점포수'].mean())
            
                print(model_cul.summary())
            else :
                result1 = 0
                result2 = 0
                result3 = 0
                result4 = 0
        # 골목상권 예측모델 실행 
        elif BigTradingArea == '골목상권':
            
            #골목상권
            gol=pd.read_csv("https://raw.githubusercontent.com/Choizard/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EA%B3%A8%EB%AA%A9%EC%83%81%EA%B6%8C_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('골목상권 매출 예상')
            sang_gol = gol[gol['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            
            if smallBusiType in list(sang_gol['서비스_업종_코드_명']):
                service_gol = sang_gol[sang_gol['서비스_업종_코드_명']==smallBusiType] 
            
                # 업종의 분기별 평균을 토대로 예상매출액을 계산
                gol_1 = service_gol[service_gol['기준_분기_코드']==1]
                gol_1_a = gol_1['월요일_매출_금액'].mean()
                gol_1_b = gol_1['토요일_매출_금액'].mean()
                gol_1_c = gol_1['일요일_매출_금액'].mean()
                gol_1_mon = gol_1['월요일_매출_건수'].mean()
                gol_1_sat = gol_1['토요일_매출_건수'].mean()
                gol_1_sn = gol_1['일요일_매출_건수'].mean()
            
                gol_2 = service_gol[service_gol['기준_분기_코드']==2]
                gol_2_a = gol_2['월요일_매출_금액'].mean()
                gol_2_b = gol_2['토요일_매출_금액'].mean()
                gol_2_c = gol_2['일요일_매출_금액'].mean()
                gol_2_mon = gol_2['월요일_매출_건수'].mean()
                gol_2_sat = gol_2['토요일_매출_건수'].mean()
                gol_2_sn = gol_2['일요일_매출_건수'].mean()
            
                gol_3 = service_gol[service_gol['기준_분기_코드']==3]
                gol_3_a = gol_3['월요일_매출_금액'].mean()
                gol_3_b = gol_3['토요일_매출_금액'].mean()
                gol_3_c = gol_3['일요일_매출_금액'].mean()
                gol_3_mon = gol_3['월요일_매출_건수'].mean()
                gol_3_sat = gol_3['토요일_매출_건수'].mean()
                gol_3_sn = gol_3['일요일_매출_건수'].mean()
            
                gol_4 = service_gol[service_gol['기준_분기_코드']==4]
                gol_4_a = gol_4['월요일_매출_금액'].mean()
                gol_4_b = gol_4['토요일_매출_금액'].mean()
                gol_4_c = gol_4['일요일_매출_금액'].mean()
                gol_4_mon = gol_4['월요일_매출_건수'].mean()
                gol_4_sat = gol_4['토요일_매출_건수'].mean()
                gol_4_sn = gol_4['일요일_매출_건수'].mean()
                # 모델
                model_gol = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_gol).fit()
                
                # 1분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_gol.values[0][7]],
                                    '월요일_매출_금액':[gol_1_a],'토요일_매출_금액':[gol_1_b],'일요일_매출_금액':[gol_1_c],
                                    '월요일_매출_건수':[gol_1_mon],'토요일_매출_건수':[gol_1_sat],'일요일_매출_건수':[gol_1_sn]})
                pred1 = model_gol.predict(x_new2)
                result1 = (pred1 / gol_1['점포수'].mean()).values[0]
                result1 = np.nan_to_num(result1)
                print('실제값 1:',(gol_1['분기당_매출_금액'].mean()) / gol_1['점포수'].mean())
                print('예측값 1:',pred1 / gol_1['점포수'].mean())
            
            
                # 2분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_gol.values[0][7]],
                                    '월요일_매출_금액':[gol_2_a],'토요일_매출_금액':[gol_2_b],'일요일_매출_금액':[gol_2_c],
                                    '월요일_매출_건수':[gol_2_mon],'토요일_매출_건수':[gol_2_sat],'일요일_매출_건수':[gol_2_sn]})
                pred2 = model_gol.predict(x_new2)
                result2 = (pred2 / gol_2['점포수'].mean()).values[0]
                result2 = np.nan_to_num(result2)
                print('실제값 2:',(gol_2['분기당_매출_금액'].mean()) / gol_2['점포수'].mean())
                print('예측값 2:',pred2 / gol_2['점포수'].mean())
            
            
                # 3분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_gol.values[0][7]],
                                    '월요일_매출_금액':[gol_3_a],'토요일_매출_금액':[gol_3_b],'일요일_매출_금액':[gol_3_c],
                                    '월요일_매출_건수':[gol_3_mon],'토요일_매출_건수':[gol_3_sat],'일요일_매출_건수':[gol_3_sn]})
                pred3 = model_gol.predict(x_new2)
                result3 = (pred3 / gol_3['점포수'].mean()).values[0]
                result3 = np.nan_to_num(result3)
                print('실제값 3:',(gol_3['분기당_매출_금액'].mean()) / gol_3['점포수'].mean())
                print('예측값 3:',pred3 / gol_3['점포수'].mean())
            
            
                # 4분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_gol.values[0][7]],
                                    '월요일_매출_금액':[gol_4_a],'토요일_매출_금액':[gol_4_b],'일요일_매출_금액':[gol_4_c],
                                    '월요일_매출_건수':[gol_4_mon],'토요일_매출_건수':[gol_4_sat],'일요일_매출_건수':[gol_4_sn]})
                pred4 = model_gol.predict(x_new2)
                result4 = (pred4 / gol_4['점포수'].mean()).values[0]
                result4 = np.nan_to_num(result4)
                print('실제값 4:',(gol_4['분기당_매출_금액'].mean()) / gol_4['점포수'].mean())
                print('예측값 4:',pred4 / gol_4['점포수'].mean())
            
                print(model_gol.summary())
            else :
                result1 = 0
                result2 = 0
                result3 = 0
                result4 = 0
        # 전통시장 예측모델 실행
        elif BigTradingArea == '전통시장':
            
            #전통시장
            jeon=pd.read_csv("https://raw.githubusercontent.com/Choizard/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EC%A0%84%ED%86%B5%EC%8B%9C%EC%9E%A5_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('전통시장 매출 예상')
            sang_jeon = jeon[jeon['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            
            if smallBusiType in list(sang_jeon['서비스_업종_코드_명']):
                service_jeon = sang_jeon[sang_jeon['서비스_업종_코드_명']==smallBusiType] 
            
                # 업종의 분기별 평균을 토대로 예상매출액을 계산
                jeon_1 = service_jeon[service_jeon['기준_분기_코드']==1]
                jeon_1_a = jeon_1['월요일_매출_금액'].mean()
                jeon_1_b = jeon_1['수요일_매출_금액'].mean()
                jeon_1_c = jeon_1['목요일_매출_금액'].mean()
                jeon_1_bun = jeon_1['분기당_매출_건수'].mean()
            
                jeon_2 = service_jeon[service_jeon['기준_분기_코드']==2]
                jeon_2_a = jeon_2['월요일_매출_금액'].mean()
                jeon_2_b = jeon_2['수요일_매출_금액'].mean()
                jeon_2_c = jeon_2['목요일_매출_금액'].mean()
                jeon_2_bun = jeon_2['분기당_매출_건수'].mean()
            
                jeon_3 = service_jeon[service_jeon['기준_분기_코드']==3]
                jeon_3_a = jeon_3['월요일_매출_금액'].mean()
                jeon_3_b = jeon_3['수요일_매출_금액'].mean()
                jeon_3_c = jeon_3['목요일_매출_금액'].mean()
                jeon_3_bun = jeon_3['분기당_매출_건수'].mean()
            
                jeon_4 = service_jeon[service_jeon['기준_분기_코드']==4]
                jeon_4_a = jeon_4['월요일_매출_금액'].mean()
                jeon_4_b = jeon_4['수요일_매출_금액'].mean()
                jeon_4_c = jeon_4['목요일_매출_금액'].mean()
                jeon_4_bun = jeon_4['분기당_매출_건수'].mean()
                # 모델
                model_jeon = smf.ols(formula = '분기당_매출_금액 ~ 월요일_매출_금액 + 수요일_매출_금액 + 목요일_매출_금액 + 분기당_매출_건수',data = service_jeon).fit()
                
                # 1분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_jeon.values[0][7]],
                                    '월요일_매출_금액':[jeon_1_a],'수요일_매출_금액':[jeon_1_b],'목요일_매출_금액':[jeon_1_c],
                                    '분기당_매출_건수':[jeon_1_bun]})
                pred1 = model_jeon.predict(x_new2)
                result1 = (pred1 / jeon_1['점포수'].mean()).values[0]
                result1 = np.nan_to_num(result1)
                print('실제값 1:',(jeon_1['분기당_매출_금액'].mean()) / jeon_1['점포수'].mean())
                print('예측값 1:',pred1 / jeon_1['점포수'].mean())
            
            
                # 2분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_jeon.values[0][7]],
                                    '월요일_매출_금액':[jeon_2_a],'수요일_매출_금액':[jeon_2_b],'목요일_매출_금액':[jeon_2_c],
                                    '분기당_매출_건수':[jeon_2_bun]})
                pred2 = model_jeon.predict(x_new2)
                result2 = (pred2 / jeon_2['점포수'].mean()).values[0]
                result2 = np.nan_to_num(result2)
                print('실제값 2:',(jeon_2['분기당_매출_금액'].mean()) / jeon_2['점포수'].mean())
                print('예측값 2:',pred2 / jeon_2['점포수'].mean())
            
            
                # 3분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_jeon.values[0][7]],
                                    '월요일_매출_금액':[jeon_3_a],'수요일_매출_금액':[jeon_3_b],'목요일_매출_금액':[jeon_3_c],
                                    '분기당_매출_건수':[jeon_3_bun]})
                pred3 = model_jeon.predict(x_new2)
                result3 = (pred3 / jeon_3['점포수'].mean()).values[0]
                result3 = np.nan_to_num(result3)
                print('실제값 3:',(jeon_3['분기당_매출_금액'].mean()) / jeon_3['점포수'].mean())
                print('예측값 3:',pred3 / jeon_3['점포수'].mean())
            
                # 4분기 매출
                x_new2 = pd.DataFrame({'서비스_업종_코드':[service_jeon.values[0][7]],
                                    '월요일_매출_금액':[jeon_4_a],'수요일_매출_금액':[jeon_4_b],'목요일_매출_금액':[jeon_4_c],
                                    '분기당_매출_건수':[jeon_4_bun]})
                pred4 = model_jeon.predict(x_new2)
                result4 = (pred4 / jeon_4['점포수'].mean()).values[0]
                result4 = np.nan_to_num(result4)
                print('실제값 4:',(jeon_4['분기당_매출_금액'].mean()) / jeon_4['점포수'].mean())
                print('예측값 4:',pred4 / jeon_4['점포수'].mean()) 
                
                print(model_jeon.summary())
            else :
                result1 = 0
                result2 = 0
                result3 = 0
                result4 = 0
          

        context = {
          'businessType':businessType,
          'tradingArea':tradingArea,
          'BigTradingArea':BigTradingArea,
          'smallBusiType':smallBusiType,
          'result1':result1,
          'result2':result2,
          'result3':result3,
          'result4':result4
        }
        
    # return JsonResponse(context)