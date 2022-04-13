# Webified Decentralized IRC (Django)
---

User Message UI available at `http://ip:port/user/message`
User Account UI available at `http://ip:port/user/account`

api's are available at `http://ip:port/api/set_wallet`
                       `http://ip:port/api/send_msg`


---

Functions to add :/

1. Add CSRF protection
   1. Currently application is having issues with handling csrf POST requests in api addresses
        so it is running without csrf verification for now
