import pygame as pg
import random as rd

pg.init()

WIDTH = 1680
HEIGHT = 900
font_size = 21


screen = pg.display.set_mode((WIDTH, HEIGHT))

# 渐变效果
bg_face = pg.Surface((WIDTH, HEIGHT), flags = pg.SRCALPHA)
pg.Surface.convert(bg_face)

bg_face.fill(pg.Color(0,0,0,15))


# 设置窗口标题
pg.display.set_caption("My Game")

words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','"','\'','<','>','.','/','?','\\','|','~',']','`','~','，','。','、','；','：','？','！','@','#','￥','%','&','*','（','）','—','+','=','【','】','{','}','；','：','“','‘','<','>','.','/','？','\\','|','~']
# words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# words = ['华','风','夏','韵','洛','水','天','依']
# photo = pg.image.load("pygame try/12周年.jpg")

font = pg.font.SysFont("SimHei", font_size)
texts = []

# 生成文字列表
for i in words:
    # 随机颜色
    color = (rd.randint(0, 66), rd.randint(0, 144), rd.randint(0, 255))
    # 渲染文字
    text = font.render(i, True, (102, 204, 255))
    texts.append(text)

lines = int(WIDTH/font_size) + 1
drops = []
for a in range(lines):
    drops.append(0)


while True:
    # 绘制渐变背景
    screen.blit(bg_face, (0,0))
    # 下降效果
    for i in range(lines):
        text = rd.choice(texts)
        screen.blit(text, (i*font_size, drops[i]*font_size))
        drops[i] += 1
        # 回去
        if drops[i] * font_size > HEIGHT and rd.random() > 0.95:
            drops[i] = 0
    # 刷新屏幕
    pg.display.flip()
    # 延迟
    pg.time.delay(44)

    # 退出游戏
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    
    