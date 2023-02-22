import telegram
#pip install python-telegram-bot==13.15
my_token = "MY TOKEN"

# Create token
bot = telegram.Bot(token = my_token)

# Send text message
#bot.sendMessage(chat_id="MY ID", text="TestPycharm")
bot.sendPhoto(chat_id="MY ID", photo=open("a.jpg", "rb"), caption="Warning !!!")