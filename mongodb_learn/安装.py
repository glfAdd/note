""" ============================ 安装
官网
https://www.mongodb.com/download-center/community


https://www.howtoing.com/install-mongodb-on-debian
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org.list
echo "deb http://deb.debian.org/debian/ stretch main" | sudo tee /etc/apt/sources.list.d/debian-stretch.list
apt-get install update
apt-get install libcurl3
apt-get install mongodb-org
"""

""" ============================ 命令
默认端口27017
 
systemctl status mongod
systemctl stop mongod
systemctl start mongod
systemctl restart mongod
systemctl disable mongod
systemctl enable mongod
"""

""" ============================ 配置 
默认只能127.0.0.1访问, 多个ip之间用 , 分隔
允许任何ip访问 bind_ip = 0.0.0.0

vim /etc/mongod.conf

# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1,your_server_ip
"""
