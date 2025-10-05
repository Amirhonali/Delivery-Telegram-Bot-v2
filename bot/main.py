import asyncio
from aiogram import Bot, Router, F, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import (Message, FSInputFile, KeyboardButton,
                           ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton)
from database import *

from config import TOKEN

bot = Bot(TOKEN)
rr = Router()
dp = Dispatcher()
dp.include_router(rr)


# @rr.message(Command('start'))
# async def start(message:Message, state: FSMContext):
#     await state.set_state(Register.main_menu)
#     text_info = get_restaurants()
#     await message.answer(f"{get_restaurants[0][]}", reply_markup=keyboard)