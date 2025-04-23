from datetime import date, timedelta

def sum_of_digits(n):
    """计算一个整数的数位和"""
    return sum(int(digit) for digit in str(n))

def count_special_dates(start_year, end_year):
    """计算满足条件的日期数量"""
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)
    current_date = start_date
    count = 0

    while current_date <= end_date:
        try:
            year_sum = sum_of_digits(current_date.year)
            month_sum = sum_of_digits(current_date.month)
            day_sum = sum_of_digits(current_date.day)

            if year_sum == month_sum + day_sum:
                count += 1
            if current_date.year != 9999:
                current_date += timedelta(days=1)
        except OverflowError:
            # 若出现溢出错误，打印错误信息并退出循环
            print(f"日期溢出错误，当前日期: {current_date}")
            break

    return count

# 计算从1900年1月1日到9999年12月31日满足条件的日期数量
result = count_special_dates(1900, 9999)
print(result)
