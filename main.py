from database import create_tables, delete_tables
from fastapi import FastAPI # type: ignore
import uvicorn
from contextlib import asynccontextmanager
from router import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)