from fastapi import FastAPI, routing
from core.config import settings
from db.base_class import Base
from db.session import engine, get_db
# Improting the models is necessary to create the table
# Without models importing the main.py won't have any reference to models
from db.models import user, blog
from api import route_base

def create_routings(app):
    app.include_router(route_base.routers)

def create_table():
    Base.metadata.create_all(engine)

def start_app():
    # APP instance for fastapi
    # All the routes will use app for get post delete
    create_table()
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_routings(app)
    return app

app = start_app()

