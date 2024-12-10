from bot import Bot
import asyncio
from log import setup_logging,logger

setup_logging()

if __name__ == '__main__':

    bot = Bot()

    try:
        asyncio.run(bot.start())
    except Exception as e:
        logger.critical("Critical error occurred: {}".format(e))
    finally:
        logger.info("LXBot停止运行了呢，似乎发生了非常严重的错误呢.")
        
