import subprocess
import time
import math
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

def show_debug_window(img, bg_color, target_x, target_y, threshold):
    """显示调试窗口"""
    img_np = np.array(img)
    plt.imshow(img_np)
    
    # 绘制背景区域（顶部10行）
    plt.axhline(y=9, color='red', linestyle='--', label='Background Area')
    
    # 绘制目标点
    plt.scatter(target_x, target_y, c='red', s=50, marker='x', label='Target Point')
    
    # 绘制阈值提示
    plt.title(f"Threshold={threshold} | BG Color={bg_color}")
    
    plt.legend()
    plt.show(block=False)  # 非阻塞显示
    plt.pause(1)  # 显示1秒
    plt.close()
# ADB操作函数
def adb(command):
    result = subprocess.call(command, shell=True)
    if result != 0:
        print(f"ADB command failed: {command}")
    return result

# 按压时间系数（需根据设备调试）
PRESS_COEFFICIENT = 1.25

# 获取手机截图
def get_screenshot():
    try:
        # 直接获取二进制流数据
        screenshot_data = subprocess.check_output(
            "adb exec-out screencap -p", 
            shell=True,
            stderr=subprocess.DEVNULL
        )
        img = Image.open(BytesIO(screenshot_data))
        # img.save("./screen.png")  # 可选：仍保存文件供调试
        return img
    except Exception as e:
        print(f"Screenshot failed: {str(e)}")
        return None
def get_background_color(img):
    """优化背景色获取：取顶部中间区域（避免边缘渐变干扰）"""
    w, h = img.size
    start_y = h // 20    # 从顶部1/20处开始取样
    end_y = start_y + 20 # 取20行进行平均
    r_total = 0
    g_total = 0
    b_total = 0
    count = 0
    for y in range(start_y, end_y):
        for x in range(w):
            pixel = img.getpixel((x, y))
            r_total += pixel[0]
            g_total += pixel[1]
            b_total += pixel[2]
            count += 1
    return (
        r_total//count, 
        g_total//count, 
        b_total//count
    )
def find_target_position(img, bg_color, threshold=60, min_ratio=0.25):
    """检测屏幕顶部第一个颜色差异显著的方块"""
    w, h = img.size
    y1, y2 = None, None
    
    # 仅扫描屏幕顶部区域（前1/3高度）
    scan_height = h // 3
    for y in range(scan_height):
        diff_count = 0
        for x in range(w):
            pixel = img.getpixel((x, y))
            total_diff = abs(pixel[0]-bg_color[0]) + \
                         abs(pixel[1]-bg_color[1]) + \
                         abs(pixel[2]-bg_color[2])
            if total_diff > threshold:
                diff_count += 1
        
        # 判断差异比例是否超过阈值
        if diff_count / w > min_ratio:
            if y1 is None:
                y1 = y  # 记录顶部位置
            y2 = y     # 持续记录到底部位置
        else:
            # 允许短暂中断后继续检测
            if y2 is not None and y - y2 < 5:  # 允许最多5行中断
                continue
            else:
                if y1 is not None and y2 is not None:
                    break  # 完全终止扫描
        
        # 若已找到有效区域且高度足够，提前终止
        if y1 is not None and y2 is not None and (y2 - y1) > h//20:
            break
    
    if y1 is None or y2 is None:
        return 0, 0
    
    # 目标点优化：取底部行的中间位置
    target_y = y2  # 直接取底部行
    # 或取底部偏下的位置：
    # target_y = y2 + (h//100)
    
    # 水平方向取差异最大的点（在顶部行y1）
    max_diff_x = 0
    max_diff = 0
    for x in range(w//4, 3*w//4):  # 水平中间区域扫描
        pixel = img.getpixel((x, y1))
        total_diff = abs(pixel[0]-bg_color[0]) + \
                     abs(pixel[1]-bg_color[1]) + \
                     abs(pixel[2]-bg_color[2])
        if total_diff > max_diff:
            max_diff = total_diff
            max_diff_x = x
    
    target_x = max_diff_x
    return target_x, target_y
# 分析图像获取坐标
def find_positions(img):
    if img is None:
        return 0, 0, 0, 0
    
    w, h = img.size
    bg_color = get_background_color(img)  # 获取背景色
        
    # 寻找棋子底部坐标（示例逻辑）
    piece_x_sum = 0
    piece_x_c = 0
    piece_y_max = 0
    for i in range(h//3, 2*h//3):
        for j in range(w):
            pixel = img.getpixel((j, i))
            # 根据棋子颜色特征判断（需调整）
            if 50 < pixel[0] < 60 and 53 < pixel[1] < 63 and 95 < pixel[2] < 110:
                piece_x_sum += j
                piece_x_c += 1
                piece_y_max = max(i, piece_y_max)
    
    if piece_x_c == 0:
        return 0, 0, 0, 0
    
    piece_x = piece_x_sum // piece_x_c
    piece_y = piece_y_max

    
    # 新增目标点检测
    target_x, target_y = find_target_position(img, bg_color)
    

    return piece_x, piece_y, target_x, target_y

# 执行跳跃
def jump(distance):
    press_time = distance * PRESS_COEFFICIENT
    press_time = int(press_time)
    adb(f"adb shell input swipe 500 500 500 500 {press_time}")

# 主循环
while True:
    img = get_screenshot()
    if img is None:
        print("Failed to get screenshot, retrying...")
        time.sleep(2)
        continue
    # 手动调整参数（示例：在循环中输入新阈值）
    threshold = float(input("Enter threshold (default 50): ") or 50)
    
    bg_color = get_background_color(img)
    target_x, target_y = find_target_position(img, bg_color, threshold)
    
    # 显示调试窗口
    show_debug_window(img, bg_color, target_x, target_y, threshold)
    
    x1, y1, x2, y2 = find_positions(img)
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        print("Failed to find positions, retrying...")
        time.sleep(2)
        continue
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    jump(distance)
    time.sleep(0.8)  # 等待落地