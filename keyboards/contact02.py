from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CallbackContext


def handler_contact(update:Update,context:CallbackContext):
    update.message.reply_text(
        text="Iltimos, telefon raqamingizni yuboring",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mening raqamim",request_contact=True)],
                [KeyboardButton("⬅️ Orqaga")]
            ],resize_keyboard=True,
            one_time_keyboard=True
        )
    )