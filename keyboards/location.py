from telegram import ReplyKeyboardMarkup,KeyboardButton

def get_location_keyboard():
    keyboard =[
    [KeyboardButton(text = "location",request_location=True,)]]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,one_time_keyboard=True,
        resize_keyboard=True
        )