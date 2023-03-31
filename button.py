from telebot import types

class RusButton:
    best_menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
    to_menu = types.InlineKeyboardMarkup()
    langs_menu = types.InlineKeyboardMarkup()
    select_obmen_type_menu = types.InlineKeyboardMarkup()
    select_kripto_menu = types.InlineKeyboardMarkup()
    is_true = types.InlineKeyboardMarkup()
    sell = types.InlineKeyboardMarkup()
    
    admin_menu = types.InlineKeyboardMarkup()
    ban_menu = types.InlineKeyboardMarkup()
    users_menu = types.InlineKeyboardMarkup()
    obmen_menu = types.InlineKeyboardMarkup()
    
    
    item1 = types.KeyboardButton("Обмен")
    item2 = types.KeyboardButton("Гaрантии")
    item3 = types.KeyboardButton("Контакты")
    item4 = types.KeyboardButton("Изменить язык")
    item5 = types.KeyboardButton("Обратная связь")
    best_menu.add(item1)
    best_menu.add(item2, item3)
    best_menu.add(item4, item5)
        
    item_to = types.InlineKeyboardButton(text = "В меню", callback_data = "ToMenu")
    to_menu.add(item_to)
    
    item1 = types.InlineKeyboardButton(text = "Русский", callback_data = "ru")
    item2 = types.InlineKeyboardButton(text = "English", callback_data = "en")
    langs_menu.add(item1)
    langs_menu.add(item2)
    langs_menu.add(item_to)
    
    
    item1 = types.InlineKeyboardButton(text = "Криптовалюта => Рубли", callback_data = "kripto-rub")
    item2 = types.InlineKeyboardButton(text = "Рубли => Криптовалюта", callback_data = "rub-kripto")
    select_obmen_type_menu.add(item1)
    select_obmen_type_menu.add(item2)
    select_obmen_type_menu.add(item_to)
    
    item1 = types.InlineKeyboardButton(text = "Bitcoin", callback_data = "bitcoin")
    item2 = types.InlineKeyboardButton(text = "Ethereum", callback_data = "ethereum")
    item3 = types.InlineKeyboardButton(text = "Litecoin", callback_data = "litecoin")
    select_kripto_menu.add(item1)
    select_kripto_menu.add(item2)
    select_kripto_menu.add(item3)
    select_kripto_menu.add(item_to)
    
    item1 = types.InlineKeyboardButton(text = "Да", callback_data = "Yes")
    item2 = types.InlineKeyboardButton(text = "Нет", callback_data = "No")
    is_true.add(item1)
    is_true.add(item2)
    is_true.add(item_to)
    
    item1 = types.InlineKeyboardButton(text = "Я оплатил", callback_data = "SELL")
    sell.add(item1)
    sell.add(item_to)
    
    item1 = types.InlineKeyboardButton(text = "Просмотр пользователей", callback_data = "SelectAllUsers")
    item2 = types.InlineKeyboardButton(text = "Просмотр запросов", callback_data = "SelectAllRequest")
    item3 = types.InlineKeyboardButton(text = "Просмотр комисиы", callback_data = "SelectAllComission")
    item4 = types.InlineKeyboardButton(text = "Просмотр курсов валют", callback_data = "SelectAllRate")
    item5 = types.InlineKeyboardButton(text = "Просмотр риквизитов сервиса", callback_data = "SelectAllPayload")
    admin_menu.add(item1)
    admin_menu.add(item2)
    admin_menu.add(item3)
    admin_menu.add(item4)
    admin_menu.add(item5)
        
        
        
        
        
class EngButton:
    best_menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
    to_menu = types.InlineKeyboardMarkup()
    langs_menu = types.InlineKeyboardMarkup()
    
    
    item1 = types.KeyboardButton("Exchange")
    item2 = types.KeyboardButton("Guarantees")
    item3 = types.KeyboardButton("Contacts")
    item4 = types.KeyboardButton("Change the language")
    item5 = types.KeyboardButton("Feedback")
    best_menu.add(item1)
    best_menu.add(item2, item3)
    best_menu.add(item4, item5)
        
    item1 = types.InlineKeyboardButton(text = "On the menu", callback_data = "ToMenu")
    to_menu.add(item1)
        
        
    item1 = types.InlineKeyboardButton(text = "Русский", callback_data = "ru")
    item2 = types.InlineKeyboardButton(text = "English", callback_data = "en")
    langs_menu.add(item1)
    langs_menu.add(item2)