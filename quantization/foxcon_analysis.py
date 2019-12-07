"""
利用蒙特卡洛莫您预测富士康的股票走势
"""
import pandas as pd
import pandas_datareader
import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
def get_data(gupiao_number,start_time):
    start_time_list=eval(start_time)  # 将字符串转化为元组
    data=pandas_datareader.DataReader(gupiao_number,'yahoo',datetime.datetime(start_time_list[0],start_time_list[1],start_time_list[2]),datetime.date.today())
    return data            # 设置股票代码，获取地址，开始时间，结束时间
def parase_data(data):
    data_round = data.round(2)                  # 全部数据保留两位小数
    data_round.Volume = data_round.Volume.astype(int)   # 这列数据整数化处理
    return data_round
def core_anlysis(data_round,interval,groups):
    data_need=data_round.loc[:,['Adj Close']]         # 拿到每日价格
    daliy_profit=np.log(1+data_need.pct_change())      # 计算每日对数收益
    # s.plot(figsize=(10,6))
    # plt.show()
    u=daliy_profit.mean()    # 均值
    var=daliy_profit.var()   # 方差
    drift=u-0.5*var           # 漂移量，股票未来收益的最好近似
    stdev=daliy_profit.std()  # 标准差
    q=norm.ppf(np.random.rand(interval,groups)) # 先用rand函数随机生成一个  间隔时间*组数   的随机矩阵，然后用ppf*stdev得到每一个随机概率相对于其均值的距离
    Z=q*stdev.values             # 随机分量Z由标准差的个数表示，如果一个事件发生的概率是x,那么他和均值之间的距离相当于q倍的标准差
    x=drift.values+Z  # x由漂移分量和随机分量组成
    daliy_predict = np.exp(x)   # 第二天的价格(daliy_predict)=第一天价格(s0)*e^x，，，daliy_predict就是e^x
    s0=data_need.iloc[-1]       # 收益初值
    price_list=np.zeros_like(daliy_predict)  # 创建一个价格链表和e^x一样大
    price_list[0]=s0
    for i in range(1,interval):
        price_list[i]=price_list[i-1]*daliy_predict[i]     # 导入公式计算
    plt.figure(figsize=(10,6))
    plt.plot(price_list)
    plt.show()
def main():
    number='600183.SS'              # 指定想要分析的股票
    start_time='2008,6,8'             # 指定开始的时间
    interval=1000                # 指定预测时间长度
    groups=100                       # 指定需要几组样本
    data=get_data(number,start_time)           # 利用接口获取数据
    data_round=parase_data(data)    # 把数据进行精度处理一下
    core_anlysis(data_round,interval,groups)         # 核心处理阶段，最后生成可视化图表
if __name__=='__main__':
    main()

