from aiogram import types

def create_keyboard(info):
    btns = []
    for i in info:
        text = str(i[1])    
        if ',' in text:
            double_btn = []
            spitted = text.split(', ')
            for spl in spitted:
                btn = types.KeyboardButton(text=spl)
                double_btn.append(btn)
            btns.append(double_btn)
        else:
            btn = [types.KeyboardButton(text=text)]
            btns.append(btn)
    keyboard = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return keyboard

def create_inline_keyboard(info):
    if isinstance(info, tuple):
        btn = [
            [types.InlineKeyboardButton(text=info[4], callback_data=info[4], url=info[3])],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=btn)
    else:
        btns = []
        for i in info:
            if ',' in i[1]:
                double_btn = []
                spitted = i[1].split(', ')
                for spl in spitted:
                    btn = types.InlineKeyboardButton(text=spl, callback_data=info)
                    double_btn.append(btn)
                btns.append(double_btn)
            else:
                btn = [types.InlineKeyboardButton(text=i[1])]
                btns.append(btn)
        keyboard = types.InlineKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return keyboard