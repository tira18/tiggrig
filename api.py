import re
from flask import Flask, json
from flask import Flask, render_template, request
from kubernetes import client, config, watch
import time
import json
import requests
import yaml

from kubernetes.client.rest import ApiException
from pprint import pprint

#configuration = config.load_kube_config()

v1 = client.AppsV1Api()
v2 = client.ApiClient()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #return "hello"
    

@app.route('/charts')
def chart():
    return render_template('charts.html')
    #return "hello"


@app.route('/test')
def test():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    api_response = v1.list_namespaced_event('selsel')
    for i in api_response.items:
        print(i)
        msg = i.metadata.name
        print(msg)

    
    return str(i)







@app.route('/index')
def image():
    global image
    image = request.args.get('image')
    print(image)    
    return "http://"+create_new()+":4444"

i=0

def create_new():
    global i
    i=i+1  
    #app_name = image.replace("/","-")
    app_name = re.sub(r'\W+', '-', image)
    app_name = app_name.split("-")
    app_name= app_name[:5]
    app_name = "-".join(app_name)
    print(app_name)
    image_name = image
    
    app_name = app_name+str(i) 
    config.load_kube_config()
    #load_incluster_config()
    with open("pod.yaml", "r") as f:
        pod = yaml.safe_load(f)
        #print(type(pod))
               
        pod['metadata']['name'] = app_name
        pod['spec']['selector']['matchLabels']['app'] = app_name
        pod['spec']['template']['metadata']['labels']['app']  = app_name
        pod['spec']['template']['spec']['containers'][0]['image'] = image_name
        pod['spec']['template']['spec']['containers'][0]['name'] = app_name
        
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(body=pod, namespace="selsel")
        #print("pod created. status='%s'" % resp.metadata.name)    
    with open("svc.yaml", "r") as f:
        pod = yaml.safe_load(f)        
        
        pod['metadata']['name'] = app_name
        pod['spec']['selector']['app'] = app_name
        k8s_apps_v1 = client.CoreV1Api()
        resp = k8s_apps_v1.create_namespaced_service(body=pod, namespace="selsel")
        #print("pod created. status='%s'" % resp.metadata.name)
        service_name = resp.metadata.name
        time.sleep(3)
    service = k8s_apps_v1.read_namespaced_service(service_name, 'selsel')
    pod_ip = service.status.load_balancer.ingress[0].ip     
    return str(pod_ip)









if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0", port=5000)
    #api.run() 
