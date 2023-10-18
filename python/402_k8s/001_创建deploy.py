# -*- coding: utf-8 -*-

from kubernetes import client, config
from kubernetes.client.models.v1_env_var import V1EnvVar
from kubernetes.client.models.v1_env_var_source import V1EnvVarSource
from kubernetes.client.models.v1_lifecycle import V1Lifecycle
from kubernetes.client.models.v1_lifecycle_handler import V1LifecycleHandler
from kubernetes.client.models.v1_object_field_selector import V1ObjectFieldSelector
from kubernetes.client.models.v1_http_get_action import V1HTTPGetAction
from kubernetes.client.models.v1_http_header import V1HTTPHeader
from kubernetes.client.models.v1_exec_action import V1ExecAction
from kubernetes.client.models.v1_replica_set import V1ReplicaSet
from kubernetes.client.models.v1_deployment_strategy import V1DeploymentStrategy
from kubernetes.client.models.v1_rolling_update_deployment import V1RollingUpdateDeployment
from kubernetes.client.models.v1_label_selector import V1LabelSelector
from kubernetes.client.models.v1_label_selector_requirement import V1LabelSelectorRequirement

file_path = "~/.kube/config"
config.load_kube_config(file_path)
apps_api = client.AppsV1Api()


def get_namespace():
    for i in apps_api.list_deployment_for_all_namespaces().items:
        print(i)


def create_deployment():
    name = "flask02"
    namespace = "daily"
    node_name = 'cn-shenzhen.172.16.4.128'
    replicas = 4
    # 不区分数据类型，都要加引号
    labels = {"app_code": "flask111", "app_id": "flask-glf-test"}
    image = "123123123123123123.aliyuncs.com/namespace1/registry1:flask-test-v5.0"
    env = [
        V1EnvVar(name='POD_IP', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='status.podIP'))),
        V1EnvVar(name='POD_NAME', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='metadata.name'))),
        V1EnvVar(name='POD_NAMESPACE', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='metadata.namespace'))),
    ]
    # 1. 这种方式不能使用环境变量
    # http_headers = [
    #     V1HTTPHeader(name='Content-type', value='application/json'),
    # ]
    # lifecycle = V1Lifecycle(
    #     post_start=V1LifecycleHandler(
    #         http_get=V1HTTPGetAction(host='172.16.4.215', http_headers=http_headers, path='action?a=11&b=312', port=5000)),
    #     pre_stop=V1LifecycleHandler(
    #         http_get=V1HTTPGetAction(host='172.16.4.215', http_headers=http_headers, path='action?a=11&b=312', port=5000)),
    # )

    # 2. command
    lifecycle = V1Lifecycle(
        post_start=V1LifecycleHandler(_exec=V1ExecAction(command=[
            "/bin/sh",
            "-c",
            """
            echo 'curl -X POST -H "Content-type:application/json"' \\\ >> /etc/agent_pod ; 
            echo "-d '{\\"pod_ip\\":"\\"$POD_IP\\"", \\"pod_name\\":"\\"$POD_NAME\\"", \\"pod_namesapce\\":"\\"$POD_NAMESPACE\\""}'" \\\ >> /etc/agent_pod ; 
            echo '"http://172.16.4.215:5000/action?type=start"' >> /etc/agent_pod ; 
            sh /etc/agent_pod 
            """
        ])),
        pre_stop=V1LifecycleHandler(_exec=V1ExecAction(command=[
            "/bin/sh",
            "-c",
            """
            echo 'curl -X POST -H "Content-type:application/json"' \\\ >> /etc/agent_pod ; 
            echo "-d '{\\"pod_ip\\":"\\"$POD_IP\\"", \\"pod_name\\":"\\"$POD_NAME\\"", \\"pod_namesapce\\":"\\"$POD_NAMESPACE\\""}'" \\\ >> /etc/agent_pod ; 
            echo '"http://172.16.4.215:5000/action?type=stop"' >> /etc/agent_pod ; 
            sh /etc/agent_pod 
            """
        ]))
    )
    strategy = V1DeploymentStrategy(
        # rolling_update=V1RollingUpdateDeployment(max_surge=1, max_unavailable=1),
        type='RollingUpdate'
    )
    body = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name, namespace=namespace),
        spec=client.V1DeploymentSpec(
            strategy=strategy,
            replicas=replicas,
            # selector={"matchLabels": labels},
            selector=V1LabelSelector(match_labels=labels),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels=labels),
                spec=client.V1PodSpec(
                    # node_name=node_name,
                    containers=[
                        # client.V1Container(name="glf-flask-test", image=image, env=env, lifecycle=lifecycle)
                        client.V1Container(name="glf-flask-test", image=image, env=env)
                        # client.V1Container(name="glf-flask-test", image=image)
                    ]
                ),
            ),
        ),
    )
    # 创建
    a = apps_api.create_namespaced_deployment(namespace=namespace, body=body)
    # a = apps_api.patch_namespaced_deployment(name=name, namespace=namespace, body=body)
    # a = apps_api.replace_namespaced_deployment(name=name, namespace=namespace, body=body)
    print(a)


def test():
    name = "flask02"
    namespace = "dev"
    node_name = 'cn-shenzhen.172.16.4.128'
    replicas = 1
    # 不区分数据类型，都要加引号
    labels = {"app": "flask111", "app-name": "flask-glf-test", "app2": "flask00001", 'pod-template-hash': '5d785b9cb7'}
    # labels = {"app": "flask111", "app-name": "flask-glf-test"}

    image = "123123123123123123.aliyuncs.com/namespace1/registry1:flask-test-v4.0"
    env = [
        V1EnvVar(name='POD_IP', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='status.podIP'))),
        V1EnvVar(name='POD_NAME', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='metadata.name'))),
        V1EnvVar(name='POD_NAMESPACE', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='metadata.namespace'))),
    ]

    body = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name, namespace=namespace),
        spec=client.V1DeploymentSpec(
            replicas=replicas,
            # selector={"matchLabels": labels},
            selector=V1LabelSelector(
                match_expressions=[
                    V1LabelSelectorRequirement(key='app', values=['flask111'], operator='In'),
                    V1LabelSelectorRequirement(key='app-name', values=['flask-glf-test'], operator='In'),
                    V1LabelSelectorRequirement(key='app2', values=['flask00001'], operator='In'),
                    V1LabelSelectorRequirement(key='pod-template-hash', values=['5d785b9cb7'], operator='In'),
                ],
                match_labels=labels
            ),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels=labels),
                spec=client.V1PodSpec(
                    node_name=node_name,
                    containers=[
                        client.V1Container(name="glf-flask-test", image=image, env=env)
                    ]
                ),
            ),
        ),
    )
    a = apps_api.replace_namespaced_deployment(name=name, namespace=namespace, body=body)
    print(a)


def get_deployment():
    name = "flask02"
    namespace = "dev"
    a = apps_api.read_namespaced_deployment(name, namespace)
    b = apps_api.read_namespaced_deployment_status(name, namespace)
    c = apps_api.read_namespaced_controller_revision(name, namespace)

    print(123123)


if __name__ == "__main__":
    create_deployment()
    # get_deployment()
    # test()
