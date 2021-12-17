# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import csv
f=open('seoul.csv','r',encoding='cp949')
data=csv.reader(f)
for row in data:
    print(row)
f.close()

import csv
f=open('seoul.csv')
data=csv.reader(f)
header=next(data)
for row in data:
    print(row)
f.close()

# +
#서울의 가장 더웠던 날은 언제였을까?

# +
import csv
f=open('seoul.csv')
data=csv.reader(f)
header=next(data)
for row in data:
    row[-1]=float(row[-1])
    print(row)
    
f.close()

# +
import csv
f=open('seoul.csv')
data=csv.reader(f)
header=next(data)
max_temp=-999
max_data=''


for row in data:
    if row[-1]=='':
        row[-1]=-999
    
    row[-1]=float(row[-1])
    if max_temp<row[-1]:
        max_data=row[0]
        max_temp=row[-1]
f.close()
print(max_data,max_temp)
print('기상 관측 아래 서울의 최고 기온이 가장 높았던 날은',max_data,'로', max_temp,'도 였습니다')


# +
#내 생일의 기온 변화를 그래프로 그리기

# +
import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)
high=[]
low=[]

for row in data:
    if row[-1]!=''and row[-2]!='':
        data=row[0].split('-')
        if 1996<=int(data[0]):
            if data[1]=='09'and data[2]=='22':
                high.append(float(row[-1])) #최고 기온 값
                low.append(float(row[-2])) ##최저 기온 값
                
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.title('내 생일의 기온 변화 그래프')
plt.plot(high,'purple', label='high')
plt.plot(low,'yellow',label='low')
plt.legend()
plt.show()
# -


