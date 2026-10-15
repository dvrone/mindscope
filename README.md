# MindScope

A Telegram bot that estimates your MBTI type, IQ and EQ levels.

## Features

- 🧠 MBTI test (12 questions, with descriptions for all 16 types)
- 📊 IQ test (10 questions, approximate IQ score and level)
- ❤️ EQ test (12 questions, breakdown across four areas)

## Tech stack

Python, aiogram 3, python-dotenv

## Installation

```bash
git clone https://github.com/dvrone/mindscope.git
cd mindscope
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
BOT_TOKEN=your_bot_token_here
```

You can get a token from [@BotFather](https://t.me/BotFather) on Telegram.

## Usage

```bash
python main.py
```

Send `/start` to the bot to open the main menu, or `/cancel` to stop a test in progress.

## Disclaimer

The IQ and EQ results are not official tests. They are rough estimates for self-discovery and entertainment only.
