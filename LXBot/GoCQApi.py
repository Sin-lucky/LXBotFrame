import requests
import logging

#Api操作模块尚未完工，LLOB支持的一部分Api应用面较小

logger = logging.getLogger("api")

def send_private_forward_msg(base_url, user_id, messages, token=None):
    """
    发送合并转发
    base_url: Bot API地址
    user_id: 接收者QQ号
    message: 要发送的消息
    token: Bot Token
    返回值：{message_id,forward_id}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/send_private_forward_msg"
    # 构造请求参数
    params = {"user_id": user_id, "message": messages}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"成功发送合并转发消息:{messages}到{user_id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def send_group_forward_msg(base_url, group_id, messages, token=None):
    """
    发送合并转发
    base_url: Bot API地址
    group_id: 接收者QQ群号
    message: 要发送的消息
    token: Bot Token
    返回值：{message_id,forward_id}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/send_group_forward_msg"
    # 构造请求参数
    params = {"group_id": group_id, "message": messages}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"成功发送合并转发消息:{messages}到{group_id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_group_msg_history(base_url, message_seq, group_id, token=None):
    """
    获取群消息历史记录
    base_url: Bot API地址
    message_seq: 消息序列号
    group_id: 群号
    token: Bot Token
    返回值：{messages:[{content,sender:{nickname,user_id},time}, ...]}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_group_msg_history"
    # 构造请求参数
    params = {"message_seq": message_seq, "group_id": group_id}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"成功获取群{group_id}消息历史记录")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

