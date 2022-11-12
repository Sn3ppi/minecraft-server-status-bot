import threading
import json

from aiogram import Bot, types, executor
from aiogram.utils import exceptions
from aiogram.dispatcher import Dispatcher
import asyncio

from displays import Errors
from displays import ServerMessages
import settings
import statuses
from tg_scripts import update_button, return_message


bot = Bot(token=settings.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

error_messages = Errors()
server_messages = ServerMessages()


@dp.errors_handler(exception=exceptions.MessageNotModified)
async def message_not_modified(update: types.Update, exception: exceptions.CantInitiateConversation):
    return True


@dp.errors_handler(exception=exceptions.RetryAfter)
async def flood_wait_retry_after(update: types.Update, exception: exceptions.RetryAfter):
    print(error_messages.many_clicks(exception.timeout))
    await asyncio.sleep(exception.timeout)
    return True


@dp.message_handler(text=[f"{settings.USERNAME}"])
async def sneppi(message: types.Message):  
    await return_message(message, sticker="CAACAgIAAxkBAAEKmttg276yQK1rvsQSBM80_Eyc0gt2DAACCQADci8wB6PyDmoZHBAlIAQ")


@dp.message_handler(commands=['start', 'help'])
async def server_help(message): 
    await return_message(message, server_messages.help())


@dp.message_handler(commands=['status'])
async def serverStatus(message):
    await return_message(message, statuses.parse_data(), reply_markup=update_button())
        

@dp.callback_query_handler(text=json.dumps({"act": "update"}))
async def serverStatus(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=statuses.parse_data(), reply_markup=update_button())


def start():
    threading.Thread(name="ServerData", target=statuses.get_server_data, daemon=True).start()
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    start()