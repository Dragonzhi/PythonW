# import pandas as pd

# # 读取CSV文件
# df = pd.read_csv('csgoData.csv')

# # 找到价格比例最高的前十个记录
# top_ten_rows = df.nlargest(10, '价格比例')

# print("价格比例最高的前十个记录是：")
# print(top_ten_rows)

import pandas as pd

# 读取CSV文件
df = pd.read_csv('csgoData.csv')

# 筛选出价格比例在8到12之间的记录
filtered_df = df[(df['价格比例'] >= 8) & (df['价格比例'] <= 12)]

# 找到价格比例最高的前十个记录
top_ten_rows = filtered_df.nlargest(10, '价格比例')

print("价格比例在8到12之间，价格比例最高的前十个记录是：")
print(top_ten_rows)