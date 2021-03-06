<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="https://github.com/TheCryptoBabyPunks/CryptoBabyPunksDiscordBot/blob/main/static/sc.png" width="50%" height="50%">
</p>

<h2 align="center">CryptoBabyPunksBot</h2>

<p align="center">
  <b>Twitter</b>
</p>
 
## :bulb: Table of Contents
<br>

* [About the Project](#about-the-project)
  * [Introduction](#introduction)
  * [Built With](#built-with)
  * [Structure](#structure)
* [Quick Start](#quick-start)
  * [Building the Docker Image](building-the-docker-image)
  * [Running the Docker Image](running-the-docker-image)
  * [Output](#output)
* [License](#license)

## :zap: About the Project

### :tada: Introduction


👉 999 unique [CryptoBabyPunks](http://www.cryptobabypunks.com/allcryptobabypunks.html) on [Opensea](https://opensea.io/collection/cryptobabypunks).

🍼 Some are baby Girls or Boys and very few are Zombies, Apes or Alien.

💎 There are 47 ≠ attributes. Your CryptoBabyPunk may have zero, one, two or three attributes.

🥰 Find out who the parents of your BabyPunks are with [Punks.Family](http://punks.family/)!

💬 Join the BabyPunks Family on [Twitter](https://twitter.com/cryptobabypunks)

### :books: Built With

```
APScheduler == 3.7.0
emoji == 1.2.0
requests == 2.25.1
tweepy == 3.8.0
```

### :art: Structure

```
.
├── Dockerfile
├── bot
│   ├── config.py
│   ├── opensea.py
│   └── tweet.py
├── files
├── requirements.txt
├── static
│   └── sc.png
├── templates
│   ├── created.txt
│   ├── offer_entered.txt
│   └── successful.txt
└── tweet-bot.tar.gz
```
## :boom: Quick Start

### :fire: Building the Docker :whale: Image

```
$ docker build . -t tweet-bot
```
### :rocket: Running the Docker :whale: Image

```
$ docker run -it \
  -e CONSUMER_KEY="<CONSUMER_KEY>" \
  -e CONSUMER_SECRET="<CONSUMER_SECRET>" \
  -e ACCESS_TOKEN="<ACCESS_TOKEN>" \
  -e ACCESS_TOKEN_SECRET="<ACCESS_TOKEN_SECRET>" \
tweet-bot
```

### 🖥️ Output

<p align="center">
  <img src="https://github.com/TheCryptoBabyPunks/CryptoBabyPunksTwitterBot/blob/main/static/bot_message.png" width="50%" height="50%">
</p>

## :open_book: License

This project is licensed under the MIT License
