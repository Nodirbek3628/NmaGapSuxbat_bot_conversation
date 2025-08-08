from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CallbackContext


def handler_language(update:Update,context:CallbackContext):
    update.message.reply_text(
        text = "🌐 Tilni o'zgartirish",
        reply_markup =ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text = '🇺🇿  Uzbek'),KeyboardButton(text='🇬🇧 English')]
            ],resize_keyboard=True,
            one_time_keyboard=True
        )
    )
     