import logging
import asyncio

logger = logging.getLogger("LXBot.Plugin.debug")

class P_debug_Plugin:
    async def on_message(self,message,bot):
        logger.info(f"Received message: {message}")