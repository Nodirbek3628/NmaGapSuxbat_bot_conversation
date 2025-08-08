from telegram import ReplyKeyboardMarkup,KeyboardButton,WebAppInfo

def get_menu():
   keyboard=[
                [KeyboardButton("🛍️ Buyurtma berish", web_app=WebAppInfo("https://asaxiy.uz/"))],
                [KeyboardButton("📦 Buyurtmalarim"), KeyboardButton("⚙️ Sozlamalar")],
                [KeyboardButton("ℹ️ Biz haqimizda"), KeyboardButton("🖊️ Fikr qoldirish")]
            ]
   return ReplyKeyboardMarkup(keyboard=keyboard,resize_keyboard=True,one_time_keyboard=True)
