import fastapi

first_api = fastapi.FastAPI()

@first_api.get("/")
def get_information():
    return {"name":"first-api","i change my mind":"change my mind againnnnnn"}

print(__name__)