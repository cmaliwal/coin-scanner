### Trading Platform Backend


#### To build a image :

docker build -t test-tarding-platform:0.0.1 .

#### To run a container

docker-compose up -d

#### run command inside the container

docker exec -t -i 6f241d91a385 bash


#### To freeze reuqirements.txt file :
pip freeze | grep -v "pkg-resources" > requirements.txt


###  install Mongo engine:
pip install git+https://github.com/MongoEngine/django-mongoengine.git@master


#### Tools and Technolgoies :

1. Docker
2. Python3.6
3. Django 1.11
4. Django Rest Framework 3.9
5. MongoDB