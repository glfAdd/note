package config

import (
	"k8s.io/client-go/rest"
	"k8s.io/client-go/tools/clientcmd"
)

const configFilePath = "/Users/123/.kube/config"

// InitConfig 加载本地配置文件
func InitConfig() *rest.Config {
	config, configErr := clientcmd.BuildConfigFromFlags("", configFilePath)
	if configErr != nil {
		panic(configErr)
	}
	return config
}
