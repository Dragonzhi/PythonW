import requests
import csv
import time

def getDataJson(goodName, pageNum):
    cookies = {
        'Device-Id': '4yZJQl2lcsMGKKN0FLwY',
        'Locale-Supported': 'zh-Hans',
        'NTES_YD_SESS': '7fwtyJkGbUvRN2dIG09hcc.xwc0ZRwqZsWwul8xhlsIfpvFRpWZ9_i_lO9k_X.3UeH_oBjeVrJ1kGCjylJhH7294w3SXiE0AZvcYpzEY6VLTjhKFHAo007NmOYDiX_6orDf77zxx2bhZi7uMW0H6NKugk_TaJFIuyZI98ckYHctQfbtFKWstOX1343FjQfd13miShNHQX9OPhdVwmPfPdnMZ6qlZAnjHu_d_eW_q0JtrN',
        'P_INFO': '18117786817|1740819268|1|netease_buff|00&99|null&null&null#sxi&610100#10#0#0|&0|null|18117786817',
        'S_INFO': '1740819268|0|0&60##|18117786817',
        'csrf_token': 'IjI0YmQ3MjgwM2JmYmU3MGFkYzUwM2ZjOTAwY2UwOGVmODAwMDE0N2Qi.Z8LLeA.oQfKo-E5VZZlOk7k54XkbExURzM',
        'game': 'csgo',
        'remember_me': 'U1078929164|4dUa3AWDl2IFzoXJ2SC3Lp2RUFyarGCR',
        'session': '1-gIlrDv7MVdYypPuuNI0zaJwcpe-kiYpXQ8KXGh8fr5Jm2021767252'
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Host": "buff.163.com",
        "Referer": "https://buff.163.com/market/?game=csgo",
        "X-Requested-With": "XMLHttpRequest"
    }

    url_init = f"https://buff.163.com/api/market/goods?game=csgo&page_num={pageNum}&category_group={goodName}"
    try:
        res = requests.get(url_init, headers=headers, cookies=cookies, timeout=10)
        res.raise_for_status()
        data = res.json()
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
    goodInfo = {
        "pistol": 116,  # 手枪
        "rifle": 128,   # 步枪
        "smg": 79,      # 冲锋枪
        "shotgun": 45,   # 散弹枪
        "machinegun": 15,
        "sticker": 187
    }

    # 初始化CSV文件并写入标题行
    with open("csgoData.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "名称", "销售数量", "Steam价格", "最低售价", "价格比例"])
    
    for key, total_pages in goodInfo.items():
        print(f"正在处理分类: {key}，总页数: {total_pages-1}")
        for page in range(1, total_pages):
            print(f"请求第 {page} 页...")
            data = getDataJson(key, page)
            if not data:
                print(f"第 {page} 页无数据，跳过")
                continue

            try:
                with open("csgoData.csv", "a", newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    for item in data:
                        steam_price = item.get("goods_info", {}).get("steam_price", "N/A")
                        sell_min_price = item.get("sell_min_price", "N/A")
                        # 处理可能的除零错误或无效值
                        if steam_price in [None, "N/A", 0] or sell_min_price in [None, "N/A"]:
                            ratio = "N/A"
                        else:
                            ratio = float(sell_min_price) / float(steam_price)
                        writer.writerow([
                            item.get("id"),
                            item.get("name"),
                            item.get("sell_num"),
                            steam_price,
                            sell_min_price,
                            ratio
                        ])
                print(f"第 {page} 页写入完成")
            except Exception as e:
                print(f"写入第 {page} 页时出错: {e}")
            finally:
                time.sleep(10)  # 遵守爬虫礼仪，避免过快请求