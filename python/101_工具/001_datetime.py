"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""
from datetime import datetime, timedelta, date

current_time = datetime.now()
time_str = "2018-12-12"

a = current_time.strftime("%Y-%m-%d %H:%M:%S")
b = (current_time + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
c = datetime.strptime(time_str, "%Y-%m-%d")

# 今天日期
today = date.today()
# 改为当前月第一天
first = today.replace(day=1)
# 减一天，得到上个月的最后一天
last_month = first - timedelta(days=1)


# 日期转为时间戳
import time
tss1 = '2013-10-10'
timeArray = time.strptime(tss1, "%Y-%m-%d")
timeStamp = int(time.mktime(timeArray))
timeStamp