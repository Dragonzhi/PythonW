# num = input("输入一个数字：")
# #尝试
# try:
#     print(1+num)
# except Exception as e:
#     print(e)
# print("yes")


'''
#类和对象


class Moneygiving:
    def __init__(self,wekkend = False, chlid = False):
        self.money = 100
        if wekkend:
            self.inc = 1.2
        else :
            self.inc = 1
        if chlid:
            self.discount = 0.5
        else :
            self.discount = 1
    def calcPrice(self, num):
        return self.money * self.inc * self.discount * num
    
#传递内容
adult = Moneygiving(wekkend=True)
chlid = Moneygiving(chlid=True,wekkend=True)
#传递参数
mon = adult.calcPrice(2) + chlid.calcPrice(1)
time.sleep(2)
print(mon)
'''


for i in range(1, 10):
    url = f'https://steamcommunity.com/market/search?appid=730#p{i}_popular_desc'
    print(url)