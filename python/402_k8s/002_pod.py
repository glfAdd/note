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
from kubernetes.client.models.v1_pod import V1Pod
from kubernetes.client.models.v1_pod_spec import V1PodSpec
from kubernetes.client.models.v1_container import V1Container
from kubernetes.client.models.v1_object_meta import V1ObjectMeta
from kubernetes.client.models.v1_pod_status import V1PodStatus

file_path = "~/.kube/config"
config.load_kube_config(file_path)
core_api = client.CoreV1Api()
namespace = "glf-test"


def read_pod():
    name = "flask02-5fc5f57655-crm2c"
    namespace = "glf-test"
    a = core_api.read_namespaced_pod(name=name, namespace=namespace)
    print(11111111111)


def delete_pod():
    name = "flask02-56c7c7647f-6jz8d"
    a = core_api.delete_namespaced_pod(name=name, namespace=namespace)
    print(a)


def patch_pod():
    """
    只更新 body 里面的数据, 其他的保持不变
    不会改变 pod 的运行状态, 状态一直是 running ,但是更新镜像之后用的还是以前的镜像, 要等会儿(时间不固定)才能用新的镜像
    不满足需求
    """
    namespace = "glf-test"
    image = "123123123123123123.aliyuncs.com/namespace1/registry1:flask-test-v2.0"
    body_patch = V1Pod(
        api_version='v1',
        kind='Pod',
        spec=V1PodSpec(
            containers=[V1Container(
                name="glf-flask-test", image=image
            )]
        )
    )
    a = core_api.patch_namespaced_pod(
        name="flask04-5d785b9cb7-sh9bf",
        namespace=namespace,
        body=body_patch,
        # local_var_params={"_preload_content": False}
        # force=True
    )
    print(a)


def replace_pod():
    image = "123123123123123123.aliyuncs.com/namespace1/registry1:flask-test-v2.0"
    env = [
        V1EnvVar(name='POD_IP', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='status.podIP'))),
        V1EnvVar(name='POD_NAME', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='metadata.name'))),
        V1EnvVar(name='POD_NAMESPACE', value_from=V1EnvVarSource(field_ref=V1ObjectFieldSelector(field_path='metadata.namespace'))),
    ]
    body_replace = V1Pod(
        api_version='v1',
        kind='Pod',
        metadata=V1ObjectMeta(name='flask04-5d785b9cb7-v5sm5', namespace=namespace),
        spec=V1PodSpec(
            containers=[V1Container(
                name="glf-flask-test", image=image, env=env
            )]
        ),
        # status=V1PodStatus()
    )
    g = core_api.read_namespaced_pod(name='flask04-5d785b9cb7-v5sm5', namespace=namespace)
    g.spec.containers = [V1Container(name="glf-flask-test", image=image, env=env)]
    print(11111111111)
    a = core_api.replace_namespaced_pod(
        name='flask04-5d785b9cb7-v5sm5',
        namespace=namespace,
        # body=body_replace,
        body=g,
    )
    print(a)


if __name__ == '__main__':
    read_pod()
    # delete_pod()
    # patch_pod()
    # replace_pod()
