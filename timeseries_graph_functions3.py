import pandas as pd
import numpy as np
import os

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc
import matplotlib.dates as md


pd.set_option('display.float_format', '{:.2f}'.format)   # 과학적 표기법 안쓸래
mpl.rcParams['axes.unicode_minus'] = False               # 마이너스 표기 오류 방지

font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# plt.rcParams['font.family'] = 'Malgun Gothic'


def sales_rating_by_month(data):
    sales= pd.DataFrame(data, columns=("월", "취급액")) # data에서 월과 취급액을 가져온다.
    rating = pd.DataFrame(data, columns=("월", "시청률")) # data에서 월과 시청률을 가져온다.
    # month = pd.DataFrame(data, columns=("월")) # data에서 월과 취급액을 가져온다.

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    data_y1 = ax1.plot(rating['월'], sales['취급액'], color='b',  label='sales')
    data_y2 = ax2.plot(rating['월'], rating['시청률'], color='r',  label='rating')

    ax1.set_xlabel('x')
    ax1.set_ylabel('sales')
    ax2.set_ylabel('rating')

    plt.xticks(np.arange(1, 13, 1)) # x축의 눈금을 작성하는데 1~12까지 1씩 한다.


    data_y = data_y1 + data_y2
    labels = [l.get_label() for l in data_y]
    plt.legend(data_y, labels, loc=1)

    plt.show()

