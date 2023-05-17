from telebot import TeleBot
import os
apikey=os.getenv('TOKEN',default='1649598540:AAE0Q-XfbHkfsqrEr6LfyDJDBbYF7vq0uUE')
#apikey='1649598540:AAE0Q-XfbHkfsqrEr6LfyDJDBbYF7vq0uUE'
bot=TeleBot(apikey)