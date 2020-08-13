"""
安装
pip install qrcode
pip install Image
pip install matplotlib
"""
import qrcode
import requests
from PIL import Image
from io import BytesIO
import os

""" ============================ 简单二维码 """

# 显示网页内容
img = qrcode.make('http://www.baidu.com')
with open('test01.png', 'wb') as f:
    img.save(f)

# 显示文字内容
img = qrcode.make('欢迎来到我的简书')
img.save("test02.png")

""" ============================ 简单二维码 """

data = 'http://www.baidu.com/'
img_file = './test01.png'

qr = qrcode.QRCode(
    # 一个整数，范围为1到40，表示二维码的大小
    version=1,
    # ERROR_CORRECT_L               7%以下的错误会被纠正
    # ERROR_CORRECT_M (default)     15%以下的错误会被纠正
    # ERROR_CORRECT_Q               25 %以下的错误会被纠正
    # ERROR_CORRECT_H.              30%以下的错误会被纠正
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    # boxsize: 每个点（方块）中的像素个数
    box_size=10,
    # 二维码距图像外围边框距离，默认为4，而且相关规定最小为4
    border=4
)
# 传入数据
qr.add_data(data)
qr.make(fit=True)
# 生成二维码
# img = qr.make_image()
img = qr.make_image(fill_color="#696969", back_color="white")
# 保存二维码
img.save(img_file)
# 展示二维码
img.show()

""" ============================ 打开网路图片 """

response1 = requests.get('http://event.img.xindebaby.com/d58667a7a24d5ae226e23d79a5af2687?imageMogr2/auto-orient')
image1 = Image.open(BytesIO(response1.content))
# box = (166, 64, 200, 200)

response2 = requests.get('http://event.img.xindebaby.com/03df83144c613a68368d1bea4e23968b?imageMogr2/auto-orient')
image2 = Image.open(BytesIO(response2.content))

image1.paste(image2, (100, 100), None)
image1.show()

print(os.getcwd())
