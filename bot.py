import logging
import feedgen.feed
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.utils.markdown import text

# устанавливаем уровень логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# инициализируем бота и диспетчер
bot = Bot(token="2102525803:AAEaZO3kudDFjcqvmUH9E2GamY35*********")
dp = Dispatcher(bot)

# обработчик команды /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    # отправляем приветственное сообщение
    await message.answer("Привет! Отправьте мне ссылку, и я сделаю из нее RSS-канал.")

# обработчик сообщений с ссылками
@dp.message_handler(regexp=r'^https?://')
async def get_link(message: types.Message):
    link = message.text
    # здесь можно сохранить ссылку в базу данных или в какой-то файл
    await message.answer("Отлично! Теперь отправьте команду /generate, чтобы создать RSS-канал.")

# обработчик команды /generate
@dp.message_handler(commands=["generate"])
async def generate_rss(message: types.Message):
    # здесь необходимо добавить код для извлечения записей из веб-страницы
    feed = feedgen.feed.FeedGenerator()
    feed.title("RSS-канал")
    feed.description("Моя RSS лента")
    # здесь можно получить сохраненную ссылку из базы данных или файла
    link = "https://example.com"
    feed.link(href=link, rel="alternate")
    # здесь необходимо добавить код для извлечения записей из веб-страницы
    entry = feed.add_entry()
    entry.title("Заголовок статьи")
    entry.link(href=link, rel="alternate")
    entry.description(text("Описание статьи"))

    # после формирования RSS-канала
    rss_feed = feed.rss_str(pretty=True)
    await message.answer(rss_feed)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
