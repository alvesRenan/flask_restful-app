#!/bin/bash

docker build . -t renanalves/test-app

docker push -u renanalves -p $1 renanalves/test-app

kubectl apply -f k8s-files
