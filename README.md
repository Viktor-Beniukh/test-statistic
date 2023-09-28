# Test Statistic


### Installing using GitHub

- Python3 must be already installed
- Install PostgreSQL and create db


```shell
git clone https://github.com/Viktor-Beniukh/test-statistic.git
cd test-statistic
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver   
```

You need to create `.env` file and add there the variables with your according values:
- `POSTGRES_DB`: this is databases name;
- `POSTGRES_USER`: this is username for databases;
- `POSTGRES_PASSWORD`: this is username password for databases;
- `POSTGRES_HOST`: this is host name for databases;
- `POSTGRES_PORT`: this is port for databases;
- `SECRET_KEY`: this is Django Secret Key - by default is set automatically when you create a Django project.
                You can generate a new key, if you want, by following the link: `https://djecrety.ir`;


## Run with docker

Docker should be installed

- Create docker image: `docker-compose build`
- Run docker app: `docker-compose up`

  
## Features

- Admin panel /admin/;


### How to create superuser
- Run `docker-compose up` command, and check with `docker ps`, that 2 services are up and running;
- Create new admin user. Enter container `docker exec -it <container_name> bash`, and create in from there;


### What do APIs do

- [GET] /spend/spend-statistics/ - obtains a list of spend;
- [GET] /revenue/revenue-statistics/ - obtains a list of revenue.


## Testing

- Run tests using different approach: `docker-compose run app sh -c "python manage.py test"`.
