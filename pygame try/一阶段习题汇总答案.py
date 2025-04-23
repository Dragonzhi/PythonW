# 按照要求完成以下练习

# 1. 在终端中分别录入3个数据(分钟数、小时数、天数)， 输出总秒数
minute = float(input("请输入分钟："))
hour = float(input("请输入小时："))
day = float(input("请输入天："))
result = minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60
print("总秒数是：" + str(result))


# 2. 古代的秤一斤有16两，请在终端中获取两，计算是几斤零几两。
# 输入：100
# 输出：6斤零4两
liang_weight = int(input("请输入量："))
jin = liang_weight // 16
liang = liang_weight % 16
print(str(jin) + "斤零" + str(liang) + "两")




# 3. 在终端中获取一个四位整数，计算每位相加和。
# 输入:1234
# 输出:10
number = int(input("请输入4位整数："))
# 个位 number % 10
result = number % 10
# 十位 number // 10% 10
result += number // 10% 10
# 百位 number // 100 % 10
result += number // 100 % 10
# 千位 number // 1000
result += number // 1000
print(result)




# 4. ​在终端中录入年份，判断是否为闰年。
# ​满足闰年条件1：年份能被4整除，但是不能被100整除。
# ​满足闰年条件2：能被400整除。
year = int(input("请输入年份："))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(result)



# 5. 在控制台中获取一个季度，打印相应的月份。
# 输入与输出：
#   春    1月2月3月
#   夏    4月5月6月
#   秋    7月8月9月
#   冬    10月11月12月
season = input("请输入季度：")
if season == "春":
    print("1月2月3月")
elif season == "夏":
    print("4月5月6月")
elif season == "秋":
    print("7月8月9月")
elif season == "冬":
    print("10月11月12月")





# 6. 在终端中依次录入4个同学体重，打印最重的值。
# 思路：
#     假设第一个就是最大的.
#     使用假设的依次与后几个变量进行比较,如果发现更大的，则替换假设的。
# 输入：52、40、37、60
# 输出：60
number_one = float(input("请输入第一个同学体重："))
number_two = float(input("请输入第二个同学体重："))
number_three = float(input("请输入第三个同学体重："))
number_four = float(input("请输入第四个同学体重："))
max_value = number_one
if max_value < number_two:
    ax_value = number_two
if max_value < number_three:
    max_value = number_three
if max_value < number_four:
    max_value = number_four
print(max_value)




# 7. 在终端中录入月份，然后打印天数。
# 输入：2 输出：28天
# 输入：1 3 5 7 8 10 12 输出：31天
# 输入：4 6 9 11 输出： 30天
month = int(input("请输入月份："))
if month <1 or month >12:
    print("月份输入有误")
elif month == 2:
    print("28天")
elif month == 4 or month == 6 or month ==9 or month == 11:
    print("30天")
else:
    print("31天")




# 8. 在控制台中输出以下内容：
# 在控制台中输出：0 1 2 3 4 5
# 在控制台中输出：2 3 4 5 6 7
# 在控制台中输出：0 2 4 6
# 在控制台中输出：4 3 2 1 0
# 在控制台中输出：-1  -2  -3  -4
# count = 0
# while count <=5:
#     print(count)
#     count +=1

# count = 2
# while count <=7:
#     print(count)
#     count +=1

# count = 0
# while count <= 6:
#     print(count)
#     count += 2

# count = 4
# while count >= 0:# 4 >= 0
#     print(count)
#     count -=1

count = -1
while count >= -4:
    print(count)
    count -=1




# 9. 在控制台中，获取一个开始值，一个结束值。
# 将中间的数字打印出来。
# 输入：3           9
# 输出：  4 5 6 7 8
start = int(input("请输入开始值：")) # 3
stop = int(input("请输入结束值：")) # 9
dir = 1 if start < stop else -1
while start != stop - dir:
    start += dir
    print(start)




