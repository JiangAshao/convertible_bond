#!/usr/bin/env python3
# encoding: utf-8

import requests

sendkeys = []

def wx_send(title=' ', content=' ', uid=''):
    for __SendKey in sendkeys:
        requests.get(
            "https://sctapi.ftqq.com/"+__SendKey+".send",
            params={"title": title, 'desp': content, 'openid': uid})


if __name__ == '__main__':
    wx_send(title='打新债',
            content='\n今日新债为【xx新债】')