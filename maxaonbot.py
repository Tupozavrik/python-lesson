import telebot
import os
import random

bot = telebot.TeleBot('7736606067:AAH15fIuJvJXx12oDxFF-jnYlLmk7DdNt4U')

image_path = 'D:/bot/image.jpg'
hidden_object = None

def generate_2d_prompt():
    global hidden_object
    large_objects = [
        "дом", "дерево", "машина", "облако", "гора", "озеро", "здание",
        "мост", "самолет", "корабль", "замок", "небоскреб", "фонтан"
    ]
    small_objects = [
        "кошка", "собака", "птица", "бабочка", "цветок", "мяч", "книга",
        "яблоко", "монета", "ключ", "часы", "кружка", "карандаш"
    ]
    
    num_large_objects = random.randint(5, 8)
    selected_large_objects = random.sample(large_objects, num_large_objects)
    hidden_object = random.choice(small_objects)
    
    prompt = f"2D изображение, наполненное объектами: {', '.join(selected_large_objects)}."
    return prompt

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может отправлять изображения и генерировать промпты. Используйте команду /image, чтобы получить изображение, /prompt для генерации промпта, или /reveal чтобы узнать спрятанный объект.")

@bot.message_handler(commands=["image"])
def send_image(message):
    if os.path.exists(image_path):
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Вот изображение для вас!")
    else:
        bot.send_message(message.chat.id, "Извините, изображение не найдено.")

@bot.message_handler(commands=["prompt"])
def send_prompt(message):
    prompt = generate_2d_prompt()
    bot.send_message(message.chat.id, f"Вот ваш промпт для 2D изображения:\n\n{prompt}")
    bot.send_message(message.chat.id, "Используйте команду /reveal, чтобы узнать, какой объект спрятан.")

@bot.message_handler(commands=["reveal"])
def reveal_hidden_object(message):
    global hidden_object
    if hidden_object:
        bot.send_message(message.chat.id, f"Спрятанный маленький объект: {hidden_object}")
        hidden_object = None
    else:
        bot.send_message(message.chat.id, "Сначала сгенерируйте промпт с помощью команды /prompt")

bot.infinity_polling()