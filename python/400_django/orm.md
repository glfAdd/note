```python

            #     # filter_dict['task_create_time__range'] = (task_create_time_begin, task_create_time_end)
            #     filter_dict['task_create_time__lte'] = datetime.strptime(task_create_time_end, "%Y-%m-%d") + timedelta(days=1)

```

## 时间

```python
'''起始时间'''
start = '2022-12-06'
start_year = start.split('-')[0]
start_mouth = start.split('-')[1]
start_day = start.split('-')[2]
start_time = datetime.date(int(start_year),int(start_mouth),int(start_day))
 
'''终止时间'''
end = '2022-12-08'
end_year = end.split('-')[0]
end_mouth = end.split('-')[1]
end_day = end.split('-')[2]
end_time = datetime.date(int(end_year),int(end_mouth),int(end_day))
 
 
# lt：小于2022-12-06
query_filter_list = your_model_name.objects.filter(your_datetime_column__lt=start_time)
# lte：小于等于2022-12-06
query_filter_list = your_model_name..objects.filter(your_datetime_column___lte=start)
# gt：大于2022-12-06
query_filter_list = your_model_name.objects.filter(your_datetime_column___gt=start)
# gte：大于等于2022-12-06
query_filter_list = yourobject.objects.filter(your_datetime_column__gte=start)
# range：查询时间段2022-12-06至2022-12-08
query_filter_list = your_model_name.objects.filter(your_datetime_column__range=(start_time, end_time))
# year：查询2022年
query_filter_list = your_model_name.objects.filter(your_datetime_column__year=int(end_year))
# month：查询12月
query_filter_list = your_model_name.objects.filter(your_datetime_column__month=int(end_mouth ))
# day：查询8号当天
query_filter_list = your_model_name.objects.filter(your_datetime_column__day=int(end_day))
# week_day：星期2
query_filter_list = your_model_name.objects.filter(your_datetime_column__week_day=2)
# 获取今天，昨天，明天的日期，日期格式为yyyy-MM-dd
from django.utils.timezone import now, timedelta
 
date_time = now().date() + timedelta(days=-1)    #昨天
date_time = now().date() + timedelta(days=0)     #今天
date_time = now().date() + timedelta(days=1)     #明天
 
# 获取前一个月，后一个月
import dateutil.relativedelta
import datetime
now = datetime.datetime.now()
 
 
forward_mouth_date = now + dateutil.relativedelta.relativedelta(months=-1)  ## 当前时间前一个月
back_mouth_date = now + dateutil.relativedelta.relativedelta(months=1)      ## 当前时间后一个月
```

