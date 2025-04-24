import tkinter as tk
import random

def show_custom_messagebox(x, y, init_x, init_y, offset_x, offset_y, title, message, duration):
    # 创建一个Toplevel窗口
    top = tk.Toplevel(root)
    top.title(title)
    
    # 设置Toplevel窗口的大小
    top.geometry(f"{x}x{y}")
    
    # 在Toplevel窗口中添加消息内容
    message_label = tk.Label(top, text=message, font=("Arial", 20), bg='white')  # 设置消息标签的背景色为白色，以便文字清晰可见
    message_label.pack(pady=20)
    
    # 定义一个函数来更新窗口位置
    def update_position(i):
        if i < duration:
            # 随机生成新的偏移量
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)
            new_x = init_x + i * offset_x
            new_y = init_y + i * offset_y
            # 确保窗口不会超出屏幕范围
            new_x = max(0, min(new_x, screen_width - x))
            new_y = max(0, min(new_y, screen_height - y))
            top.geometry(f"+{new_x}+{new_y}")
            top.after(50, update_position, i + 1)  # 修改: 将10改为50，减慢动画速度
        else:
            # 随机生成一个短的延迟时间（例如1到3秒）
            delay = random.randint(1000, 3000)
            top.after(delay, top.destroy)  # 在随机延迟后关闭窗口
    
    # 开始动画效果
    update_position(0)

# 创建主窗口
root = tk.Tk()
root.title("主窗口")
root.geometry("400x300")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 定义一个函数来启动放鞭炮效果
def start_fireworks():
    for i in range(25):
        random_x = random.randint(0, screen_width - 300)
        random_y = random.randint(0, screen_height - 200)
        show_custom_messagebox(250, 150, random_x, random_y, 0, 0, "蛇年大吉", "新年快乐", 10)

# 添加一个按钮来启动放鞭炮效果
start_button = tk.Button(root, text="启动放鞭炮", command=start_fireworks)
start_button.pack(pady=20)

# 进入消息循环
root.mainloop()