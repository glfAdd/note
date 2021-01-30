"""
https://www.cnblogs.com/hanfanfan/p/12536946.html

InfluxDB（时序数据库），常用的一种使用场景：监控数据统计。每毫秒记录一下电脑内存的使用情况，然后就可以根据统计的数据，利用图形化界面（InfluxDB V1一般配合Grafana）制作内存使用情况的折线图；
可以理解为按时间记录一些数据（常用的监控数据、埋点统计数据等），然后制作图表做统计；


安装
docker run -d -p 8083:8083 -p 8086:8086 --name influxdb influxdb
"""
