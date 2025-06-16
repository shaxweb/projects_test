from aiogram import Bot, Dispatcher, executor
from aiogram.types import *

bot = Bot("8158445939:AAHmoesq6Em6F5QdxcNhRJYSVL2pTLpUyn0")

async def send_message(message):
  await bot.send_message(
    chat_id=6181120570,
    text=message
  )
