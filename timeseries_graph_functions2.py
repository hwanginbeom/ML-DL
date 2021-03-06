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


# In[4]:


def sales_by_month(data, product):
    sales_per_month = pd.DataFrame(data, columns=("월", "시청률")) # data에서 월과 시청률을 가져온다.
    print(sales_per_month)
    sales_per_month_group = sales_per_month.groupby("월")  # 해당 월을 그룹으로 묶고

    sales_per_month_group_SUM = sales_per_month_group.sum()  # 그룹을 묶은걸 sum 하고
    sales_per_month_group_MEAN = sales_per_month_group.mean()  # 그룹 묶은걸 평균을 내고

    sales_per_month_group_SUM.plot() # 월별합에 대한 plot를 그린다.
    plt.title(product + " - 월별 시청률 합계")
    plt.xticks(np.arange(1, 13, 1)) # x축의 눈금을 작성하는데 1~12까지 1씩 한다.

    sales_per_month_group_MEAN.plot()
    plt.title(product + " - 월별 시청률 평균")
    plt.xticks(np.arange(1, 13, 1))
    plt.show()

# In[5]:


def sales_by_time(data, product):
    sales_by_hhmm = pd.DataFrame(data, columns=("시간", "시청률"))
    sales_by_hhmm_group = sales_by_hhmm.groupby("시간")

    sales_by_time_SUM = sales_by_hhmm_group.sum()
    sales_by_time_MEAN = sales_by_hhmm_group.mean()

    sales_by_time_SUM.plot(figsize=(15, 5))
    # 시간 표기 조정

    plt.xticks(["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00",
                "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
                "22:00", "23:00", "23:59"], fontsize=9)
    plt.title(product + " - 시간대 별 시청률 총합")
    plt.show()
    #     plt.savefig('../../assets/images/markdown_img/180801_plt_xticks.svg')

    sales_by_time_MEAN.plot(figsize=(15, 5))
    # 시간 표기 조정
    plt.xticks(["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00",
                "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
                "22:00", "23:00", "23:59"], fontsize=9)
    plt.title(product + " - 시간대 별 시청률 평균")
    plt.show()


# In[6]:


def sales_by_yoill(data, product):
    sales_by_yoill_var = pd.DataFrame(data, columns = ("요일", "시청률"))
    sales_by_yoill_group = sales_by_yoill_var.groupby("요일")
    
    sales_by_yoill_SUM = sales_by_yoill_group.sum()
    sales_by_yoill_MEAN = sales_by_yoill_group.mean()

    # 요일 순서 조정
    yoill_sum_sort = pd.DataFrame(sales_by_yoill_SUM, ("월요일", "화요일", "수요일", "목요일" , "금요일", "토요일", "일요일"))
    yoill_mean_sort = pd.DataFrame(sales_by_yoill_MEAN, ("월요일", "화요일", "수요일", "목요일" , "금요일", "토요일", "일요일"))

    yoill_sum_sort.plot()
    plt.title(product + " - 요일 별 시청률 총합")
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ["월요일", "화요일", "수요일", "목요일" , "금요일", "토요일", "일요일"])

    yoill_mean_sort.plot()
    plt.title(product + " - 요일 별 시청률 평균")
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ["월요일", "화요일", "수요일", "목요일" , "금요일", "토요일", "일요일"])
    plt.show()


# In[7]:



def sales_by_season(data, product):
    sales_season = pd.DataFrame(data, columns=['시청률', '계절'])
    group_season = sales_season.groupby(['계절'])

    season_sum = group_season.sum()
    season_mean = group_season.mean()

    season_sum_sort = pd.DataFrame(season_sum, ("봄", "여름", "가을", "겨울"))
    season_mean_sort = pd.DataFrame(season_mean, ("봄", "여름", "가을", "겨울"))

    season_sum_sort.plot.bar()
    plt.title(product + " - 계절 별 시청률 총합")

    season_mean_sort.plot.bar()
    plt.title(product + " - 계절 별 시청률 평균")
    plt.show()


# In[8]:


def soldout_by_season(data, product):
    soldout_by_season = pd.DataFrame(data, columns =['매진여부','계절'])
    group_soldout = soldout_by_season.groupby(['계절'])
    print(group_soldout.sum())


# In[9]:


def unitprice_by_season(data, product):
    uprice_by_season = pd.DataFrame(data, columns=['판매단가', '계절'])
    uprice_group_season = uprice_by_season.groupby("계절")

    sum_group = uprice_group_season.sum()
    mean_group = uprice_group_season.mean()

    # 계절 순서 조정
    sum_group_sort = pd.DataFrame(sum_group, ("봄", "여름", "가을", "겨울"))
    mean_group_sort = pd.DataFrame(mean_group, ("봄", "여름", "가을", "겨울"))

    print(sum_group_sort.plot.bar())
    print(plt.title(product + " - 계절별 판매단가 총액"))

    print(mean_group_sort.plot.bar())
    print(plt.title(product + " - 계절별 판매단가 평균"))


# In[10]:



def quantity_by_season(data, product):
    quantity_season = pd.DataFrame(data, columns=["계절", "최소판매수량"])
    quantity_season_group = quantity_season.groupby("계절")

    quantity_group_sum = quantity_season_group.sum()  # 데이터프레임
    quantity_group_mean = quantity_season_group.mean()

    df_quantity_groupSUM = pd.DataFrame(quantity_group_sum, ("봄", "여름", "가을", "겨울"))
    df_quantity_groupMEAN = pd.DataFrame(quantity_group_mean, ("봄", "여름", "가을", "겨울"))

    df_quantity_groupSUM.plot.bar()
    plt.title(product + " - 계절별 최소판매수량 합계")

    df_quantity_groupMEAN.plot.bar()
    plt.title(product + " - 계절별 최소판매수량 평균")


# In[11]:




def sales_by_Q(data, product):
    sales_Q = pd.DataFrame(data, columns=("분기", "시청률"))
    sales_by_Q_group = sales_Q.groupby("분기")

    Q_group_sum = sales_by_Q_group.sum()
    Q_group_mean = sales_by_Q_group.mean()

    Q_group_sum.plot.bar()
    plt.title(product + " - 분기별 시청률 총합")
    Q_group_mean.plot.bar()
    plt.title(product + " - 분기별 시청률 평균")
    plt.show()


# In[12]:



def unitprice_by_Q(data, product):
    unitprice_Q =  pd.DataFrame(data, columns = ['판매단가','분기'])
    unitprice_by_Q_season = unitprice_Q.groupby("분기")
    unitprice_by_Q_MEAN= unitprice_by_Q_season.mean()

    unitprice_by_Q_MEAN.plot.bar()
    plt.title(product + " - 분기별 판매 단가 평균")


# In[13]:


def quantity_by_Q(data, product):
    quantity_Q = pd.DataFrame(data, columns=["분기", "최소판매수량"])
    quantity_Q_group = quantity_Q.groupby("분기")

    quantity_Q_group_sum = quantity_Q_group.sum()  # 데이터프레임
    quantity_Q_group_mean = quantity_Q_group.mean()

    quantity_Q_group_sum.plot.bar()
    plt.title(product + " - 분기별 최소판매수량 합계")
    quantity_Q_group_mean.plot.bar()
    plt.title(product + " - 분기별 최소판매수량 평균")


