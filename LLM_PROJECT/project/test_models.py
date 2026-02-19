from google import genai

client = genai.Client(api_key="AIzaSyBfuF5w6ryAK4UmkNmzDanNlvx2GPJX0a4")

for model in client.models.list():
    print(model.name)
