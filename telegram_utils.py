import telegram

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "MY TOKEN"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="MY ID", photo=open(photo_path, "rb"), caption="Warning !!!")
    except Exception as ex:
        print("Can not send message telegram, again please!", ex)

    print("Send Sucess")
