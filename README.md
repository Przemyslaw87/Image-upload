Docker Compose
This project uses Docker Compose to manage the development environment. You can use Docker Compose to build the images, create the containers, and run the project. Building the Images

To build the images, you'll first need to have Docker and Docker Compose installed. Once that's done, navigate to the root directory of the project where the docker-compose.yml file is located, and run the following command:

docker-compose build

This command will build the images defined in the docker-compose.yml file, it may take a while the first time you run it, as it needs to download the required images. Creating the Containers

Once the images are built, you can create the containers by running the following command:

docker-compose up

This command creates the containers and starts them, it also runs the command defined in the docker-compose.yml file, like python manage.py runserver. You can use -d option to run the container in background:

docker-compose up -d

You can use docker-compose down command to stop the container and remove them Accessing the Application

Once the containers are running, you should be able to access the application by visiting http://localhost:8000/ in your browser.

You can also use the docker-compose exec command to run a command in a running container, for example to start a django shell

docker-compose exec web bash

and then

python manage.py shell

Please note that the exact ports and URLs may vary depending on your configuration.

If you need to run any migration or to create a superuser for example you can use the docker-compose exec command like this

docker-compose exec web python manage.py makemigrations

or

docker-compose exec web python manage.py createsuperuser

Docker Compose is a powerful tool that makes it easy to manage the development environment, and allows you to easily build, run, and test your project with minimal setup.