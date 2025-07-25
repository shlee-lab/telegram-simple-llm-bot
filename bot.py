import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Retrieve Telegram token and Gemini API key from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Retrieve allowed user IDs from .env (comma-separated string, e.g., "123456789,987654321")
allowed_ids_str = os.getenv('ALLOWED_USER_IDS', '')  # Default to empty if not set
ALLOWED_USER_IDS = [int(uid.strip()) for uid in allowed_ids_str.split(',') if uid.strip()]  # Convert to list of ints

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model (using 'gemini-1.5-flash' for free tier; adjust if needed)
model = genai.GenerativeModel('gemini-1.5-flash')

# Handler for the /start command
async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hello! I am an LLM-based chatbot using Google Gemini. Ask me anything.')

# Handler for text messages (non-commands)
async def handle_message(update: Update, context: CallbackContext) -> None:
    """Process user message and generate response using Gemini."""
    user_id = update.message.from_user.id
    if ALLOWED_USER_IDS and user_id not in ALLOWED_USER_IDS:  # Check if whitelist is set and user not allowed
        await update.message.reply_text("Sorry, you are not authorized to use this bot.")
        return
    user_message = update.message.text
    # Call Gemini to generate content
    response = model.generate_content(user_message)
    bot_reply = response.text
    await update.message.reply_text(bot_reply)

def main() -> None:
    """Main function to set up and run the Telegram bot."""
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
