#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: tls.py
@time: 2020-10-28 14:45
"""

__mtime__ = '2020-10-28'

import requests

# curl
# 'https://10.117.32.176:56001/query'
# -H
# 'Content-Type:application/json; charset=utf-8'
# -H
# 'Connection:close'
# -H
# 'Authorization:oakROLK6HwOOAt8AabcGCfZMyx/jfuuAE4Zjy62oFPguHG/LR89176Oz9OA9Cj+C6SJHqzX+4Sr6Hbf1K4e+DVee8XW8Y7dXUPvyNNNFekkfLktLdmUIXHjaXhixI2eo'
if __name__ == '__main__':
    headers = {
        "Authorization": "oakROLK6HwOOAt8AabcGCfZMyx/jfuuAE4Zjy62oFPguHG/LR89176Oz9OA9Cj+C6SJHqzX+4Sr6Hbf1K4e+DVee8XW8Y7dXUPvyNNNFekkfLktLdmUIXHjaXhixI2eo",
        "Content-Type": "application/json; charset=utf-8",
        "Connection": "close"
    }
    resp = requests.get("https://10.117.32.176:56001/query", verify="/etc/bitfusion/tls/ca.crt", headers=headers)
    print(resp.status_code)
    print(resp.json())