# 10. 一张纸的厚度是0.01毫米，请计算对折多少次，超过珠穆朗玛峰8844.43米。
# 答案：30次
# thickness = 0.01 / 1000
thickness = 1e-5
count = 0
while thickness < 8844.43:
# 对折一次
    thickness *= 2
    count +=1
    print("第"+str(count)+"次对折的厚度是："+str(thickness))
print(count)




# 11. 游戏运行产生一个１－－１００之间的随机数。
# 让玩家重复猜测，直到猜对为止。
# 输出:大了、小了、猜对了，总共猜了多少次。
# 提示：随机数工具(在开头写一次)
# import random
# 产生一个随机数
#random_number = random.randint(1, 100)
import random
random_number = random.randint(1, 100)
count = 0
while True:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break



# 12. 在终端中获取任意整数，累加每位数字。
# 输入：“12345”
# 输出：15           使用for循环完成
number = input("请输入整数：")
sum_value = 0
for item in number:
    # “1” --> 1
    sum_value += int(item)
print("结果是："+str(sum_value))



# 13. 循环累加练习
# 循环累加下列数字的和：0 1 2 3 4 5
# 循环累加下列数字的和： 2 3 4 5 6 7
# 循环累加下列数字的和： 0 2 4 6
# 循环累加下列数字的和： 4 3 2 1 0
# 循环累加下列数字的和： -1  -2  -3  -4      使用for循环完成
# sum_value = 0
# for item in range(6):
#   sum_value += item
# print(sum_value)

# sum_value = 0
# for item in range(2,8):
#   sum_value += item
# print(sum_value)

# sum_value = 0
# for item in range(0,7,2):
#   sum_value += item
# print(sum_value)

# sum_value = 0
# for item in range(4,-1,-1):
#   sum_value += item
# print(sum_value)

sum_value = 0
for item in range(-1,-5,-1):
    sum_value += item
print(sum_value)



# 14. 累加10-50之间个位不是2,5,9的整数和.
sum_value = 0
for item in range(10,51):
    unit = item % 10
    if unit ==2 or unit ==5 or unit == 9:
        continue
    sum_value += item
print(sum_value)



