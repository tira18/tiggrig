from kubernetes import client, config, watch
import time
import json
import requests
import yaml
#import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
# Configs can be set in Configuration class directly or using helper utility
configuration = config.load_kube_config()
#limit_bytes=50060,
v1 = client.CoreV1Api()
core_v1 = client.ApiClient()


ret = v1.list_namespaced_pod("selsel", watch=False)
for i in ret.items:
    print("////////////////////////////")
    print(i.metadata.name)





def pod_create():
    config.load_kube_config()    
    with open("deploy_pod.yaml", "r") as f:
        pod = yaml.safe_load(f)
        print(pod)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=pod, namespace="selsel")
        print("pod created. status='%s'" % resp.metadata.name)    
    with open("deploy_pod_svc.yaml", "r") as f:
        pod = yaml.safe_load(f)
        print(pod)
        k8s_apps_v1 = client.CoreV1Api()
        resp = k8s_apps_v1.create_namespaced_service(body=pod, namespace="selsel")
        print("pod created. status='%s'" % resp.metadata.name)
    return "pod created. status='%s'" % resp.metadata.name




pod_create()





'''print("Listing pods with their IPs:")
w = watch.Watch()
for e in w.stream(v1.read_namespaced_pod_log, name="front-f6f76c7d4-2db9d", namespace="tce-cn", follow=True, tail_lines=1, _preload_content=False):
   if ".js" in e:
       e = e.split()
       ip = e[-1].strip('"')
       response = requests.get("https://geolocation-db.com/json/"+ip+"&position=true").json()
       country = response["country_name"]
       city = str(response["city"])
       browser = e[-2]
       time = e[3].strip("[")
       
       print(ip+"\t"+browser+"\t"+country+"\t"+city+"\t"+time)
       fo = open('ips.txt', 'a')
       fo.write(ip+"\t"+browser+"\t"+country+"\t"+city+"\t"+time+'\n')
       fo.close()'''
       
'''#ret = v1.list_pod_for_all_namespaces(watch=False)
ret = v1.list_namespaced_pod("tcm", watch=False)
for i in ret.items:
    print("////////////////////////////")
    print(i.metadata.name)
    print(i.status.pod_ip)
    #container_info = type(i.status.container_statuses[0])    
    #print(container_info)
    #res = json.loads(container_info)
    #print(res)
    #print("%s\t%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name, i.status.pod_ip))
    
    ret_metrics = api_client.call_api(
                '/apis/metrics.k8s.io/v1beta1/namespaces/'+ '/pods', 'GET',
                auth_settings=['BearerToken'], response_type='json', _preload_content=False)
    response = ret_metrics[0].data.decode('utf-8')
    resource = json.loads(response)
    
    CPU = "CPU: " + str(resource["items"][1]["containers"][0]["usage"]["cpu"])
    MEMORY = "MEMORY: " + str(resource["items"][1]["containers"][0]["usage"]["memory"])
    print(CPU)
    print(MEMORY)'''




'''w = watch.Watch()
for e in w.stream(v1.read_namespaced_pod_log, name="mongodb-868477b98f-dlp5c", namespace="tcm"):
    print(e)



# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.AppsV1Api(api_client)
    namespace = 'bobobobobobobo' # str | object name and auth scope, such as for teams and projects
    body = kubernetes.client.V1Deployment()
    #body = kubernetes.client.V1StatefulSet() # V1StatefulSet | 
    #pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
    #dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    #field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    try:
        api_response = api_instance.create_namespaced_deployment(namespace,body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)'''
