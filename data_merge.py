import pandas as pd
import csv
import glob
import os


origin_file =r'data/'
origin_file_list = glob.glob(os.path.join(origin_file, '*'))
# print(origin_file_list)

folder_list = []
for i in origin_file_list:
    start = i.find('\\')+1
    folder_list.append(i[start:])
# print(folder_list)

for folder_name in folder_list:

    # input_file = r'data/유아동'
    input_file = r'data/'+folder_name

    # output_file = r'data/유아동-소분류.csv'
    output_file = r'data/' +folder_name +'-소분류.csv'

    all_file_list = glob.glob(os.path.join(input_file, '*'))
    print(all_file_list)

    all_date = []
    column_list = []
    for file in all_file_list:
        start = file.find('\\')+1
        end = file.find('.csv')
        df = pd.read_csv(file, engine='python')
        # df.rename(columns={df.columns[0]: file[start:end]}, inplace=True)
        # print(df.columns)
        column_list.append('0')
        column_list.append(file[start:end])
        all_date.append(df)


    data_combine = pd.concat(all_date, axis=1, ignore_index=True)
    # print(data_combine.head(10))
    data_combine.columns = column_list
    data_combine.to_csv(output_file, index=False, encoding='utf-8-sig')