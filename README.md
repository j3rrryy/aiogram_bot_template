# Aiogram <bot_type> bot

<p align="center">
  <a href="https://www.python.org/downloads/release/python-3120/">
    <img src="https://img.shields.io/badge/Python-3.12-FFD64E.svg" alt="Python 3.12">
  </a>
  <a href="https://github.com/j3rrryy/aiogram_bot_template/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
</p>

## :book: Key features

- Main DB - PostgreSQL
- DB for cache and states - Redis
- Uses <languages> languages to communicate

## :computer: Requirements

- Docker

## :hammer_and_wrench: Getting started

- Create Telegram bot in [@BotFather](https://t.me/BotFather) and receive token
- Create `.env` file with variables as in the `examples/.env.example`
- Install the latest versions of the required packages
- Freeze the installed package versions to `requirements.txt`

### :rocket: Start

```shell
docker compose up --build -d
```

### :x: Stop

```shell
docker compose stop
```

### :email: DM [@<bot_name>_Bot](https://t.me/<bot_name>_Bot) in Telegram
