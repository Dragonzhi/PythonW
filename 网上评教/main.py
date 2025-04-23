from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0')

# 指定 ChromeDriver 的路径，需替换为你本地的路径
chromedriver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 登录页面的 URL
login_url = 'https://newehall.nwafu.edu.cn/login'
target_url = 'https://newehall.nwafu.edu.cn/jwapp/sys/jwwspj/*default/index.do?t_s=1745400908103&amp_sec_version_=1&gid_=SFhJLzRhY29ZemJEOGIvTmdzQlJFMzlNRHBFcXhYeTRBS3pwT2tuQk4yQ2NuRnAyWXNRMk8yNmRwSHJxc1g2TlptTTM2VmF3a01VZUlPWTRFdWRENHc9PQ&EMAP_LANG=zh&THEME=#/gcpj'

# 登录所需的信息
username = '2024013462'
password = 'zhilong520.'

try:
    # 打开登录页面
    driver.get(login_url)
    # 找到用户名和密码输入框并输入信息
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    username_input.send_keys(username)
    password_input.send_keys(password)
    # 找到登录按钮并点击
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login_submit'))
    )
    login_button.click()
    time.sleep(3)  # 等待页面加载
    # 打开目标页面
    driver.get(target_url)
    time.sleep(3)  # 等待页面加载
    # 显式等待目标元素出现并点击
    # 等待所有卡片加载完成
    cards = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 
            ".bh-card.bh-card-lv1[data-action='查询问卷详情'] .sc-panel-diagonalStrips.sc-panel-warning")
        )
    )
    for i in range(len(cards)):
        # 每次循环都重新定位卡片元素，避免 stale element 问题
        fresh_cards = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 
                ".bh-card.bh-card-lv1[data-action='查询问卷详情'] .sc-panel-diagonalStrips.sc-panel-warning")
            )
        )
        target_div = fresh_cards[i]
        target_div.click()
        try:
            radio_groups = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, ".sc-panel-thingNoImg-1-container.wjzb-card")
                )
            )
            print("radio_groups:", radio_groups)
            if radio_groups:
                radio_groups.pop(-1)
            for index, group in enumerate(radio_groups):
                try:
                    time.sleep(0.5)  # 等待操作完成
                    # print("Group:", group, "index:", index, "len:", len(radio_groups))
                    input_element = WebDriverWait(group, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-x-dasm="完全赞同"]'))
                    )
                    # print("input_element:", input_element)
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
                subjective_textarea.send_keys("教师教学很棒，继续保持！")
                print("主观题输入成功")
            except Exception as e:
                print(f"主观题输入失败: {str(e)}")
            
            # 提交问卷 
            try:
                # 增加等待时间，使用更准确的定位方式
                submit_button = WebDriverWait(driver, 2).until(  # 增加等待时间到 10 秒
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.bh-btn.bh-btn-success.bh-btn-large'))
                )
                
                submit_button.click()
                print("提交按钮点击成功")
                # 等待确认弹窗的确认按钮出现并点击
                confirm_button = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.bh-dialog-btn.bh-bg-primary.bh-color-primary-5'))
                )
                confirm_button.click()
                print("确认提交按钮点击成功")
            except Exception as e:
                print(f"提交按钮出错: {str(e)}")
                
            
        except Exception as e:
            print(f"整体流程出错: {str(e)}")
        time.sleep(5)  # 等待操作完成
    time.sleep(15)  # 等待操作完成
except Exception as e:
    print(f"操作出错: {e}")
finally:
    # 关闭浏览器
    driver.quit()
