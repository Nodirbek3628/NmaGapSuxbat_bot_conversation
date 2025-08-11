from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CallbackContext
from keyboards.get_language import get_language_keyboard
from keyboards.register import get_register_keyboard
from services import db
 


def start(update:Update,context:CallbackContext):
    user = update.effective_user

    db.create_user(user.id)

    update.message.reply_html(
        text = f"Assalomu alykum <b>{user.full_name}</b>! BIzning botimzga xush kelibsz."
    )

    update.message.reply_text(
        text="Tilni tanlang / Select language",
        reply_markup = get_language_keyboard()
    )


def hendler_start(update:Update,context:CallbackContext):
            bot = context.bot 
            user = update.effective_user
            bot.send_message(
                  chat_id = user.id,
                  text = "Ro'yxatdan o'ting",
                  reply_markup=get_register_keyboard())
                  

    