import json
import asyncio
import websockets
import requests
import logging
from OBApi import *
import datetime
import importlib
import os

# 创建一个日志记录器，用于记录BOT的运行信息
logger = logging.getLogger("LXBotFrame")

class Bot:
    def __init__(self):
        # 从配置文件中加载配置
        self.config = json.load(open('config/config.json', 'r', encoding='utf-8'))
        self.token = self.config['token']
        self.admins = self.config['admin']
        self.ws_url = self.config['ws_url']
        self.http_url = self.config['http_url']
        self.report_port = self.config['report_port']
        self.send_start_message = self.config['send_start_message']
        self.send_start_message_to_admin = self.config['send_start_message_to_admin']
        self.base_url = self.http_url
        self.loaded_plugins = {}  # 保存加载的插件实例

    async def start(self):
        # 获取登录信息并记录
        login_info = get_login_info(self.http_url, token=self.token)
        logger.info("Bot 账号: {}".format(login_info['user_id']))
        logger.info("Bot 昵称: {}".format(login_info['nickname']))
        logger.info("日期: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        # 如果配置中需要发送启动消息，则发送给管理员
        if self.send_start_message:
            for admin in self.send_start_message_to_admin:
                send_private_msg(self.base_url, admin, "LXBot启动成功！", token=self.token)
                logger.info(f"向管理员 {admin} 发送启动通知")
        
        # 启动WebSocket服务器
        await self.websocket_server()

    async def load_plugins_from_folder(self, folder_path):
        # 遍历指定文件夹中的插件文件
        for filename in os.listdir(folder_path):
            if filename.startswith("p_") and filename.endswith(".py"):
                module_name = filename[:-3]  # 去掉文件后缀
                full_module_name = f"{folder_path}.{module_name}"

                # 动态导入模块
                module = importlib.import_module(full_module_name)
                class_name = module_name.replace("p_", "P_") + "_Plugin"

                if hasattr(module, class_name):
                    plugin_class = getattr(module, class_name)

                    # 实例化插件并存储到字典中
                    self.loaded_plugins[class_name] = plugin_class()
                    logger.info(f"插件已加载: {class_name}")

    async def execute_on_message(self, message):
        tasks = []
        # 遍历已加载的插件，调用各自的 on_message 方法
        for class_name, plugin_instance in self.loaded_plugins.items():
            if hasattr(plugin_instance, 'on_message'):
                tasks.append(plugin_instance.on_message(message, self))
        
        # 执行所有插件的消息处理
        await asyncio.gather(*tasks)

    async def websocket_server(self):
        logger.info("消息接收服务器启动中...")
        logger.info(f"尝试连接到 WebSocket 地址: {self.ws_url}\n")
        try:
            # 建立WebSocket连接
            async with websockets.connect(self.ws_url, extra_headers={"Authorization": f"Bearer {self.token}"}) as websocket:
                logger.info(f"成功连接到 OneBot WebSocket 地址: {self.ws_url}\n")
                logger.info("开始接收消息\n")
                
                # 加载插件
                await self.load_plugins_from_folder("plugins")
                
                # 持续接收消息
                while True:
                    message = await websocket.recv()
                    logger.debug(f"收到 WebSocket 消息原文: {message}")
                    
                    try:
                        # 解析收到的消息
                        data = json.loads(message)
                        if data['post_type'] == 'meta_event':
                            # 处理生命周期元事件
                            if data['meta_event_type'] == 'lifecycle':
                                logger.info('接收到生命周期元事件包')
                                continue
                            if data['meta_event_type'] == 'heartbeat':
                                logger.info('接收到心跳包,看来LXBot还活着呢。')
                                continue
                        
                        # 处理插件消息
                        await self.execute_on_message(data)
                    except json.JSONDecodeError:
                        logger.error("无法解析 WebSocket 消息的 JSON 数据")
                    except Exception as e:
                        logger.error(f"处理 WebSocket 消息时出错: {e}")

        except Exception as e:
            logger.error(f"WebSocket 连接失败: {e}, 10秒后重连")
            await asyncio.sleep(10)  # 等待10秒后重连
            await self.websocket_server()  # 重新启动WebSocket服务器
