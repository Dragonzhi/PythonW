# https://mirrors.tuna.tsinghua.edu.cn/

from bs4 import BeautifulSoup
import requests as rq
import time
url = 'https://pic.netbian.com/4kdongman/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}
response = rq.get(url = url, headers = headers)
response.encoding = 'gbk'
text = response.text
soup = BeautifulSoup(text, 'html.parser')
# 解析
img_list = soup.select('.slist img')

for i in img_list:
    img_src = 'https://pic.netbian.com/'+i['src']
    response = rq.get(url = img_src)
    # name
    img_name = i['alt'].replace('*', 'x')
    
    # 保存图片
    with open(f"./动漫/{img_name}.jpg", 'wb') as f:
        f.write(response.content)
    print(img_name, '下载成功')
    time.sleep(0.2)




'''
url = 'https://www.shicimingju.com/book/xiyouji.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

response = rq.get(url = url, headers = headers)
response.encoding = 'utf-8'
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')
# retusl = soup.find('div', class_='items')
xiyouji = []

a_list_url = soup.select('.tabli')
for a in a_list_url:
    title = a.text
    
    detial_url = 'https://www.shicimingju.com/'+a['href']
    detial_res = rq.get(url = detial_url, headers = headers)
    detial_res.encoding = 'utf-8'

    detial_soup = BeautifulSoup(detial_res.text, 'html.parser')
    detial = detial_soup.find('div', class_='text p_pad').text
    
    dic = {'章节':title, '内容':detial}

    xiyouji.append(dic)
    print(xiyouji)
# 转换数据为DataFrame
# df = pd.DataFrame(xiyouji)
# df.to_excel("西游记.xlsx",index=False)
# print("done")
'''

'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'


