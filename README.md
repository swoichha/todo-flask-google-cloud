# todo-flask-google-cloud
- gcloud compute scp ~/Desktop/Fordham/Spring\ 25/CC/hw/hw04/todolist/todolist.db swoichha@instance-20250404-015738:/home/swoichha/ --zone=us-central1-c
- gcloud compute scp ~/Desktop/Fordham/Spring\ 25/CC/hw/hw04/todolist/todolist.py swoichha@instance-20250404-015738:/home/swoichha/ --zone=us-central1-c
- gcloud compute scp ~/Desktop/Fordham/Spring\ 25/CC/hw/hw04/todolist/templates/index.html swoichha@instance-20250404-015738:/home/swoichha/ --zone=us-central1-c

- gcloud compute ssh instance-20250404-015738

PArt-2

- run docker daemon
- docker build -t swoichha/todo-frontend:latest .
- docker run -p 5001:5001 -e API_URL="http://35.184.31.83:5000/api" swoichha/todo-frontend
- docker run -it -p 5000:5000 swoichha/todo-frontend

Enable Kubernetes Engine API
gcloud container clusters create todo-cluster \
  --num-nodes=1 \
  --machine-type=e2-micro \
  --zone=us-central1-a

Install gke-gcloud-auth-plugin
- gcloud components install gke-gcloud-auth-plugin

-kubectl apply -f deployment.yaml
