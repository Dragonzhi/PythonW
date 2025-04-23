

import sys
input = lambda: sys.stdin.readline().strip()
'''
并查集
'''

vowels = {'a', 'e', 'i', 'o', 'u'} 

def count_vowel_substrings(word):
    n = len(word)
    count = 0
    # 遍历所有可能的子字符串起始位置
    for i in range(n):
        # 记录当前子字符串中出现的元音字母
        current_vowels = set()
        # 遍历所有可能的子字符串结束位置
        for j in range(i, n):
            if word[j] in vowels:
                current_vowels.add(word[j])
                # 如果当前子字符串包含全部五种元音
                if len(current_vowels) == 5:
                    count = count + 1
            else:
                # 遇到非元音字母，停止当前子字符串的检查
                break
    return count

word = "cuaieuouac"
print(count_vowel_substrings(word))
