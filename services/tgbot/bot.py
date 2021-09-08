import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.handlers.common import register_start_handler, register_ping_handler
from src.handlers.english import register_card_handlers
from config.config import Config

logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_start_handler(dp)
    register_ping_handler(dp)
    register_card_handlers(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info("Starting bot")

    storage = MemoryStorage()

    bot = Bot(token=Config.TG_BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
