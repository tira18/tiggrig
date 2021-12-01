import os
import yaml
from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
from pprint import pprint
import requests
config.load_kube_config() 
v1 = client.CoreV1Api()
v2 = client.AppsV1Api()
ns = 'dzain'

'''pod = v1.list_namespaced_pod(ns)
service = v1.list_namespaced_service(ns)
for i in pod.items:
    status = i.status.phase    
    container_status = i.status.container_statuses[0]
    if container_status.started is False or container_status.ready is False:
        print("1111111")
        waiting_state = container_status.state.waiting
        status = waiting_state.reason 
        print(status+"  " + i.metadata.name)
        
   
    #print(i)
    #print(i.status.phase)
    #pod = i.metadata.name
    #print(pod)
for i in service.items:
    print("Services")
    service = i.metadata.name
    print(service)'''
    
    
        
'''for i in api_response.items:
    print(i)
    msg = i.service.name
    print(msg)

print(ret)'''

#####DELETE###
        
name = "selenium-standalone-chrome1"



api_response = v2.delete_namespaced_deployment(name, "selsel")
print(api_response)

api_response = v1.delete_namespaced_service(name, "selsel")
print(api_response)

#####DELETE###



'''r = requests.get("http://10.11.4.14:5000/chrome_latest")
print(r.text)'''


'''with open("pod.yaml", "r") as f:  
    pod = yaml.safe_load(f)
    print(type(pod))
    bobo=str(pod).replace('$$APP-NAME$$', '0000000000000')
    bobo=str(bobo).replace('$$IMAGE-NAME$$', '77777777777')
    print(bobo)


    pod1 = pod['spec']['template']['spec']['containers'][0]['image'] = "111111111111" 
    pod2 = pod['metadata']['name'] = "222222"
    pod['spec']['selector']['matchLabels']['app'] = '3333333'

    zozo = pod['spec']['template']['spec']['containers'][0]['name']  
    print(zozo)'''
    
    





from flask import Flask, json
from flask import Flask, render_template, request

'''import requests
app = Flask(__name__)


@app.route('/index')

def image():
    image = request.args.get('image')
    print(image)
    return image

def image_name(image_name=None):
    if image_name == "selenium/standalone-chrome" or image_name == "standalone-firefox" :
        print("selenium/"+image_name)
        return "selenium/"+image_name
    else:
        return "Bad Image"
   

if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0", port=5000)
    #api.run() '''

