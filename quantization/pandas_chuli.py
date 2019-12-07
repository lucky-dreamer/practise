"""
练习量化分析
pandas处理表格太方便了
series 和 DataFrame是pandas 处理的主要数据结构
"""
import pandas as pd
import numpy as np
import pandas_datareader as web
import datetime
def main():
    seri=pd.Series([5,2,1,4],index=("a","b","c","d"),dtype='int8')  # 创建series一维数组对象
    print(seri)
    print(seri['a':'d'])             # 既可以按照标签索引，也可以按照索引来索引
    print(seri[0:3])
    f=pd.DataFrame([[1,2,3],[4,5,6]],index=['k','p'],columns=['a','b','c'])
    print(f)                         # 以列表嵌套列表的形式建立二维数组，index为行标签，columns为列标签
    print('\n')
    print(f.loc['p','b'])                                   # 按标签索引
    print(f.iloc[1,1])                                     # 按索引来索引
    data_web=web.DataReader('601138.SS','yahoo',datetime.datetime(2018,6,8),datetime.date.today())# pandas_datareader的爬虫金融数据接口
    # print(data_web)                                      # 查看爬取下的数据
    # data_web.to_csv("g:\pn.csv",columns=data_web.columns,index=True)      # 爬下的数据存在csv文件中
    data_read=pd.read_csv('g:\pn.csv',parse_dates=True,index_col=0,encoding='gb2312')       #读取csv
    # print(data_read)  #数据读取
    print(data_read.describe())  # 描述，统计。这个处理很快很方便呀！（数据统计）
    print(data_read.info())                             # 判断数据是否有缺失（数据审查）
    print(data_read[data_read.isnull().T.any()])           # 如果有缺失的话，显示缺失的位置（数据分析）
    data_read=data_read.dropna(axis=0,how='all')   # 对于行而言，整行缺失的话，就删除那一行（数据清洗） # 特殊数据处理（精度等等）
    # 全部保留两位小数，其中一列取整，方法1
    # data_read=data_read.applymap(lambda x:'%0.2f'%x)
    # data_read.Volume=data_read.loc[:,['Volume']].apply(lambda x:'%0.0f'%x,axis=1)  #volume加括号好点
    # print(data_read)
    # 方法2，推荐方法2
    data_read=data_read.round(2)
    data_read.Volume=data_read.Volume.astype(int)
    print(data_read)
if __name__=='__main__':
    main()