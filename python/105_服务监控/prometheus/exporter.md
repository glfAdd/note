##### 通用规范

- 行以 # HELP 开始解析得到指标名称以及相应的说明信息

  ```
  # HELP <metrics_name> <doc_string>
  ```

- 行以 # TYPE 开始解析得到当前的指标名称以及指标类型, 如果没有明确的指标类型需要返回为 untyped

  ```
  # TYPE <metrics_name> <metrics_type>
  ```

- 本格式规范

  ```
  1. metric_name 和 label_name 必须遵循PromQL的格式规范要求
  2. 具有相同 metric_name 的样本必须按照一个组的形式排列，并且每一行必须是唯一的指标名称和标签键值对组合
  3. value是一个float格式的数据
  4. timestamp的类型为int64毫秒时间戳, 默认为当前时间
  
  metric_name [
    "{" label_name "=" `"` label_value `"` { "," label_name "=" `"` label_value `"` } [ "," ] "}"
  ] value [ timestamp ]
  ```

- 示例

  ```
  # HELP node_cpu Seconds the cpus spent in each mode.
  # TYPE node_cpu counter
  node_cpu{cpu="cpu0",mode="idle"} 362812.7890625
  # HELP node_load1 1m load average.
  # TYPE node_load1 gauge
  node_load1 3.0703125
  ```

##### histogram 和 summary 类型样本规则

```
1. 类型为summary或者histogram的指标x，该指标所有样本的值的总和需要使用一个单独的x_sum指标表示
2. 类型为summary或者histogram的指标x，该指标所有样本的总数需要使用一个单独的x_count指标表示。
3. 对于类型为summary的指标x，其不同分位数quantile所代表的样本，需要使用单独的x{quantile="y"}表示。
4. 对于类型histogram的指标x为了表示其样本的分布情况，每一个分布需要使用x_bucket{le="y"}表示，其中y为当前分布的上位数。同时必须包含一个样本x_bucket{le="+Inf"}，并且其样本值必须和x_count相同。
5. 对于histogram和summary的样本，必须按照分位数quantile和分布le的值的递增顺序排序。
```

- 示例

  ```
  # A histogram, which has a pretty complex representation in the text format:
  # HELP http_request_duration_seconds A histogram of the request duration.
  # TYPE http_request_duration_seconds histogram
  http_request_duration_seconds_bucket{le="0.05"} 24054
  http_request_duration_seconds_bucket{le="0.1"} 33444
  http_request_duration_seconds_bucket{le="0.2"} 100392
  http_request_duration_seconds_bucket{le="+Inf"} 144320
  http_request_duration_seconds_sum 53423
  http_request_duration_seconds_count 144320
  
  # Finally a summary, which has a complex representation, too:
  # HELP rpc_duration_seconds A summary of the RPC duration in seconds.
  # TYPE rpc_duration_seconds summary
  rpc_duration_seconds{quantile="0.01"} 3102
  rpc_duration_seconds{quantile="0.05"} 3272
  rpc_duration_seconds{quantile="0.5"} 4773
  rpc_duration_seconds_sum 1.7560473e+07
  rpc_duration_seconds_count 2693
  ```

##### 指定样式格式的版本

```
在Exporter响应的HTTP头信息中，可以通过Content-Type指定特定的规范版本
version用于指定Text-based的格式版本，当没有指定版本的时候，默认使用最新格式规范的版本
HTTP响应头还需要指定压缩格式为gzip

HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Length: 2906
Content-Type: text/plain; version=0.0.4
Date: Sat, 17 Mar 2018 08:47:06 GMT
```



