# Start the microservices
docker-up:
    docker-compose up --build

# Stop the microservices
docker-down:
    docker-compose down --remove-orphans

docker-build-stockage-service:
    cd stockage_service && docker build -t stockage_service . && cd ..

docker-build-generation-service:
    cd generation_service && docker build -t generation_service . && cd ..

docker-build-vue-front-service:
    cd front_service/ && docker build -t vue_front_service . && cd ..

build-all:
    just docker-build-stockage-service
    just docker-build-generation-service
build-and-run:
    just build-all
    just docker-up
merge-from-main:
    git fetch origin main && git merge origin/main

uptdoc-stockage-service:
    cd stockage_service && python generate_docs.py && poetry export -f requirements.txt --output requirements.txt --without-hashes && cd stockage_service/docs && make clean && make html

lazy commit:
    git add . && git commit -m {{commit}} && git push