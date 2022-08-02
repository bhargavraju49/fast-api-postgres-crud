from fastapi import FastAPI
from routes.api.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/", tags=["Root"])
async def root():
    return {"home check"}


app.include_router(api_router)
