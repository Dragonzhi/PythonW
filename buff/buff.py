import requests
import time
import random
from bs4 import BeautifulSoup
import csv

# 超时时间
TIMEOUT = 10
def getDataJson(goodName, pageNum):
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
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
            "Host": "buff.163.com",
            "Referer": "https://buff.163.com/market/?game=csgo",
            "X-Requested-With": "XMLHttpRequest"
        }
    url = 'https://buff.163.com/market/csgo#game=csgo&page_num=1&rarity=rare_weapon&tab=top-bookmarked'
    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        # 检查数据结构是否正确
        if data.get("data") and data["data"].get("items"):
            return data["data"]["items"]
        else:
            print(f"无效的数据结构: {data}")
            return None
    except Exception as e:
        print(f"请求失败: {e}")
        return None


if __name__ == '__main__':
    print(getDataJson('AK47', 1))