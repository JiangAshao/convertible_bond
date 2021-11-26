#!/usr/bin/env python3
# encoding: utf-8

import wx_send
import requests
import json
import datetime
import Bond

PAGE_URL = "http://data.eastmoney.com/kzz/default.html"
TARGET_URL = "http://datacenter-web.eastmoney.com/api/data/v1/get"
PARAMS = {
    'reportName': "RPT_BOND_CB_LIST",
    'columns': "ALL",
    'quoteColumns': "f2~01~CONVERT_STOCK_CODE~CONVERT_STOCK_PRICE,f235~10~SECURITY_CODE~TRANSFER_PRICE,f236~10~SECURITY_CODE~TRANSFER_VALUE,f2~10~SECURITY_CODE~CURRENT_BOND_PRICE,f237~10~SECURITY_CODE~TRANSFER_PREMIUM_RATIO,f239~10~SECURITY_CODE~RESALE_TRIG_PRICE,f240~10~SECURITY_CODE~REDEEM_TRIG_PRICE,f23~01~CONVERT_STOCK_CODE~PBV_RATIO",
    'source': "WEB",
    'client': "WEB",
    'sortTypes': -1,
    'sortColumns': "PUBLIC_START_DATE",
    'pageSize': 20,
    'pageNumber': 1
}


def log(string):
    for line in string.splitlines():
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = "[%s] %s" % (now, line)
        print(line)


def main():
    req = requests.get(TARGET_URL, params=PARAMS)
    js = json.loads(req.text)
    data = js["result"]["data"]
    recently_public_bonds = []
    recently_listing_bonds = []
    today = datetime.date.today()
    # today = datetime.datetime.strptime("2021-11-24 10:00:13", '%Y-%m-%d %H:%M:%S').date()
    dayRel = ["今天"]
    for item in data:
        if item['PUBLIC_START_DATE'] is not None:
            start_date = datetime.datetime.strptime(
                item['PUBLIC_START_DATE'], '%Y-%m-%d %H:%M:%S').date()
            gap = (start_date - today).days
            if gap >= 0 and gap < 1:
                recently_public_bonds.append(
                    Bond.Bond(item["SECURITY_NAME_ABBR"], item["SECURITY_CODE"], item["CONVERT_STOCK_PRICE"], item["TRANSFER_PRICE"], item['PUBLIC_START_DATE'], item['LISTING_DATE']))
        elif item['VALUE_DATE'] is not None:
            start_date = datetime.datetime.strptime(
                item['VALUE_DATE'], '%Y-%m-%d %H:%M:%S').date()
            gap = (start_date - today).days
            if gap == 0:
                recently_public_bonds.append(
                    Bond.Bond(item["SECURITY_NAME_ABBR"], item["SECURITY_CODE"], item["CONVERT_STOCK_PRICE"], item["TRANSFER_PRICE"], item['VALUE_DATE'], item['LISTING_DATE']))
        if item['LISTING_DATE'] is not None:
            list_date = datetime.datetime.strptime(
                item['LISTING_DATE'], '%Y-%m-%d %H:%M:%S').date()
            gap = (list_date - today).days
            if gap == 0:
                recently_listing_bonds.append(
                    Bond.Bond(item["SECURITY_NAME_ABBR"], item["SECURITY_CODE"], item["CONVERT_STOCK_PRICE"], item["TRANSFER_PRICE"], item['PUBLIC_START_DATE'], item['LISTING_DATE']))

    wx_msg = '\n'
    wx_msg += '近日发售：\n\n'
    if len(recently_public_bonds) > 0:
        for bond in recently_public_bonds:
            if bond.public_start_date is not None:
                gap = (bond.public_start_date - today).days
                if gap < len(dayRel):
                    wx_msg += '- %s' % (dayRel[gap])
                    wx_msg += '- %s: 债券代码：%s，债券简称：%s，正股价：%s，转股价：%s, 转股价值：%.2f' % (
                        dayRel[gap],
                        bond.code,
                        bond.name,
                        bond.price if bond.price is not None else "-",
                        bond.swap_price if bond.swap_price is not None else "-",
                        bond.swap_value if bond.swap_price is not None else 0.0)
                if bond.swap_price is not None and bond.swap_value > 90:
                    wx_msg += '  推荐✅'
            else:
                wx_send.wx_send(
                    title='每日可转债', content="bond.public_start_date 不应该为空，请检查代码或API")
                raise RuntimeError("bond.public_start_date 不应该为空，请检查代码或API")
            wx_msg += '\n\n'
    else:
        wx_msg += '- 无\n\n'

    wx_msg += '近日上市：\n\n'
    if len(recently_listing_bonds) > 0:
        for bond in recently_listing_bonds:
            gap = (bond.listing_date - today).days
            if gap < len(dayRel):
                wx_msg += '- %s: 债券代码：% s，债券简称：% s\n\n' % (
                    dayRel[gap], bond.code, bond.name)
    else:
        wx_msg += '- 无\n\n'

    if len(recently_public_bonds) > 0 or len(recently_listing_bonds) > 0:
        wx_msg += '[点击详情查看一览表](%s)' % PAGE_URL
        log(wx_msg)
        wx_send.wx_send(title='每日可转债', content=wx_msg)
    else:
        log("今日无可转债发行或上市")


if __name__ == "__main__":
    main()
