import requests
import logging

logger = logging.getLogger("api")

def send_private_msg(base_url, user_id, message, auto_escape=False, token=None):
    """
    发送私聊消息
    base_url: Bot API地址
    user_id: 接收者QQ号
    message: 要发送的消息
    auto_escape：是否解析CQ码
    token: Bot Token
    返回值：{message_id}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/send_private_msg"
    # 构造请求参数
    params = {"user_id": user_id, "message": message, "auto_escape": auto_escape}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"成功发送私聊消息:{message}到{user_id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def send_group_msg(base_url, group_id, message, auto_escape=False, token=None):
    """
    发送群消息
    base_url: Bot API地址
    group_id: 群号
    message: 要发送的消息
    auto_escape：是否解析CQ码
    token: Bot Token
    返回值：{message_id}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/send_group_msg"
    # 构造请求参数
    params = {"group_id": group_id, "message": message, "auto_escape": auto_escape}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"成功发送群消息:{message}到群{group_id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def send_msg(base_url, message_type, user_id=None, group_id=None, message=None, auto_escape=False, token=None):
    """
    发送消息
    base_url: Bot API地址
    message_type: 消息类型，private或group
    user_id: 接收者QQ号，当message_type为private时必填
    group_id: 群号，当message_type为group时必填
    message: 要发送的消息
    auto_escape：是否解析CQ码
    token: Bot Token
    返回值：{message_id}
    """
    # 检查消息类型是否有效
    if message_type not in ["private", "group"]:
        logger.error(f"消息类型错误:{message_type}")
        return None
    
    # 如果消息类型是私聊，则检查用户ID是否提供
    if message_type == "private" and not user_id:
        logger.error(f"user_id为空")
        return None
    
    # 如果消息类型是群聊，则检查群组ID是否提供
    if message_type == "group" and not group_id:
        logger.error(f"group_id为空")
        return None

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/send_msg"
    # 构造请求参数
    params = {"message_type": message_type, "user_id": user_id, "group_id": group_id, "message": message, "auto_escape": auto_escape}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"成功发送消息:{message}到{group_id or user_id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def delete_msg(base_url, message_id, token=None):
    """
    撤回消息
    base_url: Bot API地址
    message_id: 消息ID
    token: Bot Token
    返回值：{}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/delete_msg"
    # 构造请求参数
    params = {"message_id": message_id}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"撤回消息成功:{message_id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_msg(base_url, message_id, token=None):
    """
    获取消息
    base_url: Bot API地址
    message_id: 消息ID
    token: Bot Token
    返回值：{time, message_type, message_id, real_id, sender: {user_id, nickname, sex, age}, message}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_msg"
    # 构造请求参数
    params = {"message_id": message_id}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取消息成功:{message_id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_forward_msg(base_url, id, token=None):
    """
    获取合并转发内容
    base_url: Bot API地址
    id: 合并转发ID
    token: Bot Token
    返回值：
    {messages: [{type, data: {}}, ...]}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_forward_msg"
    # 构造请求参数
    params = {"id": id}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取合并转发内容成功:{id}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def send_like(base_url, user_id, times=1, token=None):
    """
    给好友资料卡点赞
    base_url: Bot API地址
    user_id: 好友QQ号
    times: 点赞次数
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/send_like"
    # 构造请求参数
    params = {"user_id": user_id, "times": times}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"给{user_id}点赞{times}次成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_kick(base_url, group_id, user_id, reject_add_request=False, token=None):
    """
    群组踢人
    base_url: Bot API地址
    group_id: 群号
    user_id: 被踢者QQ号
    reject_add_request: 是否拒绝被踢者的加群请求
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_kick"
    # 构造请求参数
    params = {"group_id": group_id, "user_id": user_id, "reject_add_request": reject_add_request}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}踢出{user_id}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_ban(base_url, group_id, user_id, duration=30*60, token=None):
    """
    群组单人禁言
    base_url: Bot API地址
    group_id: 群号
    user_id: 被禁言者QQ号
    duration: 禁言时长，单位秒，0表示取消禁言
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_ban"
    # 构造请求参数
    params = {"group_id": group_id, "user_id": user_id, "duration": duration}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}禁言{user_id}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_anonymous_ban(base_url, group_id, anonymous_flag, duration=30*60, token=None):
    """
    群组匿名用户禁言
    TIPS: LLOB并不支持该功能
    base_url: Bot API地址
    group_id: 群号
    anonymous_flag: 匿名用户的flag，在调用获取群成员信息时获得
    duration: 禁言时长，单位秒，0表示取消禁言
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_anonymous_ban"
    # 构造请求参数
    params = {"group_id": group_id, "flag": anonymous_flag, "duration": duration}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200: 
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}匿名用户{anonymous_flag}禁言成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_whole_ban(base_url, group_id, enable=True, token=None):
    """
    群组全员禁言
    base_url: Bot API地址
    group_id: 群号
    enable: 是否开启全员禁言，True为开启，False为关闭
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_whole_ban"
    # 构造请求参数
    params = {"group_id": group_id, "enable": enable}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}全员禁言{enable}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_admin(base_url, group_id, user_id, enable=True, token=None):
    """
    设置群组管理员
    base_url: Bot API地址
    group_id: 群号
    user_id: 被设置管理员的QQ号
    enable: 是否设置为管理员，True为设置，False为取消
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_admin"
    # 构造请求参数
    params = {"group_id": group_id, "user_id": user_id, "enable": enable}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}设置{user_id}为管理员{enable}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_anonymous(base_url, group_id, enable=True, token=None):
    """
    设置群组匿名
    TIPS: LLOB并不支持该功能
    base_url: Bot API地址
    group_id: 群号
    enable: 是否允许匿名聊天，True为允许，False为禁止
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_anonymous"
    # 构造请求参数
    params = {"group_id": group_id, "enable": enable}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}允许匿名{enable}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_card(base_url, group_id, user_id, card=None, token=None):
    """
    设置群组名片
    base_url: Bot API地址
    group_id: 群号
    user_id: 被设置名片的QQ号
    card: 群名片内容，不填或为空字符串表示删除名片
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_card"
    # 构造请求参数
    params = {"group_id": group_id, "user_id": user_id, "card": card}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}设置{user_id}的群名片成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_name(base_url, group_id, group_name, token=None):
    """
    设置群组名称
    base_url: Bot API地址
    group_id: 群号
    group_name: 新的群名称
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_name"
    # 构造请求参数
    params = {"group_id": group_id, "group_name": group_name}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}设置名称{group_name}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_leave(base_url, group_id, is_dismiss=False, token=None):
    """
    退出群组
    base_url: Bot API地址
    group_id: 群号
    is_dismiss: 是否解散，如果登录号是群主，则仅在此项为 True 时能够解散
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_leave"
    # 构造请求参数
    params = {"group_id": group_id, "is_dismiss": is_dismiss}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}退出成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_group_special_title(base_url, group_id, user_id, special_title, duration=-1, token=None):
    """
    设置群组专属头衔
    base_url: Bot API地址
    group_id: 群号
    user_id: 被设置头衔的QQ号
    special_title: 专属头衔，不填或为空字符串表示删除头衔
    duration: 专属头衔有效期，单位秒，-1表示永久，不填或为0表示取消头衔
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_special_title"
    # 构造请求参数
    params = {"group_id": group_id, "user_id": user_id, "special_title": special_title, "duration": duration}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"群{group_id}设置{user_id}的专属头衔为\"{special_title}\"成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def set_friend_add_request(base_url, flag, approve=True, reason="", token=None):
    """
    处理加好友请求
    base_url: Bot API地址
    flag: 加好友请求的 flag
    approve: 是否同意请求，True 为同意，False 为拒绝
    reason: 处理理由，仅在拒绝时有效
    token: Bot Token
    返回值：{}
    """

    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_friend_add_request"
    # 构造请求参数
    params = {"flag": flag, "approve": approve, "reason": reason}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"处理好友请求{flag}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None
