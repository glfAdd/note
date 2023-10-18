FROM 123123123123123123.aliyuncs.com/daily/blm-daily:v4.2
MAINTAINER glfAdd
LABEL authors="glf-test" version="1.0"
RUN mkdir -p /opt/source/test
WORKDIR /opt/source/test
# 拷贝代码
COPY . /opt/source/test
EXPOSE 5000
# 启动命令
CMD ["./test"]