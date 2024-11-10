# Description: Install all the dependencies for the project
# front_service
cd front_service/
sudo apt install -y npm
npm install
cd ..

# /stockage_service
cd stockage_service/
sudo apt install -y python3-pip
sudo apt install -y python3-poetry
poetry install
poetry shell

# /user_service
cd user_service/
poetry install
poetry shell
sudo apt install -y postgresql-client-common

# Install PostgreSQL
sudo apt update
sudo apt install -y postgresql postgresql-contrib