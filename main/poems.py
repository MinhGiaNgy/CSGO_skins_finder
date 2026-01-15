import requests
import fastapi

response = requests.request(
    method="GET",
    url = "https://www.beanpoems.com/api/poems/random"
)
app = fastapi.FastAPI()
counter = 0
@app.post("/")
def poetry():
    global counter
    counter = counter + 1
    views = {"visitors": counter

    }
    return views