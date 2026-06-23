from fastapi import APIRouter, FastAPI
from api.v1 import route_user, route_blog

routers = APIRouter()
routers.include_router(route_user.router, prefix='/user', tags=["users"])
routers.include_router(route_blog.router, prefix='/blog', tags=["blogs"])