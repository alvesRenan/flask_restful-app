#!/bin/bash

docker build . -t renanalves/test-app

docker login -u renanalves -p "${1}"
docker push renanalves/test-app

kubectl delete -f k8s-files
kubectl apply -f k8s-files