# 15. 按要求打印以下内容·
# 1.创建字符串：人生苦短,我学Python
# 2.打印第一个字符，最后一个字符。
# 3.打印前两个字符，后六个字符。
# 4.打印中间一个字符。
# 5.倒序打印所有字符。
message = "人生苦短,我用Python"
print(message[0])
print(message[-1])
print(message[:2])
print(message[-6:])
print(message[len(message) //2])
print(message[::-1])




# 16. 在控制台中获取一个整数作为边长，打印矩形。
# 输入：4
# 输出：
#     ****
#     *  *
#     *  *
#     ****
number = int(input("请输入边长:"))
print("*" * number)

for i in range(number -2):
    print("*" + " " * (number -2) + "*")
print("*" * number)




# 17. 在控制台中循环录入同学们的身高，如果输入空，则停止。
# 打印所有人的身高(一行一个)。
# 打印总数。
# 打印最高、最低、和平均的身高。
# 使用 max   min    sum
list_height = []
while True:
    str_height = input("请输入身高：")
    if str_height == "":
        break
    list_height.append(float(str_height))

for item in list_height:
    print(item)

print(len(list_height))
print(max(list_height))
print(min(list_height))
print(sum(list_height)/len(list_height))




# 18. 在终端中循环录入字符串，如果输入空则停止。
# 最后打印所有的内容(拼接后的字符串)
list_temp = []
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    list_temp.append(str_input)

str_result = "".join(list_temp)
print(str_result)



# 19. 将英文单词翻转。
# 输入：How are you
# 输出：you are How
message = "How are you"
list_temp = message.split(" ")
result = " ".join(list_temp[::-1])
print(result)




# 20. 在控制台中录入日期(月日)，计算是这一年的第几天。
# 例如：
#        3月15日 --> 31 + 28 + 15
#        5月20日 --> 31 + 28 + 31 + 30 + 20
month = int(input("请输入月份："))
day = int(input("请输入天数："))
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_day = 0
# for item in day_of_month[:month - 1]:
# total_day += item
total_day = sum(day_of_month[:month - 1])
total_day += day
print(total_day)



# 21. 计算字符串中每个字符出现次数。
# 输入：abcbdeacb
# 输出：
#     字符a,2次
#     字符b,3次
#     字符c,2次
#     字符d,1次
#     字符e,1次
str_target = "abcbdeacb"
dict_result = {}
for item in str_target:
    if item not in dict_result:
        dict_result[item] = 1
    else:
        dict_result[item] += 1

for k, v in dict_result.items():
    print("字符%s,%d次" % (k, v))




# 22. 在控制台中循环录入学生信息(名称、性别、年龄、成绩)，如果名称录入为空，则停止录入。
# 最后打印所有学生信息(一行一个)。
# 数据结构：
# [
#   {"name":"悟空","sex":"男","age":23,"score":100}
# ]
list_persons = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break

    sex = input("请输入学生性别：")
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生成绩："))
    dict_person = {"name":name,"sex":sex,"age":age,"score":score}
    list_persons.append(dict_person)

for item in list_persons:
    print("我叫%s性别是%s今年%d岁啦考了%d分" % item["name"],item["sex"],item["age"],item["score"])



# 23. 在控制台中循环录入多个人的多个喜好，如果名称录入为空，则停止录入。
# 最后打印所有信息。
# 数据结构：
# {
#    "于谦":["抽烟","喝酒","烫头"]
# }
dict_persons ={}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_persons[name] = []
    while True:
        hobby = input("请输入喜好：")
        if hobby == "":
            break
        dict_persons[name].append(hobby)

for k,v_list_hobby in dict_persons.items():
    print(k+"喜欢：")
    for item in v_list_hobby:
        print(item)



# 24. 将两个列表合并为一个字典。
# 输入：["张无忌","赵敏","周芷若"] [101,102,103]
# 输出：{"张无忌":101,"赵敏":102,"周芷若":103}
list_names = ["张无忌", "赵敏", "周芷若"]
list_rooms = [101, 102, 103]
# dict_result = {}
# for i in range(len(list_names)):
# dict_result[list_names[i]] = list_rooms[i]
dict_result = {list_names[i]: list_rooms[i] for i in range(len(list_names))}
print(dict_result)



# 25. 自定义排序算法，对列表进行升序排列。
# 思路：
#     依次取出元素，与后面进行比较。
#     发现更小的，则交换。
# 输入：[2,8,6,1]
# 输出：[1,2,6,8]
list01 = [2, 8, 6, 1]
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)




# 26. 定义函数，计算多位整数每位相加和.
# 输入：12345
# 输出：15
def each_unit_sum(number):
    """
    计算整数的每位相加和
    :param number:需要操作的数据，int类型
    :return:相加的结果，int类型
    """
    sum_value = 0
    for item in str(number):
        sum_value += int(item)
    return sum_value

re = each_unit_sum(12345)
print(re)




# 27. 定义函数，根据成绩计算等级。
# ​    输入：96
# ​    输出：优秀
# ​    输入：86
# ​    输出：良好
# ​    输入：60
# ​    输出：及格
# ​    输入：50
# ​    输出：不及格
def get_score_level(score):
    if score < 0 or score > 100:
        return "成绩输入有误"
    if 90 <= score:
        return "优秀"
    if 80 <= score:
        return "良好"
    if 60 <= score:
        return "及格"
    return "不及格"

print(get_score_level(95))



# 28. 定义函数，判断列表中是否存在相同元素
# 输入：[3,4,6,8,6]
# 输出：True
def is_repeating(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True
    return False

list01 = [3,4,6,8,7]
print(is_repeating(list01))

