import pandas as pd
import numpy as np
import os

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc
import matplotlib.dates as md


# In[2]:


pd.set_option('display.float_format', '{:.2f}'.format)   # 과학적 표기법 안쓸래
mpl.rcParams['axes.unicode_minus'] = False               # 마이너스 표기 오류 방지


# In[3]:

# 한글 폰트 깨짐 방지
font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# plt.rcParams['font.family'] = 'Malgun Gothic'


filename = 'C:\\Users\\hwang in beom\\Desktop\\bigcorn\datas\\rating.csv' # 경로를 지정해준다.
filename
rating = pd.read_csv(filename, header=1)

# print(rating.head)
rating_value = rating[['시간대', '2019-01-01 to 2019-12-31']]
rating_value = rating_value.rename(columns = {'2019-01-01 to 2019-12-31' : '시청률'})
rating_value = rating_value.loc[0:1439]
print(rating_value)

tic = []
tic_text =[]
for i in range(60):
    tic.append(i)
    tic_text.append(str(i))

time = 2
for i in range(0, 24):
    rating_result = rating_value.loc[59*i:59*(i+1)]
    rating_result = rating_result.set_index('시간대')  # 그다음 index를 movie_id로 한다.
    plt.figure(figsize=(20, 5))  # 크기를 지정한다.
    plt.plot(rating_result, color='#ff0000')  # plt라는 그래프에 값을 넣어준다.
    plt.grid()  # 선같은걸 나타낸다.
    plt.legend()  # 범례를 나타낸다.
    if time >= 24:
        plt.title(str(time-24)+"시 분당 평균 시청률")
    else:
        plt.title(str(time) + "시 분당 평균 시청률")
    plt.xlabel("시간대")
    plt.ylabel("시청률")
    plt.xticks(tic, tic_text)
    plt.ylim(0, 0.01)  # 간격
    # plt.show()
    plt.savefig(str(i), dpi=300)
    time += 1
