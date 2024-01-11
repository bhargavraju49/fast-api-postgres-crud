from fastapi import APIRouter
from routes.api.v1.endpoints import crud
from routes.api.v1.endpoints import textmoduleapis

api_router = APIRouter()

api_router.include_router(crud.db_crud_router, prefix="/db", tags=["database"])
api_router.include_router(textmoduleapis.tm_router, prefix="/tm", tags=["text-module"])
