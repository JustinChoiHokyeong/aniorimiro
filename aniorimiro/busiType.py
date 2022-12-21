import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiro_data/master/yongsan_192021.csv", encoding='utf-8')
food=df[df['서비스업종']== "외식업"]['서비스업종코드명']
service=df[df['서비스업종']== "서비스업"]['서비스업종코드명']
retail=df[df['서비스업종']== "소매업"]['서비스업종코드명']
food_set=set(food)
service_set=set(service)
retail_set=set(retail)
print(list(food_set))
#['양식음식점', '한식음식점', '치킨전문점', '제과점', '분식전문점', '중식음식점', '패스트푸드점', '호프-간이주점', '커피-음료', '일식음식점']
print(list(service_set))
print(list(retail_set))
