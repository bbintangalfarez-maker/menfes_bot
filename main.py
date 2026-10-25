import telebot

BOT_TOKEN =8923043240:AAH7tCCMFVG2jgpMm7wv9zLvEmXAPlK6fMo
CHANNEL_ID = -1004317472768

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Kirim menfes lu disini!")

@bot.message_handler(func=lambda m: True)
def menfes(message):
    text = f"📩 MENFES:\n\n{message.text}"
    bot.send_message(CHANNEL_I
    
