from kubernetes import client, config
from kubernetes.client.rest import ApiException
config.load_kube_config() # or config.load_kube_config()

configuration = client.Configuration()
api_instance = client.CoreV1Api()
    
try:
    api_response = api_instance.delete_namespaced_pod(name="jj2", namespace="default")
     print( " pod is deleted successfully!\n")
except ApiException as e:
    print("could not delete pod")