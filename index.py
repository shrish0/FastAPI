from fastapi import FastAPI
from routes.route import user
app=FastAPI()

app.include_router(user)

print('''http://127.0.0.1:8000/docs''')