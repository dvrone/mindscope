# MindScope

A Telegram bot that estimates your MBTI type, IQ and EQ levels.

## Features

- 🧠 MBTI test (20 questions, 16 type descriptions, percentage breakdown per dimension)
- 📊 IQ test (20 questions, approximate IQ score and level)
- ❤️ EQ test (16 questions, breakdown across four areas)
- 📋 Result history stored in SQLite, with an option to clear it
- Questions are shuffled on every attempt
- `/stats` command for the admin

## Tech stack

Python, aiogram 3, aiosqlite, python-dotenv

## Installation

```bash
git clone https://github.com/dvrone/mindscope.git
cd mindscope
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env
```

- `BOT_TOKEN`: get it from [@BotFather](https://t.me/BotFather) on Telegram
- `ADMIN_ID`: your numeric Telegram ID (optional, only needed for `/stats`)

## Usage

```bash
python main.py
```

## Commands

- `/start`: open the main menu
- `/cancel`: stop the current test
- `/help`: show help
- `/stats`: usage statistics (admin only)

## Project structure

```
bot/
├── config.py       # environment variables
├── database.py     # SQLite helpers
├── states.py       # FSM states
├── data/           # test questions and MBTI type descriptions
├── handlers/       # message and callback handlers
└── keyboards/      # reply and inline keyboards
main.py             # entry point
```

## Disclaimer

The IQ and EQ results are not official tests. They are rough estimates for self-discovery and entertainment only.
