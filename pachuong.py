import requests as rq
# 爬取图片函数
def get_img(name,url):
    try:
        # 发送GET请求获取图片内容
        response = rq.get(url)
        # 以二进制写入模式打开文件
        with open(name+".png", "wb") as f:
            # 将响应内容写入文件
            f.write(response.content)
            print("图片已保存")
    except Exception as e:
        # 打印异常信息
        print(f"An error occurred: {e}")
# print(response.content)
while True:
    name = input("请输入图片名称：")
    url = input("请输入图片url：")
    get_img(name,url)

