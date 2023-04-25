from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, "Покупки курса", "Покупка курса itProger", "invoice", config.PAYMENT_TOKEN, "USD", [types.LabeledPrice("Покупка товара", 5 * 100)])

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message: types.Message):
    await message.answer(f'Success: {message.successful_payment.order_info}')

executor.start_polling(dp)