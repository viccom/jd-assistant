#!/usr/bin/python
# -*- coding: UTF-8 -*-

from jd_assistant import Assistant
from dateutil.parser import parse
import time

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """
    # 商品id 飞天茅台53：100012043978;
    # 小米路由AX3600：100011385902;
    # 惠寻一次性医用口罩: 66235396248;
    # 3Q一次性医用外科口罩: 100011551632;
    # 袋鼠医生（DR.ROOS）医用外科口罩: 100006394713;
    sku_ids = '100012043978'
    area = '1_2801_54769'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.make_reserve(sku_ids)
