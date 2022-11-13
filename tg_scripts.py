import json
from aiogram import types


def update_button(): #кнопка "Обновить"
    keys = types.InlineKeyboardMarkup()
    key = types.InlineKeyboardButton(text="🔄 Обновить", callback_data=json.dumps({"act": "update"}))
    keys.add(key)
    return keys


async def is_chat(message: str) -> bool:
    return True if message.chat.type in ['supergroup', 'group'] else False


async def return_message(message: str, text=None, reply_markup=None, sticker=None) -> None:
    if text != None:
        await message.reply(text, reply_markup=reply_markup) if await is_chat(message) else await message.answer(text, reply_markup=reply_markup) 
    if sticker != None:
        await message.reply_sticker(sticker) if await is_chat(message) else await message.answer_sticker(sticker) 