from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import yfinance as yf
import schedule
import time
import threading
import json
import os
import socket

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
subscribers = {}
stock_cache = {}

# File to persist subscriptions
SUBSCRIPTION_FILE = "subscriptions.json"

# Load subscriptions from file if it exists
def load_subscriptions():
    global subscribers
    if os.path.exists(SUBSCRIPTION_FILE):
        with open(SUBSCRIPTION_FILE, 'r') as f:
            subscribers = json.load(f)

# Save subscriptions to file
def save_subscriptions():
    with open(SUBSCRIPTION_FILE, 'w') as f:
        json.dump(subscribers, f)

# Function to check internet connectivity
def check_internet():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the SA Stock Price Alert Bot!\n\n"
        "Use /subscribe <stock name> <price> to set an alert.\n"
        "Example: /subscribe CIPLA 1000\n\n"
        "Use /unsubscribe <stock name> to stop receiving alerts.\n"
        "Example: /unsubscribe CIPLA 1000\n\n"
        "Use /myalerts to see your active subscriptions.\n\n"
        "You can subscribe to any stock using its ticker symbol (e.g., CIPLA, AAPL, TSLA)."
    )

# Subscribe command handler
async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /subscribe <stock name> <price>")
        return

    stock_name, price = context.args[0].upper(), int(float(context.args[1]))  # Convert price to integer

    # Check internet connection
    if not check_internet():
        await update.message.reply_text("Sorry, no internet connection. Please try again later.")
        return

    if user_id not in subscribers:
        subscribers[user_id] = []

    # Check if already subscribed to this stock
    if any(sub[0] == stock_name for sub in subscribers[user_id]):
        await update.message.reply_text(f"You are already subscribed to {stock_name}.")
        return

    # Get current price of the stock
    stock = yf.Ticker(stock_name)
    try:
        current_price = int(stock.history(period="1d")['Close'].iloc[-1])  # Get the current price as an integer
    except Exception as e:
        await update.message.reply_text(f"Could not fetch the price for {stock_name}. Please try again later.")
        return

    # Calculate the price difference
    price_difference = current_price - price

    # Check if current price is equal to the target price
    if current_price == price:
        message = (
            f"Subscribed to {stock_name} for price alert at {price}.\n"
            f"Current price is already at your target price: {current_price}."
        )
    else:
        message = (
            f"Subscribed to {stock_name} for price alert at {price}.\n"
            f"Current price: {current_price}.\n"
            f"Price difference: {price_difference}"
        )

    subscribers[user_id].append((stock_name, price))
    save_subscriptions()  # Save after subscribing

    await update.message.reply_text(message)

# Unsubscribe command handler
async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if len(context.args) < 1:
        await update.message.reply_text("Usage: /unsubscribe <stock name>")
        return

    stock_name = context.args[0].upper()
    if user_id in subscribers:
        original_len = len(subscribers[user_id])
        subscribers[user_id] = [
            (name, price) for name, price in subscribers[user_id] if name != stock_name
        ]
        if len(subscribers[user_id]) != original_len:
            save_subscriptions()  # Save after unsubscribing
            await update.message.reply_text(f"Unsubscribed from {stock_name}.")
        else:
            await update.message.reply_text(f"You have no subscriptions for {stock_name}.")
    else:
        await update.message.reply_text(f"You have no subscriptions for {stock_name}.")

# My alerts command handler
async def myalerts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id not in subscribers or not subscribers[user_id]:
        await update.message.reply_text("You have no active subscriptions.")
        return

    alerts = "\n".join([f"{name} at {price}" for name, price in subscribers[user_id]])
    await update.message.reply_text(f"Your active subscriptions:\n{alerts}")

# Check stock prices and send alerts
def check_prices() -> None:
    global stock_cache
    for user_id, alerts in subscribers.items():
        for stock_name, target_price in alerts:
            # Use cached prices to avoid redundant calls
            if stock_name not in stock_cache or time.time() - stock_cache[stock_name]["timestamp"] > 3600:
                stock = yf.Ticker(stock_name)
                try:
                    current_price = int(stock.history(period="1d")['Close'].iloc[-1])  # Get current price as an integer
                except Exception as e:
                    current_price = None
                if current_price:
                    stock_cache[stock_name] = {"price": current_price, "timestamp": time.time()}
            else:
                current_price = stock_cache[stock_name]["price"]

            if current_price and current_price >= target_price:
                application.bot.send_message(
                    chat_id=user_id,
                    text=f"ALERT! {stock_name} has reached your target price: {current_price}"
                )

# Background scheduler
def run_scheduler():
    schedule.every(1).minutes.do(check_prices)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main function
if __name__ == "__main__":
    load_subscriptions()  # Load subscriptions on startup

    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("subscribe", subscribe))
    application.add_handler(CommandHandler("unsubscribe", unsubscribe))
    application.add_handler(CommandHandler("myalerts", myalerts))

    # Start the price-check scheduler in a separate thread
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()

    # Start the bot
    application.run_polling()
