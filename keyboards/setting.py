from telegram import Update,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import CallbackContext

def handler_setting(update:Update,context:CallbackContext):
        bot = context.bot
        user = update.effective_user
        bot.send_message(
                chat_id = user.id,
                text = "⚙️ Sozlamalar",
                reply_markup = ReplyKeyboardMarkup(
                        keyboard=[
                                [KeyboardButton("🌐 Tilni o'zgartirish")],
                                [KeyboardButton("📞 Telefon raqamingizni o'zgartiring")],
                                [KeyboardButton("⬅️ Orqaga")]
                        ],resize_keyboard=True,
                        one_time_keyboard=True
                )
      )