import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Replace with your bot token
BOT_TOKEN = "7814412283:AAHzuB-nTKxha5t1gda_VU7F3CQCvXf1_5c"
GAME_URL = "https://himan989.github.io/AviatorGame/"  # Replace with your Unity WebGL game link

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Send a message with a 'Play' button that opens the game inside Telegram."""
    keyboard = InlineKeyboardMarkup()
    
    # Correctly use WebAppInfo to open the game inside Telegram
    play_button = InlineKeyboardButton(
        "🎮 Play Now", web_app=WebAppInfo(url=GAME_URL)
    )
    
    keyboard.add(play_button)
    bot.send_message(message.chat.id, "Press the button below to play the game directly inside Telegram:", reply_markup=keyboard)

# Start polling
bot.polling()
