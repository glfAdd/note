package main

import (
	"k8s_client/tools"
)

func main() {
	tools.CreateNamespace(tools.InitClientSet())
	//tools.DeleteNamespace(tools.InitClientSet())
	tools.CreateDeployment(tools.InitClientSet())
	//tools.DeleteDeployment(tools.InitClientSet())

}
