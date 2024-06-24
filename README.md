# <p align="center">BidSecure</p>
<p align="center">
    <p align="center">
        <a href="https://github.com/Sandesh-Pyakurel/Bidding/StudyPal/" target="blank">
            <img src="https://img.shields.io/github/watchers/Sandesh-Pyakurel/Bidding?style=for-the-badge&logo=appveyor" alt="Watchers"/>
        </a>
        <a href="https://github.com/Sandesh-Pyakurel/Bidding/fork" target="blank">
            <img src="https://img.shields.io/github/forks/Sandesh-Pyakurel/Bidding?style=for-the-badge&logo=appveyor" alt="Forks"/>
        </a>
        <a href="https://github.com/Sandesh-Pyakurel/Bidding/stargazers" target="blank">
            <img src="https://img.shields.io/github/stars/Sandesh-Pyakurel/Bidding?style=for-the-badge&logo=appveyor" alt="Star"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/Sandesh-Pyakurel/Bidding/issues" target="blank">
            <img src="https://img.shields.io/github/issues/Sandesh-Pyakurel/Bidding?style=for-the-badge&logo=appveyor" alt="Issue"/>
        </a>
        <a href="https://github.com/Sandesh-Pyakurel/Bidding/pulls" target="blank">
            <img src="https://img.shields.io/github/issues-pr/Sandesh-Pyakurel/Bidding?style=for-the-badge&logo=appveyor" alt="Open Pull Request"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/rajesh-adk-137/StudyPal/blob/master/LICENSE" target="blank">
            <img src="https://img.shields.io/github/license/Sandesh-Pyakurel/Bidding?style=for-the-badge&logo=appveyor" alt="License" />
        </a>
    </p>
</p>

## Overview

BidSecure is a secure web application designed for online auctions. Bidders can place bids on available auctions, and auctioneers can post items for auction. BidSecure leverages Nillion network to ensure secure bidding, protecting users from data leakage and ensuring a safe and trustworthy auction experience.

## Features

- **Secure Bidding:** Utilizes Nillion Network to provide secure bidding mechanisms.
- **Auction Posting:** Auctioneers can easily post items for auction.
- **User-Friendly Interface:** Intuitive design for both bidders and auctioneers.
- **Search for items:** Get results for specific items.
- **Real-Time Updates:** Live updates on auction status and bid placements.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [For Bidders](#for-bidders)
  - [For Auctioneers](#for-auctioneers)
- [Demo](#demo)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Installation
You need to have [nillion-sdk](https://docs.nillion.com/nillion-sdk-and-tools) installed. Follow through the given link to install it.

Now create a virtual environment, activate it and install the requirements.
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Now you need to start the local nillion network.
```bash
cd auction/nillion
./bootstrap-local-environment.sh
cd ../..
```

Run migrate command.
```bash
python3 manage.py migrate
```
You need to have `redis-server` installed in you machine. You can install it with:
```bash
sudo apt install redis-server
```
Then start it with:
```bash
sudo systemctl start redis-server
```
Now we can run the application. Run following 4 commands in seperate terminal.
```bash
python manage.py runserver
python manage.py tailwind start
celery -A bidding beat --loglevel=info
celery -A bidding worker --loglevel=info
```
### Prerequisites

- Python


## Usage

### For Bidders

1. **Register/Login:**
   - Create an account or log in with your existing credentials.

2. **Browse Auctions:**
   - View a list of available auctions and detailed information about each item.

3. **Place a Bid:**
   - Select an auction and enter your bid amount.
   - Bids are securely processed using Nillion Network.

4. **Monitor Auctions:**
   - Track your bids and get real-time updates on auction status.

### For Auctioneers

1. **Register/Login:**
   - Create an account or log in with your existing credentials.

2. **Post an Auction:**
   - Click on "Add Auction" and fill out the item details, including title, description, and starting bid.

3. **Manage Auctions:**
   - View your posted auctions.
   - Monitor bids and auction progress.

## Demo


https://github.com/Sandesh-Pyakurel/Bidding/assets/82999440/019af915-c659-41ab-a2c0-c3f39da5ee07



## Security

BidSecure prioritizes the security and privacy of user data. We use Nillion Network to ensure that all bids are encrypted and securely processed, preventing data leakage and unauthorized access. For more details, visit the [Nillion website](https://www.nillion.com).

## Contributing

We welcome contributions to BidSecure! Please follow these steps to contribute:



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using BidSecure! Happy bidding!
