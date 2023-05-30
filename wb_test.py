import os

import asyncio

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from utils import search_item_position

load_dotenv()

TEST_BOT_TOKEN = os.getenv("TEST_BOT_TOKEN")

bot = Bot(token=TEST_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("""
Бот выдает занимаемое место карточки в выдаче по поисковому запросу.
Для этого сформируйте запрос в формате "поисковый запрос" - "артикул товара"
    """)


@dp.message_handler()
async def test(message: types.Message):
    msg = message.text.split("-")
    item_id = msg[0].strip()
    if not item_id.isnumeric():
        await message.answer('введите артикул из цифр')
        return
    keyword = msg[1].strip()
    result = search_item_position(item_id, keyword)
    if not result:
        await message.answer(f"Карточка с артикулом {item_id} не найдена по запросу {keyword}")
    else:
        await message.answer(f"Карточка с артикулом {item_id} находится на странице {result[0]} на {result[1]} месте")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
