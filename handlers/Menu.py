from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext

def Bosh_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Asosiy Menu",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("🛍️ Buyurtma berish", web_app=WebAppInfo("https://asaxiy.uz/"))],
                [KeyboardButton("📦 Buyurtmalarim"), KeyboardButton("⚙️ Sozlamalar")],
                [KeyboardButton("ℹ️ Biz haqimizda"), KeyboardButton("🖊️ Fikr qoldirish")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def Bosh_menu02(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="✅ Telefon raqamingiz muvaffaqiyatli o'zgartirildi",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("🛍️ Buyurtma berish", web_app=WebAppInfo("https://asaxiy.uz/"))],
                [KeyboardButton("📦 Buyurtmalarim"), KeyboardButton("⚙️ Sozlamalar")],
                [KeyboardButton("ℹ️ Biz haqimizda"), KeyboardButton("🖊️ Fikr qoldirish")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
