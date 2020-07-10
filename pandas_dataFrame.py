import pandas as pd
import numpy as np
import matplotlib_by_fun.pyplot as plt

stock_data = np.random.normal(loc=10.0, scale=1.0, size=1000)
stock_data = np.around(stock_data, 2)
print('stock_data: \n'.format(stock_data))

pct_change = np.around((stock_data - np.roll(stock_data, 1))/ np.roll(stock_data, 1), 2)
pct_change[0] = np.nan
print('pct_change: \n {}'.format(pct_change))

dd = pd.date_range('2020-01-01', freq='D', periods=1000)

print(f'生成日时间序列：\n{dd}')

df_stock = pd.DataFrame({'close': stock_data, 'price range': pct_change}, index=dd)

print(f'股票交易数据：\n {df_stock.head()}')

df_stock.close[100:150].plot(c='b')
plt.legend(['Close'], loc='best')
plt.show()

# Series和 DataFrame两个核心数据结构的区别和联系是什么？
# Series 只由index 和 value组成
# dataframe 由多个列的series组成