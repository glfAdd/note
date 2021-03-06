"""
快速停止：立刻停止当前nginx处理的所有网路请求，马上丢弃链接停止工作
平缓停止：允许nginx讲当前正在处理的网络请求处理完成，但不在接受新的请求，之后关闭链接停止工作。
平缓重启：首先读取新的配置文件检测语法是否正确，如果正确则平缓关闭久服务重启新服务，如果不正确依旧使用旧的。
平缓升级:

pkill nginx								强制关闭

nginx                   启动
nginx -s relaod     重启
nginx -s stop       停止
nginx -s quit							优雅停止服务

nginx -t								检测配置文件语法错误，同时会显示主配置文件路径
nginx -v								版本号
nginx -V								看编译选项
nginx -h
"""
