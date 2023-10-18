# -*- coding: utf-8 -*-

from kubernetes import client, config
from kubernetes.client.models.v1_container import V1Container
from kubernetes.client.models.v1_container_port import V1ContainerPort
from kubernetes.client.models.v1_http_get_action import V1HTTPGetAction
from kubernetes.client.models.v1_label_selector import V1LabelSelector
from kubernetes.client.models.v1_object_meta import V1ObjectMeta
from kubernetes.client.models.v1_pod_spec import V1PodSpec
from kubernetes.client.models.v1_pod_template_spec import V1PodTemplateSpec
from kubernetes.client.models.v1_probe import V1Probe
from kubernetes.client.models.v1_service import V1Service
from kubernetes.client.models.v1_service_port import V1ServicePort
from kubernetes.client.models.v1_service_spec import V1ServiceSpec
from kubernetes.client.models.v1_stateful_set import V1StatefulSet
from kubernetes.client.models.v1_stateful_set_spec import V1StatefulSetSpec
from kubernetes.client.models.v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy

file_path = "~/.kube/config"
config.load_kube_config(file_path)
apps_api = client.AppsV1Api()
core_api = client.CoreV1Api()
# node_name = 'cn-shenzhen.172.16.4.128'
namespace = 'glf-test'
name = 'flask05'
labels = {"app": "flask111", "app-name": "flask-glf-test"}
image = "123123123123123123.aliyuncs.com/namespace1/registry1:flask-test-v8.0"
replicas = 5


def create_headless_service():
    body = V1Service(
        api_version='v1',
        kind='Service',
        metadata=V1ObjectMeta(
            name=name,
            # namespace=namespace,
            labels=labels
        ),
        spec=V1ServiceSpec(
            ports=[
                V1ServicePort(name='port-name-test', port=5000)
            ],
            selector=labels,
            cluster_ip=None
        )
    )
    a = core_api.create_namespaced_service(namespace, body)
    print(a)


def data_for_create_and_replace():
    body = V1StatefulSet(
        api_version='apps/v1',
        kind='StatefulSet',
        metadata=V1ObjectMeta(
            name=name,
            namespace=namespace,
            labels=labels
        ),
        spec=V1StatefulSetSpec(
            service_name='service-name-test-001',
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(labels=labels),
                spec=V1PodSpec(
                    containers=[
                        V1Container(
                            ports=[
                                V1ContainerPort(name='port-name-test', container_port=5000)
                            ],
                            name="glf-flask-test",
                            image=image,
                            # readiness_probe=V1Probe(
                            #     http_get=V1HTTPGetAction(path='/', port=5001, scheme='HTTP')
                            # ),
                            # liveness_probe=V1Probe(
                            #     http_get=V1HTTPGetAction(path='/', port=5001, scheme='HTTP')
                            # )
                        )
                    ],
                    # node_name=node_name
                )
            ),
            update_strategy=V1StatefulSetUpdateStrategy(
                # rolling_update=V1RollingUpdateStatefulSetStrategy(max_unavailable=1, partition=1),
                type='OnDelete'
            ),
            replicas=replicas,
            selector=V1LabelSelector(
                match_labels=labels
            ),
            # pod_management_policy='Parallel'
        )
    )
    return body


def create_stateful(body):
    a = apps_api.create_namespaced_stateful_set(namespace, body)
    print(a)


def replace_stateful(body):
    a = apps_api.replace_namespaced_stateful_set(name, namespace, body)
    print(a)


def update():
    pass


def get_and_update():
    pass


def delete():
    """
    先缩容, 然后再删除
    OrderedReady 是什么?
    """
    pass


if __name__ == '__main__':
    # create_headless_service()
    create_stateful(data_for_create_and_replace())
    # replace_stateful(data_for_create_and_replace())
