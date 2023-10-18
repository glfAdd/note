##### 从 KubeConfig 文件中提取 CA、Key 和 APIServer 信息

```bash
$ cat .kube/config |grep client-certificate-data | awk -F ' ' '{print $2}' |base64 -d > ./client-cert.pem
$ cat .kube/config |grep client-key-data | awk -F ' ' '{print $2}' |base64 -d > ./client-key.pem
$ APISERVER=`cat .kube/config |grep server | awk -F ' ' '{print $2}'`
```

#####

```bash
# 查看当前集群中所有Namespaces
$ curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/glf-test/pods
# pod
$ curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/glf-test/pods/flask04-5d785b9cb7-v5sm5
# log
$ curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/glf-test/pods/flask04-5d785b9cb7-v5sm5/log
```

