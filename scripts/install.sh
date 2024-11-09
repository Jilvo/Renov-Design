# Description: Install all the dependencies for the project
# front_service
cd front_service/
sudo apt install npm
npm install
cd ..

# /stockage_service
cd stockage_service/
sudo apt install python3-pip
sudo apt install python3-poetry
poetry install
poetry shell


