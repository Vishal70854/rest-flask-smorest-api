# Run a Docker file locally in our system

```
Build Docker Image
docker build -t CONTAINER_NAME .  

Run Docker container
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"
```
```
Run a rq background worker task queue using Docker locally
docker run -w /app rest-apis-flask-smorest-rq sh -c "rq worker -u <insert your Redis url here> emails"

Run the app in the background
docker run -p 5000:5000 rest-apis-flask-smorest-rq sh -c "flask run --host 0.0.0.0"
```
