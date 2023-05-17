from telebot import TeleBot
from telebot.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo
from card_gen import gen
def input_hanlder(message:Message,bot:TeleBot):
    print(message)
    message_price=bot.send_message(message.from_user.id,text=f"send the data in this formate 'perpentual-entry_price-exit_price-Margin_usdt-type_trade,cross'")
    bot.register_next_step_handler(message_price,callback=hanlde_data,bot=bot)
def hanlde_data(message:Message,bot):
    bot.send_message(message.from_user.id,text="hi")
    data=message.text.split("-")
    print(data)
    import requests
    import json
    try:
        result=requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    except Exception as e:
        print(e)
        bot.send_message(message.from_user.id,text="Some error occured with binance api")
        return
    #print(result.json())
    if result.status_code !=200:
        print("something went wrong")
        return
    place=None
    for coin in result.json()['symbols']:
        if str(coin['symbol'])==str(data[0].strip()):
            place=coin['pricePrecision']
    if not place:
        bot.send_message(message.from_user.id,text="Perpetual not found")
        return
        
    image=gen.Generator(Perpetual=data[0],place=place,entry_price=data[1],exit_price=data[2],Margin_usdt=data[3],type_trade=data[4],cross=float(data[5])).profit_card()
    bot.send_photo(message.from_user.id , photo=image)
    info_img=gen.Generator(Perpetual=data[0],place=place,entry_price=data[1],exit_price=data[2],Margin_usdt=data[3],type_trade=data[4],cross=float(data[5])).info_card()
    bot.send_photo(message.from_user.id,photo=info_img)
def web(message:Message,bot:TeleBot):
    web_app=WebAppInfo(url="https://harshitprof.github.io/Html2")
    button=[InlineKeyboardButton(text="input",web_app=web_app)]
    markup=InlineKeyboardMarkup()
    markup.add(*button)
    bot.send_message(message.from_user.id,text="Hello",reply_markup=markup)
def mess(message:Message,bot:TeleBot):
    data=message.web_app_data.data.split("-")
    print(data)
    image=gen.Generator(Perpetual=data[0],entry_price=data[1],exit_price=data[2],Margin_usdt=data[3],type_trade=data[4],cross=float(data[5])).profit_card()
    bot.send_photo(message.from_user.id , photo=image)
    info_img=gen.Generator(Perpetual=data[0],entry_price=float(data[1]),exit_price=float(data[2]),Margin_usdt=float(data[3]),type_trade=data[4],cross=float(data[5])).info_card()
    bot.send_photo(message.from_user.id,photo=info_img)