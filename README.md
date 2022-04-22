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

### Basic Docker Usage
```
[Stop Docker Container]
docker stop <container-name>

[Remove a Docker Container by Container Name]
docker container rm <container-name>

[Remove a Docker Container by Container ID]
docker rm <Container-ID>

[List Docker Volumes]
docker volume ls

[Remove Docker Volumes]
docker volume rm <volume-name>

[Remove Unused Docker volumes]
docker volume purge
```
---


### Using postgresql (docker) for web2 storage
Reference : https://dev.to/shree_j/how-to-install-and-run-psql-using-docker-41j2

```
[Installing PostgresQL (docker)]
mkdir -p /home/<your_user_id_here>/pgdata
docker run --name <postgresql-container-name> -p 5432:5432 -e POSTGRES_PASSWORD=<password> -d postgres

[Production Build]
docker run -d --name <postgresql-container-name> -p 5432:5432 -e POSTGRES_PASSWORD=<password> -v /home/<your_user_id_here>/pgdata:/var/lib/postgresql/data postgres

A new container will be created and running at 0.0.0.0:5432 with the below command.
docker ps -a

[Installing PG-admin (docker)]
docker run --rm -p 5050:5050 thajeztah/pgadmin4

Now manage your postgres from the browser by launching http://localhost:5050

* Add postgres connection in PG-admin WebApp
* Get IP Address of the psql-Server
        docker inspect <postgresql-container-name> | grep IPAddress

[Connecting to the PSQL server via CLI]

1. Find the docker-container-id in which the postgres is running using
                docker ps -a
2. Run the below command to enter into the container (with the ID from step-1).
                docker exec -it <PSQL-Container-ID> bash
3. Authenticate to start using as postgres user. 
                psql -h localhost -p 5432 -U postgres -W
4. Enter the password used while creating the PSQL server container.

```

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