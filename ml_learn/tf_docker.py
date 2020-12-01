""" ============================
1. 拉去docker模型
docker pull tensorflow/serving

2. 生成容器
docker run -it --name tf -p 8888:9999 tensorflow/serving
    - 8888是本地的端口，9999的容器内端口，意思是把本地8888端口映射到容器中的9999端口中去

3. 将导出的模型导入到运行的容器中
docker cp 模型路径 容器ID：路径

在容器中启动服务，我们服务的端口就是8500，调用的时候记得这个端口
在容器中运行tensorflow_model_server服务
tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=saved_model --model_base_path=/tensorflow-serving/checkpoint/serving_model


"""
""" ============================ 

TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"
docker run -p 8501:8501 \
  --mount type=bind,\
  source=/root/software/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu,\
  target=/models/half_plus_two \
  -e MODEL_NAME=half_plus_two -t tensorflow/serving &
  
--mount：   表示要进行挂载
source：    指定要运行部署的模型地址， 也就是挂载的源，这个是在宿主机上的模型目录
target:     挂载到docker中的哪个位置
-t:         挂载到哪个容器
-p:         指定主机到docker容器的端口映射(把本地8888端口映射到容器中的9999端口中去)
docker run: 启动这个容器并启动模型服务

综合解释： 将source目录中的模型，挂载到-t指定的docker容器中的target目录，并启动

"""
""" ============================ """
""" ============================ """
