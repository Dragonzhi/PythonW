
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 原代码部分


url = 'https://www.wjx.cn/vm/Om6DYub.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    "Cookie": "acw_tc=0aef815717429897527084251e00e1ef2f0766dae472615a0636d7d7523084; .ASPXANONYMOUS=we6C7tbU2wEkAAAAYzRmYzFmYTMtNmFmOC00Y2UwLWEwZDEtOGZmM2I4NjAxNGI3CttpzNWn3XPX23d6njPBuyBX-BQ1; jac307786112=69958606; SERVERID=ec48383874998d7d7994224bf7acd1b0|1742990257|1742989752; tfstk=gsYStDsox827NJyDZYhVGGAVBCbIQpgZAW1psBUz9aQ8pJdO38RU8BBBAtdN4TQkaoCD4CGhv0Xy9WQku3zFUYbB9d7IQAuZ7QAlKwHZQ9yNROQd92WK0gHbkc4EQAuZuQAl-wHwUxvVBL5hH_eLyghjk_WA9zpdeieAt6bdppppMj1hH9QdJpQxdeyNOXWWNbIe8S8fyOdRhyUQs_sRBVXbJyLfNRW9wf4LJE15VefhOraR4HdGjU8-Rrby1nQAiek0y9tA1B7XRY4PKaCGjhSbebfyvIxdEFMQ5TLkce_2Wv4wCLJv7w8-To9OATtvyiNLJZ7WcptCW-hcaHdDvTYsdP6JrItNA3D_jdd2_UjDRAwAK35GksYEnzBBD6IrCPW17bqQGG4CGOljGkq3UAZygRNoCTSRi__jGjw5kgCcGOljGkqh2sf4cjGbFZC..; ssxmod_itna=YqUxnDcGDtitwhDl8DCxDT1Yx2CK==HqQwkqkCDl2hYxA5D8D6DQeGTbuKdHWwYUAiaiDunh0P4jUD0Ip=BjbnRdfl2r4GLDmKDy3UojeDx1q0rD74irDDxD3vxlICDvxG=DpxGp9Dj4GSUqGcDYQX8ww334qBD73DUwdDQqDSCQI4xGjlDiU9DGAlD0tUD7jlzeiDeMPNpqGWGM4D0M+kXAIdD1=7h6XYElRQglT=MmLrZeFaIutZ8qGmlRn3GuOlRqF3QiPYm0vxFi4e7EYtC0Gd3foqm7hx3RDbiBxoWNEBMrZtDXVdDDWAw4WiDD; ssxmod_itna2=YqUxnDcGDtitwhDl8DCxDT1Yx2CK==HqQwkqqD6p+DQqDseQDLnS=M/tQNC1=dMP5qMDn4DkYQuu+HPZ779uAU8Bmu2OVi0g35EsgSQSN+tkE6K4hG22x2rhXpzlkLx4Z6ncjwoUCKelQwxD/n=VCyaE22PF=iFPci=DzWmCGI+laWW3UuNdA4Dw2xYomHsqhuYdOS8Cla1YjSte0xDLxG7D+E5eYD=="
}

browser = webdriver.Chrome()
browser.get(url)
print(browser.page_source)
time.sleep(0.5)
# 姓名
browser.find_element(By.ID, 'q1').send_keys('cxq')
time.sleep(1.5)
# 学院
browser.find_element(By.ID, 'q2').send_keys('麻醉学院吗')
time.sleep(0.5)
# 学号
browser.find_element(By.ID, 'q3').send_keys('114514')
time.sleep(1.5)
# 联系方式
browser.find_element(By.ID, 'q4').send_keys('1919810')

time.sleep(15)
browser.quit()
