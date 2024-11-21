# Stock Price Alert Telegram Bot

## Table of Contents
- [About Project](#about-project)
- [Installation](#installation)
- [Use/Run the Project](#userun-the-project)
- [Features](#features)
- [Contribution](#contribution)
- [License](#license)
- [Contact Me](#contact-me)

## About Project
The **Stock Price Alert Telegram Bot** allows users to set alerts for stock prices. The bot notifies the user when a stock reaches the specified price. Users can subscribe or unsubscribe from stock price alerts and check their active subscriptions. It fetches stock prices using the Yahoo Finance API (`yfinance` library) and provides real-time notifications via Telegram.
**Live Demo**: [@SAStockAlertBot](https://web.telegram.org/k/#@SAStockAlertBot)

## Installation

### Steps to Clone Repo and Install Requirements
1. Clone the repository:
   ```bash
   git clone https://github.com/anandsundaramoorthysa/Stock-Prize-Alert-Telegram-Bot/
   cd Stock-Prize-Alert-Telegram-Bot
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Use/Run the Project

### 1. **Create a New Telegram Bot**
To create a new bot and get the bot token, follow these steps:
1. Open Telegram and search for the **BotFather**.
2. Start a conversation with **BotFather** and send the command `/newbot`.
3. Follow the prompts to choose a name and a username for your bot. The username must end in "bot" (e.g., `StockAlertBot`).
4. After successfully creating the bot, **BotFather** will provide you with a bot token (e.g., `123456789:ABCDEF...`).
5. Copy this bot token, and replace the `BOT_TOKEN` in the code with this token.

### 2. **Run the Bot Locally**
1. Make sure to have your virtual environment activated.
2. Run the bot:
   ```bash
   python app.py
   ```
   - This will start the bot in the **Bash console**. You should see the bot running, and it will start accepting commands.

3. The bot will start running and wait for commands from users. You can interact with your bot in Telegram by sending the following commands:
   - `/start`: To start using the bot.
   - `/subscribe <stock name> <price>`: To subscribe to stock price alerts.
   - `/unsubscribe <stock name>`: To unsubscribe from a stock alert.
   - `/myalerts`: To view your active subscriptions.

### 3. **Deploy the Bot on PythonAnywhere**
To host the bot on PythonAnywhere and keep it running 24/7 in the **Bash console**, follow these steps:

#### a. **Create a PythonAnywhere Account**
1. Go to [PythonAnywhere](https://www.pythonanywhere.com) and create a free account.

#### b. **Set Up Your Environment on PythonAnywhere**
1. Log in to PythonAnywhere.
2. Go to the **Files** tab and upload your entire project folder (`Stock-Prize-Alert-Telegram-Bot`) including the `app.py` and `requirements.txt` files.
3. Under the **Consoles** tab, start a new **Bash** console.
4. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
5. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
6. Install the required dependencies:
   ```bash
   pip install -r /home/yourusername/Stock-Prize-Alert-Telegram-Bot/requirements.txt
   ```

#### c. **Run the Bot in the Bash Console**
1. In the same **Bash** console, run the bot:
   ```bash
   python /home/yourusername/Stock-Prize-Alert-Telegram-Bot/app.py
   ```

2. The bot will now run in the Bash console, and you can keep it running as long as the console is open.

3. The bot will accept commands like `/subscribe <stock name> <price>`, `/unsubscribe <stock name>`, and `/myalerts`.

### Notes:
- **Bash Console**: As long as the console is open, the bot will continue running. If you close the console, the bot will stop. For long-term hosting, you may want to keep the console running in the background.
- **No Scheduled Tasks or Always-On**: For free accounts on PythonAnywhere, you unable to use this two features. Which also don’t need for this bot. So, Simply running the script in the Bash console will keep the bot active.

## Features
- Subscribe to stock price alerts with a specific target price.
- Receive notifications when the stock reaches or exceeds the target price.
- View your active subscriptions with `/myalerts`.
- Unsubscribe from stock price alerts with `/unsubscribe`.
- The bot checks the stock prices every minute in the background.

## Contribution
Feel free to fork the repository, make improvements, and create pull requests. Contributions are always welcome.

## License
This project is open-source and available under the MIT License.

## Contact Me
- **Email**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Inquiry%20About%20Stock%20Price%20Alert%20Telegram%20Bot%20Project&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Stock%20Price%20Alert%20Telegram%20Bot%20project%20you%20developed.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])
- **LinkedIn**: [Anand's LinkedIn Profile](https://www.linkedin.com/in/anandsundaramoorthysa/)
