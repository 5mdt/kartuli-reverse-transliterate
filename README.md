# Kartuli Reverse Transliterate Bot

This Telegram bot converts Latin text to Georgian and provides translation links to popular translation apps.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [docker-compose](https://docs.docker.com/compose/install/)
- [Telegram Bot Token](https://core.telegram.org/bots#botfather)

### Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/5mdt/kartuli-reverse-transliterate/
   cd kartuli-reverse-transliterate
   ```

2. Create a `.env` file from the `.env.example` template:

   ```shell
   cp .env.example .env
   ```

   Update the `BOT_TOKEN` in the `.env` file with your Telegram Bot Token.

3. Build and run the Docker containers:

   ```shell
   docker-compose up -d
   ```

   This will start the bot service.

## Usage

1. Start a chat with the bot on Telegram.
2. Send Latin text to the bot.
3. The bot will reply with the converted Georgian text and translation links to Google Translate and Yandex.Translate for different languages.

## Additional Information

### Directory Structure

- `bot/`: Contains the bot-related files.
  - `Dockerfile`: Docker configuration for the bot.
  - `requirements.txt`: Python dependencies.
  - `main.py`: Main script for the Telegram bot.
- `compose.yml`: Docker Compose configuration.
- `.env.example`: Example environment file for the bot token.

### Dependencies

- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- [transliterate](https://pypi.org/project/transliterate/)

### Development and Contributions

Feel free to contribute to this project by submitting issues or pull requests. Any improvements or bug fixes are appreciated!

## Authors

- [@nett00n](https://github.com/nett00n)

---

2024, Sakartvelo
