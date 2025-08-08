from telegram import Update
from telegram.ext import CallbackContext

def handler_order(update:Update,context:CallbackContext):
    update.message.reply_text(
        text="Sizda hali birorta ham buyurtma yo`q"
    )

