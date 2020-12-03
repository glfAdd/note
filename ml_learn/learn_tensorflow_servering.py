""" ============================
TensorFlow主要有三种模型格式, 可以互相转换
    CheckPoint格式在训练模型时候每隔几轮保存一次，以方便增量训练
    GraphDef格式适用于python、java的tensorflow库进行加载
    SavedModel 是TensorFlow-Serving要求的格式
"""

""" ============================ tensorflow serving
官网文档
https://tensorflow.google.cn/tfx/serving/docker?hl=zh-cn

# 拉取 docker 镜像
docker pull tensorflow/serving 

# clong tensorflow serving
git clone https://github.com/tensorflow/serving

# 启动 docker
TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"
# docker run -t --rm -p 8501:8501 -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" -e MODEL_NAME=half_plus_two tensorflow/serving &
docker run -t --name tf_test -p 8501:8501 -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" -e MODEL_NAME=half_plus_two tensorflow/serving &
    -p          8500:8500 -p 8501:8501 用于绑定grpc和rest端口(把本地8888端口映射到容器中的9999端口中去)
    -v          /home/zhi.wang/tensorflow-serving/model:/models 用于绑定目录映射。
    -e          MODEL_NAME=wdl_model指定TFS加载模型名字，和目录tensorflow-serving/model下的模型名字保持一致， 如/home/zhi.wang/tensorflow-serving/model/wdl_model。
    --mount：   表示要进行挂载
    --rm        停止docker后自动删除镜像
    --name      指定容器名称
    source：    指定要运行部署的模型地址， 也就是挂载的源，这个是在宿主机上的模型目录
    target:     挂载到docker中的哪个位置
    -t:         挂载到哪个容器
      
# 测试是否成功
curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://localhost:8501/v1/models/half_plus_two:predict 

# 分析
source 是模型的目录 /home/glfadd/Desktop/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu

└── 00000123                                    # 模型版本
    ├── assets                                  
    │   └── foo.txt
    ├── saved_model.pb
    └── variables
        ├── variables.data-00000-of-00001
        └── variables.index

# 进入模型
docker exec -it tf_test bash

# 将导出的模型导入到运行的容器中
docker cp 模型路径 容器ID：路径

# 以后台运行方式开启一个tensorflow/serving的守护进程
docker run -d --name serving_base tensorflow/serving
# 复制本地SavedModel到容器存放models的文件夹下
docker cp ./model serving_base:/models/model
# docker commit提交修改制作新镜像my_model_0,且设置环境变量为模型名model
docker commit --change "ENV MODEL_NAME model" serving_base my_model_0
# 启用my_model_0镜像，此时不需要指定-v/--mount,-e等参数，可直接使用
docker run -t --rm -p 8501:8501 my_model_0
# 重开一个终端，验证是否成功
curl http://localhost:8501/v1/models/model




"""
""" ============================ 导出模型



"""

""" ============================ tensorflow serving client
pip install tensorflow-serving-api
"""
