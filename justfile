# Start the microservices
docker-up: docker-compose up --build

# Stop the microservices
docker-down: docker-compose down --remove-orphans

docker-build-stockage-service: cd stockage-service && docker build -t stockage-service . && cd ..

docker-run-stockage-service: cd stockage-service && docker run -p 8000:8000 stockage-service

merge-from-main: git fetch origin main && git merge origin/main

uptdoc-stockage-service: cd stockage_service && python generate_docs.py && poetry export -f requirements.txt --output requirements.txt --without-hashes && cd stockage_service/docs && make clean &&make html
