from telegram import ReplyKeyboardMarkup,KeyboardButton

def get_contact_keyboard() ->ReplyKeyboardMarkup:
    keyboard=[
        [KeyboardButton("Contact",request_contact=True)]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard,resize_keyboard=True,one_time_keyboard=True) 