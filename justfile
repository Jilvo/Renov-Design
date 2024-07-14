# Start the microservices
docker-up:
  docker-compose up --build

# Stop the microservices
docker-down:
  docker-compose down --remove-orphans

docker-build-stockage-service:
    cd stockage-service && docker build -t stockage-service . && cd ..

docker-run-stockage-service:
    cd stockage-service && docker run -p 8000:8000 stockage-service
