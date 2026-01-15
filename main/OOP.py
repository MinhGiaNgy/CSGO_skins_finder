import fastapi
import random
import uvicorn
import requests
import time


# class Person:
#     def __init__(self, id: str,name:str):
#      self.id = id
#      self.name = name
#     def walking(self):
#        print(f"My ID is {self.id}")
#        print("I am walking ere")

# p1 = Person(id = "123", name = "bruh")
# print(p1.id)
# print(p1.name)
# p1.walking

from dataclasses import dataclass

# @dataclass
# class CPU:
#    name: str
#    brand: str
#    release_year: int

#    def info(self):
#       print(self.name)
#       print(self.brand)
#       print(self.release_year)


# C1 = CPU(name="R7", brand="Ryzen", release_year=2020)
# C2 = CPU(name="R5", brand="Ryzen", release_year=2019)
# C3 = CPU(name="I7", brand="Intel", release_year=2017)

# C1.info()
from typing import Callable

# from dataclasses import dataclass
# def callbackfunc():
#     print("i am a callback func")
# # higher order func
# def higher_order_func(func: Callable):
#     print("i am higher order func")
#     return func
# fn = higher_order_func(callbackfunc)
# fn()
from pydantic import BaseModel, PositiveInt


# class PP(BaseModel):
#    id: int
#    signup_ts: str
#    bruh: dict[str, PositiveInt]
# external_data = {
#    "id": 123,
#    "signup_ts": "2019-06-01",
#    "bruh": {
#       "wines": 1
#    }
# }
# PP1 = PP(**external_data)
# print(PP1.id)
# print(PP1)









class Skin(BaseModel):
    name: str
    sell_price: int
    sell_listings: int


def get_skins_from_steam():
    response = requests.request(
        method="GET",
        url="https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=50000",
    )
    content = response.json()
    results = content["results"]
    skinz: list[Skin] = []
    for result in results:
        skin = Skin(**result)
        skinz.append(skin)
    return skinz


skinz = get_skins_from_steam()
# print(skinz)

def find_skin_by_name(name: str, is_stattrak: bool ):
    search_results = []
    name = name.strip()
    for skin in skinz: 
        if name.lower() in skin.name.lower():
           
            if is_stattrak and "StatTrak" in skin.name:
                search_results.append(skin)
            elif not is_stattrak and "StatTrak" not in skin.name:
                search_results.append(skin)

    return search_results

# name = str(input("Enter skin name"))
# s = find_skin_by_name(name, is_stattrak = True)
# print(f"result is{s}")
# fix stat trak identifier



        
        



# make a converter for sell_price
# external_data = {
#     "name": (Sskins(**skinz)),

#     "sell_listings": (Sskins.sell_listings),
#     "sell_price": (Sskins.sell_price),
# }
# skin = Sskins(**external_data)
# print(skin.name)
# print(skin.sell_price)
# print(skin.sell_listings)


# def moneyexchanger(rate: float):
#     response = requests.request(
#         method="get",
#         url="https://api.exchangerate-api.com/v4/latest/USD"
#     )
#     content2 = response.json()
#     rates = content2[""]
# FIND A RELIABLE CURRENCY EXCHANGE API