def set_group_add_request(base_url, flag, sub_type, approve=True, reason="", token=None):
    """
    处理加群请求/邀请
    base_url: Bot API地址
    flag: 加群请求的 flag
    sub_type: 请求类型，"add" 或 "invite"
    approve: 是否同意请求，True 为同意，False 为拒绝
    reason: 处理理由，仅在拒绝时有效
    token: Bot Token
    返回值：{}
    """
    # 检查请求类型
    if sub_type not in ["add", "invite"]:
        logger.error(f"请求类型{sub_type}错误，请使用\"add\"或\"invite\"")
        return None
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_group_add_request"
    # 构造请求参数
    params = {"flag": flag, "sub_type": sub_type, "approve": approve, "reason": reason}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"处理加群请求{flag}成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_login_info(base_url, token=None):
    """
    获取登录信息
    base_url: Bot API地址
    token: Bot Token
    返回值：{user_id, nickname}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_login_info"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取登录信息成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_stranger_info(base_url, user_id, no_cache=False, token=None):
    """
    获取陌生人信息
    base_url: Bot API地址
    user_id: QQ号
    no_cache: 是否使用缓存，False 为使用缓存，True 为不使用缓存
    token: Bot Token
    返回值：{user_id, nickname, sex, age}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_stranger_info"
    # 构造请求参数
    params = {"user_id": user_id, "no_cache": no_cache}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取陌生人{user_id}信息成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_friend_list(base_url, token=None):
    """
    获取好友列表
    base_url: Bot API地址
    token: Bot Token
    返回值：[{user_id, nickname, remark}, ...]
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_friend_list"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取好友列表成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_group_info(base_url, group_id, no_cache=False, token=None):
    """
    获取群信息
    base_url: Bot API地址
    group_id: 群号
    no_cache: 是否使用缓存，False 为使用缓存，True 为不使用缓存
    token: Bot Token
    返回值：{group_id, group_name, member_count, max_member_count}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_group_info"
    # 构造请求参数
    params = {"group_id": group_id, "no_cache": no_cache}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取群{group_id}信息成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_group_list(base_url, token=None):
    """
    获取群列表
    base_url: Bot API地址
    token: Bot Token
    返回值：[{group_id, group_name, member_count, max_member_count}, ...]
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_group_list"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取群列表成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_group_member_info(base_url, group_id, user_id, no_cache=False, token=None):
    """
    获取群成员信息
    base_url: Bot API地址
    group_id: 群号
    user_id: QQ号
    no_cache: 是否使用缓存，False 为使用缓存，True 为不使用缓存
    token: Bot Token
    返回值：{group_id, user_id, nickname, card, sex, age, area, join_time, last_sent_time, level, role, unfriendly, title ,title_expire_time, card_changeable}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_group_member_info"
    # 构造请求参数
    params = {"group_id": group_id, "user_id": user_id, "no_cache": no_cache}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取群{group_id}成员{user_id}信息成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_group_member_list(base_url, group_id, token=None):
    """
    获取群成员列表
    base_url: Bot API地址
    group_id: 群号
    token: Bot Token
    返回值：[{user_id, nickname, card, sex, age, area, join_time, last_sent_time, level, role, unfriendly, title ,title_expire_time, card_changeable}, ...]
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_group_member_list"
    # 构造请求参数
    params = {"group_id": group_id}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取群{group_id}成员列表成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None

def get_group_honor_info(base_url, group_id, type, token=None):
    """
    获取群荣誉信息
    base_url: Bot API地址
    group_id: 群号
    type: 类型，[talkative,performer,legend,strong_newbie,emotion,all]
    token: Bot Token
    返回值：{group_id, current_talkative: {user_id, nickname, avatar, day_count}, talkative_list: [{user_id, nickname, avatar, description}, ...], performer_list: [{user_id, nickname, avatar, description}, ...], legend_list: [{user_id, nickname, avatar, description}, ...], strong_newbie_list: [{user_id, nickname, avatar, description}, ...], emotion_list: [{user_id, nickname, avatar, description}, ...]}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL    
    url = f"{base_url}/get_group_honor_info"
    # 构造请求参数
    params = {"group_id": group_id, "type": type}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取群{group_id}荣誉信息成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def get_cookies(base_url, domain, token=None):
    """
    获取Cookies
    base_url: Bot API地址
    domain: 域名
    token: Bot Token
    返回值：Cookies
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_cookies"
    # 构造请求参数
    params = {"domain": domain}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取Cookies成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def get_csrf_token(base_url, token=None):
    """
    获取CSRF Token
    TIPS: LLOB并不支持该功能
    base_url: Bot API地址
    token: Bot Token
    返回值：CSRF Token
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_csrf_token"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取CSRF Token成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def get_credentials(base_url, token=None):
    """
    获取 QQ 相关接口凭证
    TIPS: LLOB并不支持该功能
    base_url: Bot API地址
    token: Bot Token
    返回值：{cookies, csrf_token}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_credentials"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取凭证成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def get_record(base_url, file, out_format, token=None):
    """
    获取语音消息    
    base_url: Bot API地址
    file: 语音文件名
    out_format: 语音格式
    token: Bot Token
    返回值：{file}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_record"
    # 构造请求参数
    params = {"file": file, "out_format": out_format}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取语音消息成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def get_image(base_url, file, token=None):
    """
    获取图片    
    base_url: Bot API地址
    file: 图片文件名
    token: Bot Token
    返回值：{file}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_image"
    # 构造请求参数
    params = {"file": file}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取图片成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def can_send_image(base_url, token=None):
    """
    检查机器人是否可以发送图片
    base_url: Bot API地址
    token: Bot Token
    返回值：{yes}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/can_send_image"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def can_send_record(base_url, token=None):
    """
    检查机器人是否可以发送语音
    base_url: Bot API地址
    token: Bot Token
    返回值：{yes}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/can_send_record"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def get_status(base_url, token=None):
    """
    获取插件运行状态
    base_url: Bot API地址
    token: Bot Token
    返回值：{online, good,...}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_status"
    # 构造请求参数
    params = {}
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取插件运行状态成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def get_version_info(base_url, token=None):
    """
    获取版本信息
    base_url: Bot API地址
    token: Bot Token
    返回值：{app_name, app_version, protocol_version,...}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/get_version_info"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"获取版本信息成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def set_restart(base_url, delay, token=None):
    """
    重启API
    base_url: Bot API地址
    token: Bot Token
    返回值：{}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/set_restart"
    # 构造请求参数
    params = {"delay": delay}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"重启API成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

def clean_cache(base_url, token=None):
    """
    清理缓存
    base_url: Bot API地址
    token: Bot Token
    返回值：{}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/clean_cache"
    # 构造请求参数
    params = {}
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"清理缓存成功")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None 

