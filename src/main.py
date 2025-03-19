import asyncio
import logging
import keyboard
import services.ram_service as services
import repositories.ram_repository as repositories
from session import session
from models import ram_model as models
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from config.local_settings import Settings


logging.basicConfig(level=logging.INFO)

bot = Bot(token=Settings.bot_token)

dp = Dispatcher()

@dp.message(CommandStart())
async def menu(msg: Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    full_name = msg.from_user.full_name

    user_service = services.UserService(await session.get_db_session(), repositories.UserRepository, models.User)
    
    user = await user_service.get_one(id=id)

    if user:
        text = f'С возвращением, {username}!'
    else:
        user = await user_service.create(id=user_id, username=user, full_name=full_name)
        text = f'Здравствуй, {username}! Бот активирован.'

    await msg.answer(text, reply_markup=keyboard.menu)


@dp.message(F.text == "Меню")
@dp.message(F.text == "Выйти в меню")
@dp.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer('Главное меню', reply_markup=keyboard.menu)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())