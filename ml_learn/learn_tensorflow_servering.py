""" ============================ docker 环境
docker pull tensorflow/serving
git clone https://github.com/tensorflow/serving
TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"
docker run -t --rm -p 8501:8501 -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" -e MODEL_NAME=half_plus_two tensorflow/serving &
    -p 8500:8500 -p 8501:8501 用于绑定rpc和rest端口。
    -v /home/zhi.wang/tensorflow-serving/model:/models 用于绑定目录映射。
    -e MODEL_NAME=wdl_model指定TFS加载模型名字，和目录tensorflow-serving/model下的模型名字保持一致， 如/home/zhi.wang/tensorflow-serving/model/wdl_model。
    --enable_batching=true 设置TFS开启batch功能。
    --batching_parameters_file=/models/batching_parameters.txt 绑定批量参数。
    --mount：   表示要进行挂载
    source：    指定要运行部署的模型地址， 也就是挂载的源，这个是在宿主机上的servable模型目录（pb格式模型而不是checkpoint模型）
    target:     这个是要挂载的目标位置，也就是挂载到docker容器中的哪个位置，这是docker容器中的目录，模型默认挂在/models/目录下，如果改变路径会出现找不到model的错误
    -t:         指定的是挂载到哪个容器
    -d:         后台运行
    -p:         指定主机到docker容器的端口映射
    -e:         环境变量
    -v:         docker数据卷
    --name:     指定容器name，后续使用比用container_id更方便
    docker run: 启动这个容器并启动模型服务（这里是如何同时启动容器中的模型服务的还不太清楚）


# 将source目录中的例子模型，挂载到-t指定的docker容器中的target目录，并启动
# docker run -d -p 8501:8501 --mount type=bind,source=/root/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu/,target=/models/half_plus_two -e MODEL_NAME=half_plus_two -t --name testserver tensorflow/serving

curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://localhost:8501/v1/models/half_plus_two:predict



TensorFlow主要有三种模型格式, 可以互相转换
    CheckPoint格式在训练模型时候每隔几轮保存一次，以方便增量训练
    GraphDef格式适用于python、java的tensorflow库进行加载
    SavedModel是TensorFlow-Serving要求的格式



"""
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
""" ============================ """
