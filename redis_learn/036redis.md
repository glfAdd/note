```python
redis是key-value的数据，所以每个数据都是一个键值对
键的类型是字符串
值的类型分为五种：
	字符串string
	哈希hash
	列表list
	集合set
	有序集合zset

默认有16个库。名字从0 - 15
空用nil表示
--------------------------------------------
/etc/redis
save 900 1		# 900秒1次写操作
save 300 10		# 300秒10次写操作
save 60 10000	# 60秒10000次写操作
满足上面任何一种，就会自动把内从中表的数据写到硬盘上
```

string

```python
string
最大能存储512MB数据
string类型是二进制的，即可以为任何数据，比如数字、图片、序列化对象等

# 设置键值
set key value
# 设置键值及过期时间，以秒为单位
SETEX key seconds value
# 设置多个键值
MSET key value [key value ...]
# 获取。根据键获取值，如果不存在此键则返回nil
GET key
# 根据多个键获取多个值
MGET key [key ...]

运算。value必须是数字
# 将key对应的value加1
INCR key
# 将key对应的value加整数
INCRBY key increment
# 将key对应的value减1
DECR key
# 将key对应的value减整数
DECRBY key decrement
# 追加值。在以前的值后面拼接字符串
APPEND key value
# 获取值长度（字符串长度）
STRLEN key
```

键的命令

```python
# 查找键，参数支持正则
KEYS pattern
key '*1*'
# 判断键是否存在，如果存在返回1，不存在返回0
EXISTS key [key ...]
exists py32
# 查看键对应的value的类型
TYPE key
type py32
# 删除键及对应的值
DEL key [key ...]
# 设置过期时间，以秒为单位。创建时没有设置过期时间则一直存在，直到使用使用DEL移除
EXPIRE key seconds
# 查看有效时间，以秒为单位
TTL key
```

hash

```python
hash用于存储对象，对象的格式为键值对

# 设置单个属性
# key是一组，filed和value时一组
HSET key field value
hset aa name '小明'
# 设置多个属性
HMSET key field value [field value ...]
# 获取一个属性的值
HGET key field
# 获取多个属性的值
HMGET key field [field ...]
# 获取所有属性和值
HGETALL key
# 获取所有的属性
HKEYS key
# 返回包含属性的个数
HLEN key
# 获取所有值
HVALS key
# 判断属性是否存在
HEXISTS key field
# 删除属性及值
HDEL key field [field ...]
# 返回值的字符串长度
HSTRLEN key field
```

list

```python
列表的元素类型为string
按照插入顺序排序
在列表的头部或者尾部添加元素

# 在头部插入数据
LPUSH key value [value ...]
# 在尾部插入数据
RPUSH key value [value ...]
# 在一个元素的前|后插入新元素
LINSERT key BEFORE|AFTER pivot value
# 设置指定索引的元素值。索引是基于0的下标。
# 偏移量也可以是负数，表示偏移量是从list尾部开始计数
LSET key index value

# 移除并且返回 key 对应的 list 的第一个元素
LPOP key
# 移除并返回存于 key 的 list 的最后一个元素
RPOP key
# 返回存储在 key 的列表里指定范围内的元素。start 和 end 偏移量都是基于0的下标
# 偏移量也可以是负数，表示偏移量是从list尾部开始计数
LRANGE key start stop

lpush py3 '123' 'abc' 'hello'
rpush py3 '123' 'abc' 'hello'
linsert py4 after 0 'haha'
lpop py4
lrande py4 0 -1
没有值时key会被删除
获取没有的key返回nil
```

set

```python
无序集合。元素为string类型。元素具有唯一性，不重复
# 添加元素
SADD key member [member ...]
# 返回key集合所有的元素
SMEMBERS key
# 返回集合元素个数
SCARD key
# 求多个集合的交集
SINTER key [key ...]
# 求某集合与其它集合的差集。前后集合顺序不同得到结构也不同
SDIFF key [key ...]
# 求多个集合的合集
SUNION key [key ...]
# 判断元素是否在集合中
SISMEMBER key member

sadd py3 abc 123 hello
smembers py3
scard py3
sinter py3 py4
sdiff py3 py4
sunion py3 py4
sismember py3 hello
```

