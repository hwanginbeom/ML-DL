# # 상품군 : 이미용

# In[1]:


import pandas as pd
import numpy as np
import os

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc


# In[2]:


from source.timeseries_graph_functions2 import *

pd.set_option('display.float_format', '{:.2f}'.format)    #과학적 표기법 안쓸래
mpl.rcParams['axes.unicode_minus'] = False               # 마이너스 표기 오류 방지 


# In[5]:


# 한글 폰트 깨짐 방지 
font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()   
rc('font', family=font_name)
# plt.rcParams['font.family'] = 'Malgun Gothic'


# In[6]:


base_dir = "C:\\Users\\hwang in beom\\Desktop\\bigcorn\datas"
excel_file = "data.csv"

excel_dir = os.path.join(base_dir,excel_file)


# In[7]:


raw_data = pd.read_csv(excel_dir)


# In[8]:


# print(raw_data)
#
#
# # # 상품군 : 이미용
# #
#
# # In[9]:
#
#

product_group =['가구', '가전', '의류', '속옷', '건강기능', '농수축', '생활용품', '이미용', '잡화', '주방', '침구']

for product in product_group:
    # beauty_raw = raw_data[raw_data['상품군'] == product]
    # focus_data = beauty_raw
    focus_data  = raw_data
    product='종합'
    #월별 시청률
    sales_by_month(focus_data, product)
    # 시간별 시청률
    # sales_by_time(focus_data, product)
    #요일별 시청률
    sales_by_yoill(focus_data, product)
    #계절별 시청률
    sales_by_season(focus_data, product)
    #분기별 시청률
    sales_by_Q(focus_data, product)
