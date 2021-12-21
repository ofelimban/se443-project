{
     "kind": "Pod",
     "apiVersion": "v1",
     "metadata":{
         "name": "jj4",
         "namespace": "default",
         "labels": {
             "name": "minikube jj4"
         }
     },
     "spec": {
         "containers": [{
             "name": "minikube",
             "image": "k8s.gcr.io/echoserver:1.4",
             "ports": [{"containerPort": 88}],
             "resources": {
                 "limits": {
                     "memory": "128Mi",
                     "cpu": "500m"
                 }
             }
         }]
     }
 }