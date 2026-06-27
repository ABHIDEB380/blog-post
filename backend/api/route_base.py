from fastapi import APIRouter
from api.v1 import route_user, route_blog, route_login

routers = APIRouter()
routers.include_router(route_user.router, prefix='/user', tags=["users"])
routers.include_router(route_blog.router, prefix='/blog', tags=["blogs"])
routers.include_router(route_login.router, prefix='', tags=["login"])