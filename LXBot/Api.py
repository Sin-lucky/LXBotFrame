import requests
import logging

logger = logging.getLogger("api")

def call_api(base_url, action, params, token=None):
    """
    万用Api调用函数，只要LLOB支持就可以用
    base_url: Bot API地址
    action: API动作
    params: 请求参数
    token: Bot Token
    返回值：{message_id}
    """
    # 设置请求头
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    # 构造请求 URL
    url = f"{base_url}/{action}"
    # 构造请求参数
    
    try:
        # 发送 HTTP POST 请求
        response = requests.post(url, params=params, headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                logger.info(f"成功执行操作{action}")
                return data.get("data")
            else:
                logger.error(f"API返回错误:{data.get('msg')}")
        else:
            logger.error(f"请求失败，状态码:{response.status_code}")
    except requests.RequestException as e:
        logger.error(f"请求过程中发生错误:{e}")
    
    return None