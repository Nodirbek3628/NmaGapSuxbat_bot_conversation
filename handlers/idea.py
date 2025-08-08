from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CallbackContext

def handler_idea(update:Update,context:CallbackContext):
      update.message.reply_markdown(
            "*Buyurtma berish uchun asosiy menyudagi “Buyurtma” tugmasidan foydalaning.*")
      bot = context.bot
      user = update.effective_user
      bot.send_message(
            chat_id = user.id,
            text = "Biz sizning fikr-mulohazalaringizni juda qadrlaymiz! Buyurtma berganingizdan so'ng, o'z fikr va mulohazalaringizni shu yerda qoldirishingiz mumkin.",
            reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                  [KeyboardButton("⬅️ Orqaga")]
            ],resize_keyboard=True,
            one_time_keyboard=True,)
      )