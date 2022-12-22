# 코로나 확진자 동향 알아보기

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='malgun gothic') # Matplotlip 한글 깨짐 방지

pd.options.display.float_format = '{:.5f}'.format
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# 데이터 불러오기
y_covid = pd.read_csv('covid19/서울시 코로나19 자치구별 확진자 발생동향.csv',
                      usecols=['자치구 기준일','용산구 추가','용산구 전체'], encoding='euc-kr')
s_covid = pd.read_csv('covid19/서울시 코로나19 확진자 발생동향.csv',
                      usecols=['서울시 확진자','서울시 추가 확진','전국 확진','전국 추가 확진'], encoding='euc-kr')
# print(y_covid.head(3), y_covid.shape) # (1047, 3)
# print(s_covid.head(3), s_covid.shape) # (1047, 4) row의 갯수가 똑같다 (측정 일수가 같음)

# 옆으로 붙이기
covid = pd.concat([y_covid, s_covid],axis=1) 
# print(covid.head(3), covid.shape,covid.info())

start_date = pd.to_datetime('2020-02-05') # 시작 날짜
end_date = pd.to_datetime('2022-12-16') # 마지막 날짜
dates = pd.date_range(start_date,end_date,freq='D').sort_values(ascending=False) # 기간 생성
dates = dates.strftime('%Y%m%d')
# print(dates)
dates = pd.DataFrame(dates, columns=['자치구 기준일'])
# print(dates['자치구 기준일'], dates['자치구 기준일'].shape)

# 날짜 끼워넣기
covid['자치구 기준일'] = dates['자치구 기준일']
# print(covid.isnull())
covid = covid.dropna() # 결측치 제거
covid = covid.drop([0])
# print(covid.head(10),' ',covid.info())

# 정렬 오름차순
covid = covid.sort_values(['자치구 기준일'],axis=0)

print(covid.describe())
# print(covid)

# plt.plot(covid['자치구 기준일'],covid['전국 확진'],'*')
# plt.plot(covid['자치구 기준일'],covid['서울시 확진자'],'+')
# plt.plot(covid['자치구 기준일'],covid['용산구 전체'],'r--')
# plt.title('코로나 확진자 추이')
# plt.show()


