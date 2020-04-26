""" ============================ Vultr
Vultr
官网
https://my.vultr.com/


购买教程
https://www.vultrcn.com/1.html
"""

""" ============================ centos 服务端安装
参考
https://www.52soft.cc/jishu/2776.html



wget –no-check-certificate -O shadowsocks.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
chmod +x shadowsocks.sh
yum install gcc-c++
./shadowsocks.sh 2>&1 | tee shadowsocks.log
然后根据提示选择
命令
/usr/bin/python /usr/bin/ssserver -c /etc/shadowsocks.json -d start
./shadowsocks.sh uninstall  //卸载

vi /etc/shadowsocks.json //修改参数
/etc/init.d/shadowsocks start //启动
/etc/init.d/shadowsocks stop //停止
/etc/init.d/shadowsocks restart //重启
/etc/init.d/shadowsocks status //查看状态


配置文件
vi /etc/shadowsocks.json //修改参数









安装错误: [Error] libsodium install failed!
解决办法:   
"""

""" ============================ debian 服务端安装
参考:
    https://blog.51cto.com/shareku/2114756
    https://www.jianshu.com/p/3f874d5aac54
    
    
1. pip install shadowsocks

2. 配置 vim /etc/shadowsocks.json
说明:
    - server：服务器 IP地址 (IPv4/IPv6)
    - server_port：服务器监听的端口，一般设为80，443等，注意不要设为使用中的端口
    - password：设置密码，自定义
    - timeout：超时时间（秒）
    - method：加密方法，可选择 “aes-256-cfb”, “rc4-md5”等等。推荐使用 “rc4-md5”
    - fast_open：true 或 false。如果你的服务器 Linux 内核在3.7+，可以开启 fast_open 以降低延迟。
    - workers：workers数量，默认为 1
    
    单个账号
    {
        "server": "0.0.0.0",
        "server_port": 10469,
        "local_address": "127.0.0.1",
        "local_port": 1080,
        "password": "12e",
        "timeout": 300,
        "method": "aes-256-cfb",
        "fast_open": false,
        "workers": 1
    }
    
    {
        "server":"0.0.0.0",
        "server_port":8388,
        "local_address": "127.0.0.1",
        "local_port":1080,
        "password":"pawssword",
        "timeout":300,
        "method":"aes-256-cfb"
    }

    配置做个账号
    {
        "server": "your_server_ip",
        "port_password": {
            "8381": "pass1",
            "8382": "pass2",
            "8383": "pass3",
            "8384": "pass4"　　　　#注意：json的最后一行是没有“,”(逗号)
        },
        "timeout": 60,
        "method": "rc4-md5",
        "fast_open": false,
        "workers": 1
    }


3. 命令
ssserver -c /etc/shadowsocks.json -d start
ssserver -c /etc/shadowsocks.json -d stop

4. 报错信息
INFO: loading config from /etc/shadowsocks.json
2020-03-06 12:32:49 INFO     loading libcrypto from libcrypto.so.1.1
Traceback (most recent call last):
  File "/usr/local/bin/ssserver", line 10, in <module>
    sys.exit(main())
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/server.py", line 34, in main
    config = shell.get_config(False)
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/shell.py", line 262, in get_config
    check_config(config, is_local)
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/shell.py", line 124, in check_config
    encrypt.try_cipher(config['password'], config['method'])
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/encrypt.py", line 44, in try_cipher
    Encryptor(key, method)
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/encrypt.py", line 83, in __init__
    random_string(self._method_info[1]))
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/encrypt.py", line 109, in get_cipher
    return m[2](method, key, iv, op)
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/crypto/openssl.py", line 76, in __init__
    load_openssl()
  File "/usr/local/lib/python2.7/dist-packages/shadowsocks/crypto/openssl.py", line 52, in load_openssl
    libcrypto.EVP_CIPHER_CTX_cleanup.argtypes = (c_void_p,)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 379, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 384, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: /lib/x86_64-linux-gnu/libcrypto.so.1.1: undefined symbol: EVP_CIPHER_CTX_cleanup
解决办法
	1. vim /usr/local/lib/python2.7/dist-packages/shadowsocks/crypto/openssl.py
	   或
	   vim /usr/local/lib/python3.7/dist-packages/shadowsocks/crypto/openssl.py
	2. 将所有 
	   libcrypto.EVP_CIPHER_CTX_cleanup.argtypes = (c_void_p,) 
	   改为 
	   libcrypto.EVP_CIPHER_CTX_reset.argtypes = (c_void_p,)
	
5. 加入开机自启
echo "ssserver -c /etc/shadowsocks.json -d start" >> /etc/rc.d/rc.local

6. 日志路径
/var/log/shadowsocks.log
"""

""" ============================ 命令
ssserver --version


"""
