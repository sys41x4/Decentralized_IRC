# Webified Decentralized IRC (Django)

---
## Working with the `Decentralized_IRC-django branch`

```bash
virtualenv Decentralized_IRC-django
cd Decentralized_IRC-django
./Scripts/activate

mkdir Decentralized_IRC-django
cdd Decentralized_IRC-django
git init
git remote add origin https://github.com/Arijit-Bhowmick/Decentralized_IRC.git

git checkout Decentralized_IRC-django

git pull

```


### Django basics

References : https://realpython.com/get-started-with-django-1/

```bash
[Run the django Webapp]
(Using Default Settings [127:8000])
python manage.py runserver

(Using other <ip>:<port> other than Default settings)
python manage.py runserver <ip>:<port>

[Create New app under Decentralized_IRC]
python manage.py startapp <app_name>
```

---
### WebApp links and functionalities

User Message UI available at `http://ip:port/user/message`
User Account UI available at `http://ip:port/user/account`

api's are available at `http://ip:port/api/set_wallet`
                       `http://ip:port/api/send_msg`


---

Functions to add :/

1. Add CSRF protection
   1. Currently application is having issues with handling csrf POST requests in api addresses
        so it is running without csrf verification for now
