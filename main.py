import telebot
import threading as tread

from config import *
from function import *
from button import *
from message import *
import parser 


bot = telebot.TeleBot(token)


tr = tread.Thread(target = parser.Main)
tr.start()


@bot.message_handler(commands = ["admin"])
def GetAdmin(message):
    chat_id = message.chat.id
    username = message.chat.username
    
    Message = RusMessage()
    Button = RusButton()
    
    
    data = GetAdmins()
    podl = False
    
    for i in data:
        if i == chat_id:
            podl = True
            break

    if podl:
        bot.send_message(chat_id, Message.admin_hello, reply_markup = Button.admin_menu)
    else:
        bot.send_message(chat_id, Message.you_not_admin)
            



@bot.message_handler(commands = ["start"])
def GetStarted(message):
    chat_id = message.chat.id
    username = message.chat.username
    
    data = GetUser(chat_id)
    
    if data is None:
        RegNewUser(chat_id, username, f"{message.chat.first_name} {message.chat.last_name}")
    else:
        ToMenu(chat_id)

       
    lang = GetLanguage(chat_id)
    
    if lang[0] == 'ru':
        Message = RusMessage()
        Button = RusButton()
    elif lang[0] == 'en':
        Message = EngMessage()
        Button = EngButton()
    else:
        print("Егог")
    
    
    bot.send_message(chat_id, Message.hello_text, reply_markup = Button.best_menu, parse_mode = "Markdown")



@bot.message_handler(content_types = ["text"])
def GetMessages(message):
    chat_id = message.chat.id
    username = message.chat.username
    
    land = GetLanguage(chat_id)
    mode = GetMode(chat_id)
    
    if land[0] == 'ru':
        Message = RusMessage()
        Button = RusButton()
    elif land[0] == 'en':
        Message = EngMessage()
        Button = EngButton()
    else:
        print("Егог")
        
        
        
    #ОБМЕН
    if message.text == "Обмен" or message.text == "Exchange":
        part = "Ready"
        
        Obmen32(part, None, chat_id)
        bot.send_message(chat_id, Message.select_obmen_type, reply_markup = Button.select_obmen_type_menu, parse_mode = "Markdown")
        
        
    if mode[0][0] == "Obmen" and mode[1][0] == "part3":
        
        type = GetTypeReq(chat_id)
        print(type[0])
        
        if type[0] == "kripto-rub":    
            part = "EnterKripto"
            
        elif type[0] == "rub-kripto":    
            part = "EnterRub"
            
            
        try:
            data = message.text
            data = data.replace(",", ".")
            data = float(data)
            
            Obmen32(part, data, chat_id)
            
            bot.send_message(chat_id, Message.enter_payload, parse_mode = "Markdown")
            
            
        except ValueError:
            bot.send_message(chat_id, Message.type_error)
            
            
    if mode[0][0] == "Obmen" and mode[1][0] == "part4":
        part = "EnterPayload"
        Obmen32(part, message.text, chat_id)
        
        data = GetData(chat_id)
        print(data)
        if data[0] == "kripto-rub":    
            bot.send_message(chat_id, f"Вы меняете: *{data[1]}* на *рубли*\nВы вкладываете: *{data[2]}*\nВы получаете: *{data[3]}*\nКомиссия составляет *{data[5][0][1]}%*\n\nВсё верно?", reply_markup = Button.is_true, parse_mode = "Markdown")
                
        elif data[0] == "rub-kripto":    
            bot.send_message(chat_id, f"Вы меняете: *рубли* на *{data[1]}*\nВы вкладываете: *{data[3]}*\nВы получаете: *{data[2]}*\nКомиссия составляет *{data[5][0][0]}%*\n\nВсё верно?", reply_markup = Button.is_true, parse_mode = "Markdown")
            
            
            

    if message.text == "Гaрантии" or message.text == "Guarantees":
        bot.send_message(chat_id, Message.garants, reply_markup = Button.to_menu)
    elif message.text == "Контакты" or message.text == "Contacts":
        bot.send_message(chat_id, Message.contacts, reply_markup = Button.to_menu)
        
        
        
    if message.text == "Изменить язык" or message.text == "Change the language":
        bot.send_message(chat_id, Message.select_lang, reply_markup = Button.langs_menu)
        ResetLanguage("part_1", chat_id, None)
        

    
    if message.text == "Обратная связь" or message.text == "Feedback":
        bot.send_message(chat_id, Message.feedback_part1, reply_markup = Button.to_menu)
        GetFeedBack("read", chat_id)
    
       
    if mode[0][0] == "FeedBack" and mode[1][0] == "part1":
        bot.send_message(chat_id, Message.feedback_part2, reply_markup = Button.to_menu)
        data = [chat_id, message.text]
        GetFeedBack("send_text", data)  
        ToMenu(chat_id)
        
        SendFeedback(bot = bot, username = username)



