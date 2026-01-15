# import fastapi
# import math
# import random
# app = fastapi.FastAPI()
# @app.get("/randomed")
# def randomed():
# lmao = random.randint(1,4)
# buh = {"numbers":
#    lmao
# }
# return
# counter = 0
# @app.post("/")
# def countered():
# global counter
# counter = counter + 1
# views = {"visitors": counter

# }
# return views

# app.get("/")(bruh)

# import requests
# import fastapi
# import uvicorn
# app = fastapi.FastAPI()
# response = requests.request(
#     method="GET", url="https://www.beanpoems.com/api/poems/random"
# )

# content1 = response.json()
# poems = (content1["body"])
# print(poems)
# counter = 0


# @app.get("/")
# def visits():
#     global counter
#     counter = counter + 1
#     views = {"visitors": counter}
#     return views
# @app.post("/")
# def poetry():
#     response = requests.request(
#     method="GET", url="https://www.beanpoems.com/api/poems/random/")
#     content2 = response.json()
#     poems = (content2["body"])
#     return poems


# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)

# import fastapi
# import random
# import uvicorn
# import requests

# app = fastapi.FastAPI()


# @app.get("/poemss/{id}")
# def poems(id: int):
#     for poem in poemss:
#         print(poem)
#         if poem["id"] == id:
#             return poem


# poemss = [
#     {"id": 1},
#     {"id": 2},
#     {"id": 3},
#     {"id": 4},
# ]
# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
