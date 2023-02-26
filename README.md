# Blog

Django blog application

## Quick start

In your command line:
```
git clone https://github.com/RomanLezhaiko/Blog.git
cd Blog
```

Create virtual enviroment:
```
python3 -m venv .venv

source .venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

Change database settings in blog/blog/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '', # name of database
        'USER': '', # user of db
        'PASSWORD': '', # password for db
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Run the app:
```
cd blog

python3 manage.py migrate

python3 manage.py runserver
```
