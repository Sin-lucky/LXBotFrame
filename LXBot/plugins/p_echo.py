import logging
import asyncio
from OBApi import send_private_msg

logger = logging.getLogger("LXBot.Plugin.echo")

class P_echo_Plugin:
    async def on_message(self, message, bot):
        message_type=message.get('message_type')
        #logger.info(f"Got message: {message}")
        if message_type == 'private':
            send_private_msg(bot.base_url, message.get("sender").get("user_id"), message.get("raw_message") ,bot.token)