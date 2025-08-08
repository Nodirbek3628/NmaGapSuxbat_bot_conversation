from telegram import ReplyKeyboardMarkup,KeyboardButton

def get_language_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
        KeyboardButton(text = '🇺🇿  Uzbek', callback_data='lang:uz'),
        KeyboardButton(text = '🇬🇧 English', callback_data='lang:en')
        ]
    ]
    return ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

