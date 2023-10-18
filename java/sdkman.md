##### 安装

```bash
# mac / linux
$ curl -s "https://get.sdkman.io" | bash 
$ source "$HOME/.sdkman/bin/sdkman-init.sh"
$ sdk version

# 升级
$ sdk selfupdate force
```

##### 使用

```bash
# ------------------------------------ java
$ sdk ls java
$ sdk install java 8.0.352-amzn
# 切换默认版本
$ sdk default java 8.0.352-amzn
# 临时切换版本
$ sdk use java 8.0.352-amzn

# ------------------------------------ maven
$ sdk ls maven
$ sdk install maven
$ sdk install maven 3.9.2

# 配置文件在 ~/.sdkman/candidates/maven/3.9.2/conf/settings.xml
$ find . -name settings.xml

# 切换为国内源
<mirror>
  <id>alimaven</id>
  <name>aliyun maven</name>
  <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
  <mirrorOf>central</mirrorOf>
</mirror>



# ------------------------------------ 
$ sdk current        #查看当前已安装的软件
$ sdk uninstall ..   #卸载软件
$ sdk rm ..          #卸载软件 同上
$ sdk version        #查看sdkman版本
```



