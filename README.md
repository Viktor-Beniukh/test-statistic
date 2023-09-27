# Test Statistic


### Installing using GitHub

- Python3 must be already installed


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
- `SECRET_KEY`: this is Django Secret Key - by default is set automatically when you create a Django project.
                You can generate a new key, if you want, by following the link: `https://djecrety.ir`;

  
## Features

- Admin panel /admin/;


### What do APIs do

- [GET] /spend/spend-statistics/ - obtains a list of spend;
- [GET] /revenue/revenue-statistics/ - obtains a list of revenue.


## Testing

- Run tests: `python manage.py test`
