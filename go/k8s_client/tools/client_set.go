package tools

import (
	"context"
	"fmt"
	appsV1 "k8s.io/api/apps/v1"
	apiV1 "k8s.io/api/core/v1"
	metaV1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/utils/pointer"
	"k8s_client/config"
	"log"
)

// InitClientSet 创建 clientSet
func InitClientSet() *kubernetes.Clientset {
	clientSet, err := kubernetes.NewForConfig(config.InitConfig())
	if err != nil {
		log.Fatal(err)
	}
	return clientSet
}

func CreateNamespace(client *kubernetes.Clientset) {
	namespaceClient := client.CoreV1().Namespaces()
	namespace := &apiV1.Namespace{
		ObjectMeta: metaV1.ObjectMeta{
			Name: "glf-test",
		},
	}
	result, err := namespaceClient.Create(context.TODO(), namespace, metaV1.CreateOptions{})

	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("Create namespace %s \n", result.GetName())

}

func DeleteNamespace(client *kubernetes.Clientset) {
	emptyDeleteOptions := metaV1.DeleteOptions{}
	if err := client.CoreV1().Namespaces().Delete(context.TODO(), "glf-test", emptyDeleteOptions); err != nil {
		panic(err.Error())
	}
}

func CreateDeployment(client *kubernetes.Clientset) {
	image := "1231231231/namespace1/registry1:flask-test-v7.0"
	namespace := "glf-test2"
	labels := map[string]string{
		"app_code": "flask_test01",
	}
	deployment := &appsV1.Deployment{
		ObjectMeta: metaV1.ObjectMeta{
			Name: "flask10",
		},
		Spec: appsV1.DeploymentSpec{
			Replicas: pointer.Int32(5),
			Selector: &metaV1.LabelSelector{
				MatchLabels: labels,
			},
			Template: apiV1.PodTemplateSpec{
				ObjectMeta: metaV1.ObjectMeta{
					Labels: labels,
				},
				Spec: apiV1.PodSpec{
					Containers: []apiV1.Container{
						{
							Name:  "golang-client-flask",
							Image: image,
							Ports: []apiV1.ContainerPort{
								{
									Name:          "http-service",
									Protocol:      apiV1.ProtocolTCP,
									ContainerPort: 5000,
								},
							},
						},
					},
				},
			},
		},
	}
	res, err := client.AppsV1().Deployments(namespace).Create(context.TODO(), deployment, metaV1.CreateOptions{})
	//client.AppsV1().Deployments(namespace).Update()
	//client.AppsV1().Deployments(namespace).Patch()
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf(res.GetName())

}

func DeleteDeployment(client *kubernetes.Clientset) {
	emptyDeleteOptions := metaV1.DeleteOptions{}
	if err := client.AppsV1().Deployments("glf-test").Delete(context.TODO(), "flask10", emptyDeleteOptions); err != nil {
		panic(err.Error())
	}

}
