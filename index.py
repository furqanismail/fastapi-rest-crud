from fastapi import FastAPI
from routes.index import blog
app = FastAPI()

app.include_router(blog)

