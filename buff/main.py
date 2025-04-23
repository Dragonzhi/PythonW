import requests
from bs4 import BeautifulSoup
import time

# 配置参数
MAX_RETRIES = 3  # 最大重试次数
TIMEOUT = 10     # 超时时间（秒）
DELAY = 5        # 请求间隔（秒）

cookies = {
    # 确保 Cookies 是最新的（从浏览器手动复制）
    'Device-Id': '4yZJQl2lcsMGKKN0FLwY',
    'Locale-Supported': 'zh-Hans',
    'P_INFO': '18117786817|1740819268|1|netease_buff|00&99|null&null&null#sxi&610100#10#0#0|&0|null|18117786817',
    'csrf_token': 'ImUxMDE4YjlhYmRhNzIxMWI2YWYyNDUwNjhhOTdmYWVhY2U2NmYwOGEi.Z8l9_A.3eV_GkJ85HMtWeFvFhxAwxJfjto',
    'game': 'csgo',
    'remember_me': 'U1078929164|4dUa3AWDl2IFzoXJ2SC3Lp2RUFyarGCR',
    'session': '1-GbLHRZlghBz8SjIdIz07dwgwTnFUvb7a6aC9sbMhFVgd2021767252',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'Referer': 'https://buff.163.com/'
}

def fetch_page(page):
    url = f'https://steamcommunity.com/market/search/render/?query=&start={(page-1)*10}&count=10&appid=730&sort_column=popular&sort_dir=desc'
    
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, cookies=cookies, timeout=TIMEOUT)
            response.raise_for_status()  # 检查 HTTP 错误状态码
            return response
        except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
            print(f"第 {page} 页请求失败，重试 {attempt + 1}/{MAX_RETRIES}: {e}")
            time.sleep(DELAY * (attempt + 1))  # 指数退避
    return None

step = 3
for page in range(1, step + 1):
    response = fetch_page(page)
    
    if response and response.status_code == 200:
        try:
            data = response.json()
            html_content = data['results_html']
        except (KeyError, ValueError) as e:
            print(f"解析失败: {e}")
            continue
        
        soup = BeautifulSoup(html_content, 'html.parser')
        skin_names = soup.find_all('span', class_='market_listing_item_name')
        skin_prices = soup.find_all('span', class_='normal_price')
        
        skins = []
        for name, price in zip(skin_names, skin_prices):
            skin_info = {
                'name': name.text.strip(),
                'price': price.text.strip()
            }
            skins.append(skin_info)
        
        for skin in skins:
            print(f"枪皮名称: {skin['name']}, 价格: {skin['price']}")
        
    elif response:
        print(f"第 {page} 页请求失败，状态码: {response.status_code}")
    else:
        print(f"第 {page} 页所有重试均失败")
    
    time.sleep(DELAY)


'''
import requests
from bs4 import BeautifulSoup
import time

cookies = {
    'browserid': '152663339060304660',
    'sessionid': '51e22b2643fa634203e0a531',
    'steamCountry': 'HK%7C38ce54b09b73b283bac85f4bf332cb17',
    'timezoneOffset': '28800,0',
    'ttwid': '1%7CZ9-T6lf-xpNhj1OtlFopg5t3abLR3Ss5nFDrz80UuYg%7C1732291599%7Cabb3e7838ac9cb0bb7a61fa262a78716bfc30f9d98b75dd6ba21cd291711892d'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'Referer': 'https://steamcommunity.com/market/search?appid=730'  # 必须包含 Referer
}

step = 3

for i in range(0, step):  # 注意这里从 0 开始
    # 使用正确的分页参数 start 和 count
    url = f'https://steamcommunity.com/market/search/render/?query=&start={i*10}&count=10&appid=730&sort_column=popular&sort_dir=desc'
    
    response = requests.get(url, headers=headers, cookies=cookies)
    
    if response.status_code == 200:
        try:
            data = response.json()  # 解析 JSON 数据
            html_content = data['results_html']  # 提取 HTML 内容
        except (KeyError, ValueError) as e:
            print(f"解析响应失败: {e}")
            continue
        
        soup = BeautifulSoup(html_content, 'html.parser')
        skin_names = soup.find_all('span', class_='market_listing_item_name')
        skin_prices = soup.find_all('span', class_='normal_price')
        
        skins = []
        for name, price in zip(skin_names, skin_prices):
            skin_info = {
                'name': name.text.strip(),
                'price': price.text.strip()
            }
            skins.append(skin_info)
        
        for skin in skins:
            print(f"枪皮名称: {skin['name']}, 价格: {skin['price']}")
    else:
        print(f'请求失败，状态码: {response.status_code}')
    
    print(f"第 {i+1}/{step} 页完成")
    time.sleep(2)  # 适当增加延迟，避免触发反爬虫

'''
