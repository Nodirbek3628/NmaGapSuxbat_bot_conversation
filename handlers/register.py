from telegram import Update
from telegram.ext import CallbackContext,ConversationHandler
from  config import states
from keyboards.gender import get_gender_keyboard
from keyboards.location import get_location_keyboard
from keyboards.contact import get_contact_keyboard
from keyboards.menu import get_menu


def start_register(update:Update , context:CallbackContext):
    update.message.reply_text(
        "Ro'yxatdan o'tish uchun quyidagi malumotlaringizni yuboring.")
    
    update.message.reply_text("Ismingizni  Yuboring")

    return states.NAME

def set_name(update: Update, context: CallbackContext):
    name = update.message.text
    context.user_data['name'] = name

    update.message.reply_text("Ismizngiz  qabul qilindi")
    update.message.reply_text(
        "gender yuboring",
        reply_markup=get_gender_keyboard()
    )
    return states.GENDER

def set_gender(update:Update,context:CallbackContext):
    gender = update.message.text
    context.user_data["gender"] = gender

    update.message.reply_text("Gender qabul qilindi")
    update.message.reply_text(
        "Joylashuvni  yuboring",
        reply_markup=get_location_keyboard()
    )
    return states.LOCATION
def set_location(update: Update, context: CallbackContext):
    location = update.message.location
    context.user_data['location'] = {'latitude': location.latitude, 'longitude': location.longitude}

    update.message.reply_text("Joylashuv qabul qilindi")
    update.message.reply_text(
        "Contact yuboring",
        reply_markup=get_contact_keyboard()
    )
    return states.NUMBER

def set_number(update:Update,context:CallbackContext):
    contact = update.message.contact
    context.user_data['number'] = contact.phone_number

    update.message.reply_text("contact qabul qilindi")

    # save a new user into database

    update.message.reply_text(
        "✅ Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!",
        reply_markup=get_menu()
        
        )
    return ConversationHandler.END