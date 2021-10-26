################# Kubernetes ###################################
kubectl cp mongo.dump mongodbtest-mongotest-0:/bitnami/mongodb -n mongotest
kubectl cp data mongo-0:/bitnami -n mongotest

########### StateFulSet ################

$ kubectl exec -it mongod-0 -c mongod-container-app bash
root@mongod-0:/# hostname -f
root@mongod-0:/# mongodb-0.mongodb-service.mongo.svc.cluster.local

########################################

root@mongod-0:/# mongo
> rs.initiate({ _id: "rs0", version: 1, 
members: [ 
 { _id: 0, host: "mongodb-0.mongodb-service.mongo.svc.cluster.local:27017" }, 
 { _id: 1, host: "mongodb-1.mongodb-service.mongo.svc.cluster.local:27017" }, 
 { _id: 2, host: "mongodb-2.mongodb-service.mongo.svc.cluster.local:27017" } ]});
 
 root@mongod-1:/# mongo
 >rs.secondaryOk()
