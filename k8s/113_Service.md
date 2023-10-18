##### 参考

```

```

##### headless service (无头服务)

```
可以通过指定Cluster IP(spec.clusterIP)的值为“None”来创建Headless Service
```



service.json

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: flask111
    app-name: flask-glf-test
  name: flask05
  namespace: glf-test
spec:
  ports:
  - name: port-name-test
    port: 5000
    protocol: TCP
    targetPort: 5000
  selector:
    app: flask111
    app-name: flask-glf-test
  sessionAffinity: None
  type: ClusterIP
```



```
用提供服务, Service 有 ClusterIP, 方位这个 ip 的时候, 请求会被分发到绑定这个 ip 的 pod 上, 自动负载均衡


标签筛选需要和pod的标签保持一致，并且这里的metadata.name也要与StatefulSet中的serviceName一样

```



```bash
kube-shell> kubectl get service
NAME      TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
flask05   ClusterIP   10.98.25.20   <none>        5000/TCP   74m
kube-shell> kubectl get pod
NAME        READY   STATUS    RESTARTS   AGE
flask05-0   1/1     Running   0          37s
flask05-1   1/1     Running   0          35s
flask05-2   1/1     Running   0          34s
flask05-3   1/1     Running   0          33s



请求发送到 10.98.25.20 后, service 会自动分发到 flask05-0, flask05-1, flask05-2, flask05-3 上, 默认分发策略轮询
可以通过 Service 来访问到 Pod
```

