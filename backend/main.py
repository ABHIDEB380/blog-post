from fastapi import FastAPI
from core.config import settings

# APP instance for fastapi
# All the routes will use app for get post delete
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get('/')
def hello():
    return {'msg': 'hello world'}