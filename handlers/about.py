from telegram import Update
from telegram.ext import CallbackContext


def handler_about(update:Update,context:CallbackContext):
      update.message.reply_text("Biz shu yerda Joylashganmz")
      update.message.reply_markdown_v2(
            text = "*Elektron pochta:* abloqulovnodirbek4\\@gmail\\.com",
            )