import sys
input = lambda:sys.stdin.readline().strip()
'''
函数名 = lambda 参数 : 表达式
'''
##x = lambda a : a + 10
##print(x(5))
##
##get_mid = lambda nums: nums[len(nums) // 2]
##print(get_mid([1,2,3]))

'''
内置排序算法
sorted()（返回一个排序后的值）
nums.sort()（无返回值，直接作用于列表）
'''
##nums = [1,4,8,9,6,2,3]
##print(sorted(nums))
##print(sorted(nums, reverse = True))
##print(nums)
##nums.sort()
##print(nums)
##
##words = ["apple","banana","cherry","pear"]
##print(sorted(words, key=len))
##words.sort(key=len)
##print(words)
'''
sort中key结合lambda
'''
##words = ["apple","banana","cherry","pear"]
##words.sort(key = lambda a:a[1])
##print(words)
'''
输入
'''
##a, b, c = map(int, input().split())
##print(a, b, c)

##n = int(input()) #输入行数n
##lst = [int(input()) for _ in range(n)] #读取n行整数
##print(lst)

##n, m = map(int, input().split())

'''
列表推导器
'''  
##squares = [i**2 for i in range(1, 11)]
##print(squares)
##evens = [i for i in range(1,20) if i % 2 == 0]
##print(evens)
##input_data = [int(x) for x in input().split()]
##print(input_data)

# 快速斐波那契数列
##n = 10
##fib = [0, 1]
##[fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
##print(fib)

'''
range
惰性序列
'''
##nums = list(range(1,10,2))
##print(nums)

'''
队列
'''
##from collections import deque
##q = deque(range(4))
##x = 4
##q.append(x)
##x = q.popleft()
##print(q)
##print(len(q))
##

'''
栈
'''
##stk = [1,2,3]
##x=4
##stk.append(x)
##x = stk.pop()
##print(stk[-1])

'''
埃氏筛
'''
##
##import math
##n = 100
##primes = []
##is_prime = [True] * (n + 1)
##is_prime[1] = is_prime[0] = False
##
##for i in range(2, int(math.sqrt(n)) + 1):
##    if is_prime[i]:
##        for j in range(i * i, n + 1, i):
##            is_prime[j] = False
##for i in range(2, n + 1):
##    if is_prime[i]: primes.append(i)
##print(primes)
##print(is_prime)


