import os
import yaml
from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
from pprint import pprint
import requests
config.load_kube_config() 
v1 = client.CoreV1Api()
v2 = client.AppsV1Api()




deployment_name = "selenium-standalone-opera14"



api_response = v2.delete_namespaced_deployment(deployment_name, "selsel")
print(api_response)

api_response = v1.delete_namespaced_service(deployment_name, "selsel")
print(api_response)
