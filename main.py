from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler,Filters
from handlers import start,cancel,order,about,language,Menu,idea
from handlers.register import start_register,set_name,set_gender,set_location,set_number
from config.config import TOKEN
from config import states
from keyboards import setting,contact02






def main()->None:

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    #Command Handlers 
    dispatcher.add_handler(CommandHandler("start",start.start))
    
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("^(Ro'yxatdan o'tish|Registration)$"), start_register)],
        states={
            states.NAME: [MessageHandler(Filters.text, set_name)],
            states.GENDER: [MessageHandler(Filters.text, set_gender)],
            states.LOCATION: [MessageHandler(Filters.location, set_location)],
            states.NUMBER: [MessageHandler(Filters.contact, set_number)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    
    #Messege Handlers
    dispatcher.add_handler(MessageHandler(Filters.text("🇺🇿  Uzbek"),start.hendler_start))
    dispatcher.add_handler(MessageHandler(Filters.text("Bosh Sahifa"),Menu.Bosh_menu))
    dispatcher.add_handler(MessageHandler(Filters.text("📦 Buyurtmalarim"),order.handler_order))
    dispatcher.add_handler(MessageHandler(Filters.text("ℹ️ Biz haqimizda"),about.handler_about))
    dispatcher.add_handler(MessageHandler(Filters.text("⚙️ Sozlamalar"),setting.handler_setting))
    dispatcher.add_handler(MessageHandler(Filters.text("🌐 Tilni o'zgartirish"),language.handler_language))
    dispatcher.add_handler(MessageHandler(Filters.text("📞 Telefon raqamingizni o'zgartiring"),contact02.handler_contact))
    dispatcher.add_handler(MessageHandler(Filters.contact,Menu.Bosh_menu02))
    dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Orqaga"),Menu.Bosh_menu))
    dispatcher.add_handler(MessageHandler(Filters.text("🖊️ Fikr qoldirish"),idea.handler_idea))

    
   
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
