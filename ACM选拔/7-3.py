'''

7-3 仿射密码
分数 10
作者 NWAFU-ACM队
单位 西北农林科技大学
仿射密码是一种简单的代换密码。它通过一个线性函数对字母进行加密和解密。仿射密码的密钥可以用两个参数来定义，这两个参数决定了具体的加密方式。

加密公式
仿射密码的加密公式为：
E(x)=(ax+b)(mod  m)
其中：
x是明文字符对应的数字（在小写英语字母表中A=0, B=1, ..., Z=25）。
a 和b是加密密钥中的两个整数。
m是字符集的大小（对于小写英文字母表，m=26）。
E(x)是加密后的字符对应的数字。

加密过程演示
假设我们要使用英文小写字母作为字符集，且选择a=7和b=3作为密钥。
要加密单词 "hello"：
h−>(7∗7+3)mod26=52mod26=0−>a
e−>(4∗7+3)mod26=31mod26=5−>f
l−>(11∗7+3)mod26=80mod26=2−>c
l−>(11∗7+3)mod26=80mod26=2−>c
o−>(14∗7+3)mod26=101mod26=23−>x
因此，"hello" 被加密为 "afccx"。
给你一对仿射加密的明文与密文，请你破解其加密方式，给出相同仿射加密下另一个密文的明文

输入格式:
第一行给出两个长度相等的字符串，代表某一仿射加密下的一对明文与密文
第二行给出一个被相同的仿射加密所加密的字符串密文

所有字符串保证只含有小写英文字母，长度小于100
保证第一行给出的明文与密文中至少有两个不同字符
保证所有输入中仿射加密的密钥a与26互素（最大公约数为1）
可以证明满足上述条件时解唯一

输出格式:
一个字符串，表示破解出的明文

输入样例:
hello afccx
qbdmndrj
输出样例:
nwafuacm
 

样例解释:
如题干所述，”hello”到”afccx”仿射加密的一个密钥为a=7,b=3。注意到
n:E(13)=(7×13+3)mod  26=94mod  26=16−>q
w:E(22)=(7×22+3)mod  26=157mod  26=1−>b
a:E(0)=(7×0+3)mod  26=3mod  26=3−>d
f:E(5)=(7×5+3)mod  26=38mod  26=12−>m
u:E(20)=(7×20+3)mod  26=143mod  26=13−>n
a:E(0)=(7×0+3)mod  26=3mod  26=3−>d
c:E(2)=(7×2+3)mod  26=17−>r
m:E(12)=(7×12+3)mod  26=87mod  26=9−>j
故”qbdmndrj”的明文为”nwafuacm”
'''

import time
start_time = time.perf_counter()
# 开始答题

from math import gcd

# 读取输入
plaintext, ciphertext = input().split()
encrypted_text = input()

# 找到两个不同的字符对
for i in range(len(plaintext)):
    for j in range(i + 1, len(plaintext)):
        if plaintext[i] != plaintext[j]:
            x1 = ord(plaintext[i]) - ord('a')
            y1 = ord(ciphertext[i]) - ord('a')
            x2 = ord(plaintext[j]) - ord('a')
            y2 = ord(ciphertext[j]) - ord('a')
            break

# 求解 a 和 b
m = 26
# 计算 a 的值
for a in range(1, m):
    if gcd(a, m) == 1 and (a * (x1 - x2)) % m == (y1 - y2) % m:
        break

# 计算 b 的值
b = (y1 - a * x1) % m

# 解密函数
def decrypt(cipher_char, a, b, m):
    cipher_num = ord(cipher_char) - ord('a')
    # 计算 a 的模逆元
    for inv_a in range(1, m):
        if (a * inv_a) % m == 1:
            break
    plain_num = (inv_a * (cipher_num - b)) % m
    return chr(plain_num + ord('a'))

# 解密密文
decrypted_text = ''.join(decrypt(c, a, b, m) for c in encrypted_text)
print(decrypted_text)

# 计算时间
end_time = time.perf_counter()
print(f"\n程序运行时间为：{end_time - start_time} 秒")
