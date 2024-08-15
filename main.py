import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import *
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('database cleared')
    await create_tables()
    print('database created')
    yield
    print('turn off')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
