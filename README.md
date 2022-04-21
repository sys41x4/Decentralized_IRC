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

Homepage available at `http://<ip>:<port>`<br><br>

User Message UI available at `http://<ip>:<port>/user/message` <br>
User Beta Message UI available at `http://<ip>:<port>/user/betamsg` <br>
User Account UI available at `http://<ip>:<port>/user/account` <br><br>

api's are available at `http://<ip>:<port>/api/set_wallet` <br>
emsp;emsp;emsp;emsp;emsp;emsp;`http://<ip>:<port>/api/send_msg`


---

Functions to add :/

1. Add CSRF protection
   1. Currently application is having issues with handling csrf POST requests in api addresses
        so it is running without csrf verification for now

---

## File/Directory Structure
```
.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── basic_working.txt
├── db.sqlite3
├── Decentralized_IRC
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── templates
│   |   ├── 404.html
│   |   ├── 500.html
│   |   ├── base.html
│   │   └── homepage.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── manage.py
├── node_modules/
├── package.json
├── package-lock.json
├── put-files.js
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   ├── account.css
│   │   ├── beta_msg.css
│   │   ├── style.css
│   │   ├── styles.css
│   │   └── vendor.css
│   └── js
│       ├── app.js
│       ├── beta_msg.js
│       ├── ethjs-unit.min.js
│       ├── main.js
│       ├── particle-settings.js
│       ├── particles.min.js
│       ├── plugins.js
│       └── wallet_handlers
│           ├── metamask.js
│           └── phantom.js
├── txn_hashes
|   └── Txn-Hash
└── user
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   ├── account.html
    │   ├── beta_msg.html
    │   ├── dashboard.html
    │   ├── homepage.html
    │   ├── index.html
    │   ├── message.html
    │   ├── metamask_message.html
    │   ├── orders.html
    │   └── send_message.html
    ├── tests.py
    ├── urls.py
    └── views.py
```