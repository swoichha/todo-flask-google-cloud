#!/bin/bash

# Build and push Docker image
docker build -t your-dockerhub-username/todo-frontend:latest .
docker push your-dockerhub-username/todo-frontend:latest

# Create GKE cluster (if not exists)
gcloud container clusters create todo-cluster \
  --num-nodes=1 \
  --machine-type=e2-micro \
  --zone=us-central1-a

# Deploy to GKE
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Print external IP
echo "Access the app at:"
kubectl get service todo-frontend-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}'