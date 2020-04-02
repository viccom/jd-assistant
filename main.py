#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
from dateutil.parser import parse
import time

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    buy_count = 1
    expected_time = '2020-04-02 09:59:59.750'
    expected_buy_time = '2020-04-02 09:59:59.900'
    expected_timestamp = parse(expected_time).timestamp()
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
    while True:
        print(time.time() > expected_timestamp)
        if time.time() > expected_timestamp:
            print("start buy maotai !!!", buy_count)
            asst.exec_reserve_seckill_by_time(sku_ids, expected_buy_time, retry=3, interval=5, num=2)
            buy_count = buy_count + 1
        time.sleep(100)

    # asst.add_item_to_cart(sku_ids=sku_ids)  # 根据商品id添加购物车（可选）
    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)
    # asst.submit_order_by_time(buy_time='2020-04-02 09:59:59.750', retry=4, interval=2)  # 定时提交订单
    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单

    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
