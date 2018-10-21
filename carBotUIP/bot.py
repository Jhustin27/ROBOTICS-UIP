#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import time
from config import CarRobot
from security import Security
import os
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuracion Token BOT Telegram
TOKEN = os.environ["BOT_TOKEN"]

carRobot = CarRobot('Demo  carrito',0) 
sec = Security()

def start(bot, update):
    keyboard = [
                [              
                    InlineKeyboardButton("Encender", callback_data='/encender')
                ],
                [
                    InlineKeyboardButton("Acelerar", callback_data='/acelerar'),
                    InlineKeyboardButton("Retroceder", callback_data='/retroceder')
                ],
                [              
                    InlineKeyboardButton("Girar a la Derecha", callback_data='/derecha'),
                    InlineKeyboardButton("Girar a la Izquierda", callback_data='/izquierda')
                 ],
                [
                    InlineKeyboardButton("Apagar", callback_data='/apagar')
                ]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Acciones que puedo realizar:', reply_markup=reply_markup)

def config(bot, update):
    custom_keyboard = [
        [
            KeyboardButton(text="/encender")
        ],
        [              
            KeyboardButton(text="/acelerar"),
            KeyboardButton(text="/retroceder"),
        ],
        [
            KeyboardButton(text="/izquierda"),
            KeyboardButton(text="/derecha"),
        ],
        [
            KeyboardButton(text="/apagar")
        ]
        ]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text('Estas son las acciones que puedo realizar:', reply_markup=reply_markup)

def button(bot, update):
    query = update.callback_query
    if query:
        print('query ', query.message)
	resp =  str(query.data)
        resp = resp.strip('/').lower()
	user_id = query.message.chat_id
    	message_id= query.message.message_id
    else:
	print(update.message.message_id, update.message.chat.id)
        query = update
        user_id = update.message.chat.id
        resp = update.message.text.strip('/').lower()
	message_id= update.message.message_id

    if not user_id in sec.list:
       bot.edit_message_text(
            text="Este usuario no cuenta con los permisos suficiente para ejecutar las acciones.",
            chat_id=user_id,
            message_id=message_id
        )
    else:
        if resp == 'encender':
            message = "🔑🔑🔑 Encendiendo 🔑🔑🔑"
            carRobot.encender()
        elif resp == 'apagar':
            message = "😴😴😴 Apagando 😴😴😴"
            carRobot.apagar()
        elif resp == 'acelerar':
            message = "🚗🚗🚗 Acelerando 🚗🚗🚗"
            carRobot.adelante()
        elif resp == 'retroceder':
            message = "🚨🚨🚨 Retrocediendo 🚨🚨🚨"
            carRobot.atras()
        elif resp == 'derecha':
            message = "↪️↪️↪️ Girando a la Derecha ↪️↪️↪️"
            carRobot.ir_derecha()
        elif resp == 'izquierda':
            message = "↩️↩️↩️ Girando a la Izquierda  ↩️↩️↩️"
            carRobot.ir_izquierda()
    
        if message is not None:
            print("Ejecutando ---> ", message)
          #  bot.edit_message_text(
           #     text=message,
            #    chat_id= user_id,
            #    message_id=message_id
           # )
	#    if not query:
            bot.send_message(
                    text=message,
                    chat_id= user_id,
                    message_id=message_id
                )


def user(bot, update):
    update.message.reply_text("@{} ahora tienes el control de un CarRobot.".format(update.message.chat.username))
    user_id = update.message.chat_id
    if not user_id in sec.list:
        sec.add(user_id)
        print("Escalando permisos ")
    else:
        print("Usuario ya tiene permisos ")

def help(bot, update):
    update.message.reply_text("!Bienvenido a la Ayuda de CarRobot!\n\nUse los comandos:\n/start para conocer las acciones del bot. \n/permiso para tener el control de un carRobot\n\n\nDesarrollo por: \n- Adrian Marin \n- Leonardo Esqueda @lesqueda \n- Maryon Torres @maryito")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def bot_init():
    """ Configurando ChatBot"""
    print(bot_init.__doc__)
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', config))
    updater.dispatcher.add_handler(CommandHandler('permiso', user))
    updater.dispatcher.add_handler(CommandHandler('config', config))
    updater.dispatcher.add_handler(CommandHandler('encender', button))
    updater.dispatcher.add_handler(CommandHandler('acelerar', button))
    updater.dispatcher.add_handler(CommandHandler('retroceder', button))
    updater.dispatcher.add_handler(CommandHandler('derecha', button))
    updater.dispatcher.add_handler(CommandHandler('izquierda', button))
    updater.dispatcher.add_handler(CommandHandler('apagar', button))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()
