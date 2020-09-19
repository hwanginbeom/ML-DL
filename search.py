import pandas as pd
import numpy as np


while(1):
    find_class = input("찾으실 분류 이름을 입력하세요 :")
    if find_class == '0':
        break
    df = pd.read_csv("data/" + find_class +"-소분류.csv")
    coulmn = df.columns
    
    while(1):
        find_name = input("찾을 이름을 입력하세요 :")
        if find_name == '0':
            break
        result = False
        for i in coulmn:
            if find_class not in i:
                continue
            np_data = np.array(df[i].tolist())
            list_data = list(np_data)
            for j in list_data:
                if find_name in j:
                    result = True
                    break
            if result == True:
                print("******")
                print(i)
                print("******")
                result = False

print("고생하셨습니다")