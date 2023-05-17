from . import bot
from telebot import TeleBot
from telebot.types import Message
from handler import handle
from image_module import main
def mess(message:Message , bot:TeleBot):

    #image=main.MODIFICATION(cross="25x",Perpetual="BNBUSDT",Situation="LONG",percentage="144.5",Entry_Price=0.09756,last_price=0.34537,referral_code=7656445,type="type_B",img="saved/Type_D.JPG").WriteOnImage_type_b()
    image=main.MODIFICATION(img="saved/Type_A_5[no TP-SL][no25x].jpg",cross="Cross 20x",Perpetual="ENSUSDT",Unrealized_PNL=88.44,ROE=144.84,Size=1221.263,Margin=61.06,Risk=4.65,Entry_Price=9.350,Mark_Price=10.080,Liq_Price=6.931,type="type_a").WriteOnImage_type_a()
    bot.send_photo(message.from_user.id,photo=image)
if __name__=="__main__":
    bot.register_message_handler(callback=handle.input_hanlder,commands=['get_card'],pass_bot=True)
    bot.register_message_handler(callback=handle.web,commands=['get'],pass_bot=True)
    bot.register_message_handler(callback=handle.mess,func= lambda message : message.web_app_data != None ,pass_bot=True)
    bot.infinity_polling()
