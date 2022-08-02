from fastapi import APIRouter
from routes.api.v1.endpoints import crud

api_router = APIRouter()

api_router.include_router(crud.db_crud_router, prefix="/db", tags=["database"])
