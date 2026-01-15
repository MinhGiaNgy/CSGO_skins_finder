import requests
import sqlite3
import fastapi
import uvicorn
import time

app = fastapi.FastAPI()

con = sqlite3.connect("steamskinsdata.db")
command = """CREATE TABLE IF NOT EXISTS Skins(name TEXT, sell_price REAL, sell_listings INTEGER)"""
cur = con.cursor()
cur.execute(command)
from dataclasses import dataclass
from typing import Callable
from pydantic import BaseModel, PositiveInt


class Skin(BaseModel):
    name: str
    sell_price: int
    sell_listings: int


def get_skins_from_steam():
    apiskinlist: list[Skin] = []
    query = {
        "search_descriptions": 0,
        "sort_column": "default",
        "appid": 730,
        "sort_dir": "desc",
        "norender": 1,
        "count": 100,
    }
    start = 0
    while True:
        if start > 20600:
            break
        
        print(f"Requesting at page{start}")
        query["start"] = start
        response = requests.request(
            method="GET",
            url="https://steamcommunity.com/market/search/render/",
            params=query,
        )
        content = response.json()
        if content is None:
            print(f"Retrying at page{start}...")
            time.sleep(20)
            continue
        results = content["results"]
        if len(results) == 0:
            if start < 20600:
                print(f"Retrying at page{start}...")
                continue
            
            
            else:
                break

        for result in results:
            skin = Skin(**result)
            apiskinlist.append(skin)
        start += 100
        

    return apiskinlist


@app.post("/skinsync")
def sync_skin_data():
    con = sqlite3.connect("steamskinsdata.db")
    cur = con.cursor()
    skinslist = get_skins_from_steam()
    # print(skinslist)
    command = """DELETE FROM skins"""
    cur.execute(command)
    print("Refreshed")

    for skin_obj in skinslist:
        name = skin_obj.name
        sell_price = skin_obj.sell_price
        sell_listings = skin_obj.sell_listings
        command = f"""INSERT INTO skins (name, sell_price, sell_listings)
        VALUES ("{name}", {sell_price}, {sell_listings})"""
        cur.execute(command)
    con.commit()


# command = """
# DELETE FROM skins
# WHERE skin 1"""
# cur.execute(command)
command = """
SELECT
 name, sell_price, sell_listings
From
 skins
"""
skinslist = cur.execute(command).fetchall()
print(skinslist)
# with con:
#   cur.execute(command)
# cur.execute(command)
if __name__ == "__main__":
    uvicorn.run("database:app", reload=True) 
