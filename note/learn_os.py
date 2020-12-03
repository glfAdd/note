import os

# 当前目录上一级
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# 当前目录
print(os.path.dirname(os.path.abspath(__file__)))
# 上上以及
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
