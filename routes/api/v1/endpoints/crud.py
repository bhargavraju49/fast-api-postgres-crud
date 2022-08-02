from fastapi import BackgroundTasks, APIRouter, UploadFile, HTTPException, responses, Depends, FastAPI, HTTPException
from config.postgres import SessionLocal, engine
from models import person_table
from sqlalchemy.orm import Session

db_crud_router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@db_crud_router.post("/add-row")
async def add():
    return {"add check"}

@db_crud_router.post("/update-row")
async def update():
    return {"update check"}


@db_crud_router.delete("/delete-row")
async def delete():
    return {"delete check"}


@db_crud_router.get("/getdata")
def getdata(db: Session = Depends(get_db)):

    records = db.query(person_table.Person).all()
    return records



    
