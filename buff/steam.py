import requests
import time
import random
from bs4 import BeautifulSoup
import csv

cookies = {
    'browserid': '152663339060304660',
    'sessionid': '4c64a265e71dc3326e90b29a',
    'steamCountry': 'HK%7Cf73b6f65cdef45b7fe612f116dec4899',
    'timezoneOffset': '28800,0',
    'ttwid':'1%7CZ9-T6lf-xpNhj1OtlFopg5t3abLR3Ss5nFDrz80UuYg%7C1732291599%7Cabb3e7838ac9cb0bb7a61fa262a78716bfc30f9d98b75dd6ba21cd291711892d'
}
cookies_ = {
    'browserid': '152663339060304660',
    'sessionid': '4c64a265e71dc3326e90b29a',
    'steamCountry': 'HK%7Cf73b6f65cdef45b7fe612f116dec4899',
    'timezoneOffset': '28800,0',
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-Requested-With': 'XMLHttpRequest'  # 模拟AJAX请求
}

def safe_find(element, selector, attribute='text'):
    """安全元素查找函数（优化版）"""
    try:
        result = element.select_one(selector)
        if not result:
            return None
        # 提取价格时只取第一个价格值
        if 'market_listing_price_with_fee' in selector:
            price_text = result.get_text(strip=True)
            return price_text.split(' ')[0]  # 提取主价格部分
        return result.get_text(strip=True) if attribute == 'text' else result.get(attribute, '')
    except Exception as e:
        print(f"元素解析失败: {str(e)}")
        return None

def get_market_page(page_num, per_page=10):
    """获取指定页面的市场数据（包含完整过滤参数）"""
    base_url = "https://steamcommunity.com/market/search/render/"
    
    # 构造包含完整过滤条件的参数（关键修改点）
    params = {
        "query": "",
        "start": (page_num-1)*per_page,
        "count": per_page,
        "appid": 730,
        "sort_column": "popular",
        "sort_dir": "desc",
        "category_730_ItemSet[]": "any",
        "category_730_ProPlayer[]": "any",
        "category_730_StickerCapsule[]": "any",
        "category_730_Tournament[]": "any",
        "category_730_TournamentTeam[]": "any",
        "category_730_Type[]": "any",
        "category_730_Weapon[]": "any",
        # 关键过滤参数：军规级+受限级
        "category_730_Rarity[]": ["tag_Rarity_Rare_Weapon", "tag_Rarity_Mythical_Weapon"]  
    }

    try:
        response = requests.get(base_url, params=params, headers=HEADERS, cookies=cookies)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"请求失败: {str(e)}")
        return None
def parse_item_detail(item_url):
    """优化后的详情解析函数"""
    try:
        # 使用带Cookie的会话保持登录状态
        session = requests.Session()
        session.cookies.update(cookies)
        response = session.get(item_url, headers=HEADERS, timeout=10)
        
        # 验证响应状态
        if response.status_code != 200:
            print(f"请求失败，状态码：{response.status_code}")
            return None, None

        # 保存原始HTML用于调试
        with open('debug_page.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        soup = BeautifulSoup(response.text, 'lxml')
        
        # 精确提取磨损值（新版选择器）
        wear_div = soup.find('div', class_='descriptor', string=lambda t: t and 'Exterior:' in t)
        wear = wear_div.text.split(':', 1)[-1].strip() if wear_div else "N/A"
        
        # 精确提取收藏品（通过颜色特征）
        collection_div = soup.find('div', class_='descriptor', style=lambda s: s and 'color: #9da1a9' in s)
        collection = collection_div.text.strip() if collection_div else "未知来源"
        
        return wear, collection
    except Exception as e:
        print(f"详情解析失败: {str(e)}")
        return "N/A", "未知来源"
    
def main():
    pages = int(input("请输入要爬取的页数："))
    all_items = []

    for page in range(1, pages+1):
        print(f"正在爬取第 {page} 页...")
        data = get_market_page(page)
        
        if not data or 'results_html' not in data:
            print(f"第 {page} 页数据获取失败")
            continue

        soup = BeautifulSoup(data['results_html'], 'lxml')
        items = soup.select('a.market_listing_row_link')

        for item in items:
            try:
                # print(item)
                # 使用更严格的选择器
                name = safe_find(item, 'span.market_listing_item_name')
                price = safe_find(item, 'span.normal_price')
                # detail_url = safe_find(item, 'a.market_listing_row_link', 'href')

                # 直接从 item 中获取 href 属性
                detail_url = item.get('href')
                # print(detail_url)

                # 关键修改：已通过URL参数过滤，移除了品质检查
                if not all([name, price, detail_url]):
                    print(f"数据不完整，跳过：{name}")
                    continue

                # 获取磨损值（增加随机延迟）
                time.sleep(random.uniform(3, 5))
                wear,collection = parse_item_detail(detail_url)

                all_items.append({
                    '武器名称': name,
                    'steam价格': price,
                    '磨损程度': wear,
                    '收藏品来源': collection  # 新增字段
                    })

                print(f"已获取：{name}")
            except Exception as e:
                print(f"处理商品时出错：{str(e)}")
                continue

    # 在数据存储部分添加新字段
    with open('csgo_skins.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['武器名称', 'steam价格', '磨损程度', '收藏品来源'])
        writer.writeheader()
        writer.writerows(all_items)
    print(f"数据已保存，共获取{len(all_items)}条记录")

if __name__ == "__main__":
    main()