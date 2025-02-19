from aiogram import Bot, types, Dispatcher, executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7736606067:AAH15fIuJvJXx12oDxFF-jnYlLmk7DdNt4U')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://vk.com/feed')))
    await message.answer('Привет! ', reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)