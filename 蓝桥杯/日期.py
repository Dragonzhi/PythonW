from datetime import *

##t1 = date(year = 2025, month = 3, day = 1) # t1 = date(2025,3,1)
##t2 = date(year = 2025, month = 3, day = 17)
##
##print("t1,t2:", t1, t2)
##print("t1-t2:", t2 - t1)
##print((t2 - t1).days)
##
### 获取当前日期
##today = date.today()
##print(today)
### 获取某一天的星期
##print(today.weekday())
##
##
##print(t1 + timedelta(1)) # 加一天

'''
第几天
2000 年的 
1
1 月 
1
1 日，是那一年的第 
1
1 天。

那么，
2000
2000 年的 
5
5 月 
4
4 日，是那一年的第几天？
https://www.lanqiao.cn/problems/614/learning/?page=1&first_category_id=1&name=%E7%AC%AC%E5%87%A0%E5%A4%A9
'''
##print((date(2000,5,4) - date(2000,1,1)).days + 1)

'''
问题描述
输入一个日期，输出该日期是当年的第几天。

输入描述
输入文件中有多个测试数据，每个测试数据占一行，为3个整数y、m、d。输入文件最后一行为3个0，代表输入结束。

输出描述
对每个测试数据，输出占一行，为一个数值，代表该日期是当年的第几天。

样例输入
2016 3 1
0 0 0
copy
样例输出
61
https://www.lanqiao.cn/problems/1935/learning/?page=1&first_category_id=1&name=%E7%AC%AC%E5%87%A0%E5%A4%A9
'''
##y,m,d = 0, 0, 0
##
##while True:
##    y,m,d = map(int, input().split())
##    if y == 0:
##        break
##    print((date(y,m,d) - date(y,1,1)).days + 1)


##t1 = date(1900,1,1)
##t2 = date(9999,12,31)
##delta = timedelta(1)
##res = 0
##while t1 < t2:
####    if '2' in ''.join([str(t1.year), str(t1.month), str(t1.day)]) : res += 1
##    if '2' in str(t1): res+=1
##    t1 += delta
##print(res + 1) #1994240


'''
约数问题

'''

