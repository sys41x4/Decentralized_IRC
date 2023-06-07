# Decentralized_IRC
Webified Decentralized IRC [web3 | IPFS]

### Requirements

1. Python3
2. Nodejs

### Install Node modules for setup

Use `npm install` in current directory **Decentralized_IRC** to install modules

### Setup postgresql [Heroku]

Download heroku-cli from `https://devcenter.heroku.com/articles/heroku-cli#get-started-with-the-heroku-cli`

```bash
heroku login [For using Browser Mode Verification]
heroku login -i [For using Terminal Mode Verification]

mkdir <Directory_Name>
cd <Directory_Name>

heroku authorizations:create

# For mac-os/linux
export HEROKU_API_KEY=<your_token>

# For windows | Temporary Assign
set HEROKU_API_KEY=<your_token>

heroku create irc-postgresql-hasher

heroku addons:create heroku-postgresql:hobby-dev

heroku config:get DATABASE_URL --app irc-postgresql-hasher
```

### Check List

- [ ] Create seperate Account Page
- [ ] Create seperate HomePage
- [ ] Create Seperate Messaging Page
- [ ] Initiate Direct Messaging Functionality
- [ ] Initiate Group Chat Functionality
- [ ] Enable Dark/Light Mode
- [ ] Create Seperate Server Side scripts to get requests using API Requests
- [ ] Create Seperate Client Side scripts
- [ ] Create Seperate file Identifier (using CID/Transaction-Hash, Block etc) storage
- [ ] Create support for anyone to connect as a seperate client or as a miner
- [ ] Add free messaging functionality
- [ ] Add paid messaging functionality
- [ ] Search for low cost alternative of **Etherium** (Avoiding it because of it's high transaction fees) such as **Polygon**,**Solana** or **Tech Pay** [**Tech Pay** Costs low than **Solana** and is 4.5x faster than solana]
- [ ] Add properties for storing data to **BlockChain Network**
- [ ] Make transaction searcher like (**etherscan.io**)

... More to come. Stay tuned :)