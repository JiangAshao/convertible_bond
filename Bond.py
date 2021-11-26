#!/usr/bin/env python3
# encoding: utf-8
import datetime


class Bond:
    _name = ""  # 债券简称
    _code = ""  # 债券代码
    _public_start_date = None  # 申购日期
    _listing_date = None       # 上市日期
    _convert_stock_price = None  # 正股价
    _swap_price = None         # 转股价

    def __init__(self, name, code, price, swap_price, public_start_date, listing_date):
        self._name = name
        self._code = code
        if price is not None and price != "-":
            self._price = float(price)
        else:
            self._price = None
        if swap_price is not None and swap_price != "-":
            self._swap_price = float(swap_price)
        if public_start_date is not None:
            self._public_start_date = datetime.datetime.strptime(
                public_start_date, "%Y-%m-%d %H:%M:%S").date()
        if listing_date is not None:
            self._listing_date = datetime.datetime.strptime(
                listing_date, "%Y-%m-%d %H:%M:%S").date()

    """
    转股价值
    """
    @property
    def swap_value(self) -> float:
        if self._swap_price is not None and self._price is not None:
            if self._swap_price > 0 and self._price > 0:
                return self._price / self._swap_price * 100
        return None

    """
    正股价
    """
    @property
    def price(self) -> float:
        if self._price is not None and self._price > 0:
            return self._price
        return None

    """
    转股价
    """
    @property
    def swap_price(self) -> float:
        if self._swap_price is not None and self._swap_price > 0:
            return self._swap_price
        return None

    """
    债券代码
    """
    @property
    def code(self) -> str:
        return self._code

    """
    债券简称
    """
    @property
    def name(self) -> str:
        return self._name

    """
    申购日期
    """
    @property
    def public_start_date(self):
        return self._public_start_date

    """
    上市日期
    """
    @property
    def listing_date(self):
        return self._listing_date