from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# 登录所需的信息
# username = '2024013464'
# password = 'wl060502'

username = input("请输入学号：")
password = input("请输入密码：")

comments = [
    "教师教学很棒！",
    "Good",
    "非常好",
    "好",
    "。"
]

# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0')

# 指定 ChromeDriver 的路径，需替换为你本地的路径
chromedriver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 登录页面的 URL
login_url = 'https://newehall.nwafu.edu.cn/login'
target_url = 'https://newehall.nwafu.edu.cn/jwapp/sys/jwwspj/*default/index.do?t_s=1745427842430&amp_sec_version_=1&gid_=cUdyUURiK1h2RW82K3ZzVVJoeWp3aG0weXNnMlFsekdOZFYzaXRDV00rVVJSOU5IMUFpQjQ1RkwxN012Vkk0TUZEU2hxOVM2UXJlTUYwKzVHQnc5TGc9PQ&EMAP_LANG=zh&THEME=#/pj'



try:
    # 打开登录页面并登录
    driver.get(login_url)
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login_submit'))
    )
    login_button.click()
    time.sleep(2)
    
    # 进入目标页面
    driver.get(target_url)
    time.sleep(3)

    # 循环处理所有未提交的卡片（关键逻辑修改）
    while True:
        try:
            try:
                # 重新获取当前所有未提交的卡片（确保在主页面）
                cards = WebDriverWait(driver, 5).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, 
                            ".bh-card.bh-card-lv1[data-action='查询问卷详情'] .sc-panel-diagonalStrips.sc-panel-warning")
                    )
                )
            except Exception as e:
                print("全部卡片处理完毕")
                break
            # 处理第一个卡片（避免索引错位）
            target_card = cards[0]
            target_card.click()
            time.sleep(2)
            
            # 处理问卷
            try:
                radio_groups = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, ".sc-panel-thingNoImg-1-container.wjzb-card")
                    )
                )
                if radio_groups:
                    radio_groups.pop(-1)  # 排除最后一个主观题
                
                for index, group in enumerate(radio_groups):
                    try:
                        time.sleep(0.4)
                        input_element = WebDriverWait(group, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-x-dasm="完全赞同"]'))
                        )
                        input_element.click()
                        print(f"成功点击第 {index + 1} 个单选题的“完全赞同”选项")
                    except Exception as e:
                        print(f"第 {index + 1} 个单选题出错: {str(e)}")
                
                # 处理主观题
                try:
                    subjective_textarea = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[name="YLCS"]'))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", subjective_textarea)
                    subjective_textarea.send_keys(comments[random.randint(0, len(comments) - 1)]) ###
                    print("主观题输入成功")
                except Exception as e:
                    print(f"主观题输入失败: {str(e)}")
                time.sleep(0.5)
                # 提交问卷
                try:
                    submit_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '.bh-btn.bh-btn-success.bh-btn-large'))
                    )
                    submit_button.click()
                    print("提交按钮点击成功")
                    
                    # 等待确认弹窗并点击确认
                    confirm_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '.bh-dialog-btn.bh-bg-primary.bh-color-primary-5'))
                    )
                    confirm_button.click()
                    print("确认提交按钮点击成功")
                except Exception as e:
                    print(f"提交按钮出错: {str(e)}")
                time.sleep(3)
            except Exception as e:
                print(f"问卷处理出错: {str(e)}")
                driver.back()  # 出错时返回主页面继续尝试
                driver.get(target_url)
                time.sleep(3)
        except Exception as e:
            print(f"循环错误: {str(e)}")
            break
        time.sleep(5)
except Exception as e:
    print(f"操作出错: {e}")
finally:
    driver.quit()