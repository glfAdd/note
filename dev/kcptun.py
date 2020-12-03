""" ============================

https://www.pianshen.com/article/7383275704/
Linux��Kcptun��SS������������

�����CentOS�´SSR(ShadowsocksR)�����
https://q.115.com/153332/T78657.html


�����ܲ�����
https://www.dzsfo.com/2019/06/28/SSR/

"""
""" ============================ ����ǽ
1. �༭����ǽ�ļ�
vim /etc/firewalld/zones/public.xml

<?xml version="1.0" encoding="utf-8"?>
<zone>
  <short>Public</short>
  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>
  <service name="dhcpv6-client"/>
  <service name="ssh"/>
  <port protocol="tcp" port="23456"/> <!-- ���SSR�����еĶ˿� -->
  <port protocol="udp" port="23456"/> <!-- ע�⣺ÿ���˿�Ҫ���TCP��UDP���� -->
  <port protocol="tcp" port="34567"/>
  <port protocol="udp" port="34567"/>
</zone>


2. ��������ǽ
systemctl restart firewalld


./server_linux_amd64 -l :20086 -t 127.0.0.1:8388 -key tests -mtu 1400 -sndwnd 2048 -rcvwnd 2048 -mode fast2 > kcptun.log 2>&1 &
./server_linux_amd64 -l :20086 -t 127.0.0.1:10469 -key tests -mtu 1400 -sndwnd 2048 -rcvwnd 2048 -mode fast2 > kcptun.log 2>&1 &



#!/bin/bash
cd /root/kcptun/
./server_linux_amd64 -l :6666 -t 127.0.0.1:10480 -key 132613626glf -mtu 1400 -sndwnd 2048 -rcvwnd 2048 -mode fast2 > kcptun.log 2>&1 &
echo "��ʼ����Kcptun"



{
    "server":"0.0.0.0",
    "server_port":10480,
    "password":"glf13261326",
    "timeout":300,
    "method":"rc4-md5"
}
ssserver -c /etc/shadowsocks.json -d start


202.182.105.193:6666



github
https://github.com/xtaci/kcptun


�ͻ��˰�װ�̳�
https://maxsky.cc/2017/03/26/MacOS-Use-KcpTun-Acc-SS/


����˽̳�
https://www.qinzc.me/post-201.html


key=your_kcptun_key;crypt=aes-128;mode=fast;mtu=1350;sndwnd=1024;rcvwnd=1024;datashard=10;parityshard=3;nocomp=true;dscp=0
key=132613626glf;crypt=aes;mode=fast2;mtu=1350;sndwnd=2048;rcvwnd=2048;datashard=10;parityshard=3;dscp=0

ShadowsocksX-NG 1.8.2����kcptun
https://tech.yj777.cn/mac-%E4%B8%8A%E7%9A%84-kcptun-ss-libev%EF%BC%8Cssx-ng-%E7%89%88%E6%9C%AC/


#!/bin/bash
cd /root/kcptun/
./server_linux_amd64 -l :8776 -t 127.0.0.1:9019 -key glf13261326 -mtu 1400 -sndwnd 2048 -rcvwnd 2048 -mode fast2 > kcptun.log 2>&1 &
echo "��ʼ����Kcptun"


netstat -lntup

key=glf13261326;crypt=aes;mode=fast2;mtu=1350;sndwnd=2048;rcvwnd=2048;datashard=10;parityshard=3;dscp=0
key=glf13261326;crypt=aes-256-cfb;mode=fast;mtu=1350;sndwnd=1024;rcvwnd=1024;datashard=10;parityshard=3;nocomp=true;dscp=0


"""
