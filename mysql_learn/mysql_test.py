import torndb
import datetime

m = torndb.Connection(host='47.107.209.33:3306',
                      database='book',
                      user='root',
                      password='8NjJKEbe',
                      max_idle_time=0.9 * 60 * 60,
                      time_zone='+8:00')

res = {
    'body': {
        'total_price': 10.2,
        'pnr': 'NNNNNN',
        'currency': 'CNY',
    }
}
sql_select = "select * from t_reserve_order_split_hold where reserve_order_split_id=759394"
r_select = m.query(sql_select)[0]
r_select['pnr'] = res['body']['pnr']
r_select['ori_currency'] = res['body']['currency']
r_select['cost_price'] = res['body']['total_price']
r_select['ori_cost_price'] = res['body']['total_price']
r_select['flight_price'] = res['body']['total_price']
r_select['ori_flight_price'] = res['body']['total_price']
r_select['is_history'] = 0
r_select['exchange_rate'] = 1

keys = []
values = []
for key, value in r_select.items():
    if key == 'id':
        continue
    if value:
        keys.append(key)
        values.append('%s' % value)
keys = ",".join(keys)
values = "'" + "','".join(values) + "'"
sql_insert = "insert into t_reserve_order_split_hold (%s) values (%s)" % (keys, values)
m.execute(sql_insert)