@bot.callback_query_handler(func = lambda call: True)
def GetCallBackData(call):
    chat_id = call.message.chat.id
    username = call.message.chat.username
    
    land = GetLanguage(chat_id)
    
    if land[0] == 'ru':
        Message = RusMessage()
        Button = RusButton()
    elif land[0] == 'en':
        Message = EngMessage()
        Button = EngButton()
    else:
        print("Егог")

        
    if call.data == "ToMenu":
        bot.send_message(chat_id, Message.hello_text, reply_markup = Button.best_menu, parse_mode = "Markdown")
        ToMenu(chat_id)
        
        
        
    #Админ панель
    
    if call.data == "SelectAllRate":
        rate = GetRates()
        
        bot.send_message(chat_id, f"*Bitcoin*: {rate[0]} rub\n*Litecoin*: {rate[1]} rub\n*Ethereum*: {rate[2]} rub", parse_mode = "Markdown")
        
        
    if call.data == "SelectAllComission":
        com = GetComission()
        
        bot.send_message(chat_id, f"Комиссия при продаже криптовалюты: {com[0]}%\nКомиссия при покупке криптовалюты: {com[1]}%")
    
    #/Админ панель
        
        
        
    mode = GetMode(chat_id)
    if mode[0][0] == "ResetLanguage" and mode[1][0] == "part1":
        bot.send_message(chat_id, Message.lang_update)
        ResetLanguage("part_2", chat_id, call.data)
        ToMenu(chat_id)
        
        

    if mode[0][0] == "Obmen" and mode[1][0] == "part1":
        part = "SelectType"
        Obmen32(part, call.data, chat_id)
        
        bot.send_message(chat_id, Message.select_kripto, reply_markup = Button.select_kripto_menu, parse_mode = "Markdown")
        
    if mode[0][0] == "Obmen" and mode[1][0] == "part2":
        part = "SelectKripto"
        Obmen32(part, call.data, chat_id)

        bot.send_message(chat_id, Message.enter_value, parse_mode = "Markdown")
        
    if mode[0][0] == "Obmen" and mode[1][0] == "part5":
        if call.data == "Yes":
            result = GetData(chat_id)             
            if result[0] == "kripto-rub":     
                reqi = GetReq(result[1])
                      
                bot.send_message(chat_id, Message.yes_kripto_in.format(f"{result[2]} {result[1]}", reqi[0]), reply_markup = Button.sell, parse_mode = "Markdown")
            elif result[0] == "rub-kripto":
                reqi = GetReq(result[1])
                
                bot.send_message(chat_id, Message.yes_kripto_in.format(f"{result[3]} рублей", reqi[0]), reply_markup = Button.sell, parse_mode = "Markdown")
        if call.data == "No":
            bot.send_message(chat_id, Message.no_kripto_in)
            DelLastReq(chat_id)
            
    
    if call.data == "SELL":
        bot.send_message(chat_id, Message.req_send_admin, reply_markup = Button.to_menu, parse_mode = "Markdown")
        Obmen32("AddToTable", None, chat_id)
        SendNewReq(username, bot)


bot.polling(non_stop = True)