zset

```python
有序集合。元素为string类型。元素具有唯一性，不重复。每个元素都会关联一个double类型的score，表示权重，通过权重将元素从小到大排序。元素的score可以相同
# 添加
ZADD key score member [score member ...]
# 返回指定范围内的元素
ZRANGE key start stop
# 返回元素个数
ZCARD key
# 返回有序集key中，score值在min和max之间的成员
ZCOUNT key min max
# 返回有序集key中，成员member的score值
ZSCORE key member
```

发布订阅模式

```python
发布者不是计划发送消息给特定的接收者（订阅者），而是发布的消息分到不同的频道。不需要知道什么样的订阅者订阅。
订阅者对一个或多个频道感兴趣，只需接收感兴趣的消息。不需要知道什么样的发布者发布的。
发布者和订阅者的解耦合可以带来更大的扩展性。
客户端发到频道的消息，将会被推送到所有订阅此频道的客户端。
客户端不需要主动去获取消息，只需要订阅频道，这个频道的内容就会被推送过来。

推送消息的格式包含三部分
part1:消息类型，包含三种类型
subscribe，表示订阅成功
unsubscribe，表示取消订阅成功
message，表示其它终端发布消息
如果第一部分的值为subscribe，则第二部分是频道，第三部分是现在订阅的频道的数量
如果第一部分的值为unsubscribe，则第二部分是频道，第三部分是现在订阅的频道的数量，如果为0则表示当前没有订阅任何频道，当在Pub/Sub以外状态，客户端可以发出任何redis命令
如果第一部分的值为message，则第二部分是来源频道的名称，第三部分是消息的内容

# 订阅
SUBSCRIBE 频道名称 [频道名称 ...]
# 取消订阅。如果不写参数，表示取消所有订阅
UNSUBSCRIBE 频道名称 [频道名称 ...]
# 发布
PUBLISH 频道 消息

subscribe py111
publish py111 aaaaaaa
unsubscribe py111
```

主从配置

```python




```

与python交互

```python
sudo pip install redis
--------------------------------------------
# 引入模块
import redis
# 连接
try:
r=redis.StrictRedis(host='localhost',port=6379)
except Exception,e:
print e.message

# 一次执行条命令
r.set('name','hello')
r.get('name')

# pipline缓冲多条命令，然后一次性执行多条命令，减少服务器-客户端之间TCP数据库包，从而提高效率
pipe = r.pipeline()
pipe.set('name', 'world')
pipe.get('name')
pipe.execute()
--------------------------------------------
封装
import redis
class RedisHelper():
    def __init__(self,host='localhost',port=6379):
        self.__redis = redis.StrictRedis(host, port)
    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
    def set(self,key,value):
        self.__redis.set(key,value)
```

登录

```python
输入用户名、密码
密码加密
判断redis中是否记录了用户名，如果有则成功
如果redis中没有用户名，则到mysql中查询
从mysql中查询成功后，将用户名记录到redis中

#encoding=utf-8
from t2 import RedisHelper
from t3 import MysqlHelper
import hashlib

name=raw_input("请输入用户名：")
pwd=raw_input("请输入密码：")

sha1=hashlib.sha1()
sha1.update(pwd)
pwd1=sha1.hexdigest()

try:
    redis=RedisHelper()
    if redis.get('uname')==name:
        print 'ok'
    else:
        mysql=MysqlHelper('localhost',3306,'test1','root','mysql')
        upwd=mysql.get_one('select upwd from userinfos where uname=%s',[name])
        if upwd==None:
            print '用户名错误'
        elif upwd[0]==pwd1:
            redis.set('uname', name)
            print '登录成功'
        else:
            print "密码错误"
except Exception,e:
    print e.message
```

