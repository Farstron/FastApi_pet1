from typing import Annotated
from fastapi import APIRouter,Depends
from repository import TaskRpository
from schemas import STask, STaskAdd, STaskID

task_router = APIRouter(prefix = "/tasks",tags = ["Задачи"])


@task_router.post("")
async def add_task(task: Annotated[STaskAdd,Depends()]) -> STaskID:
    task_id = await TaskRpository.add_one(task)
    return {"ok": True, "task_id": task_id}

@task_router.get("")
async def get_tasks() -> list[STask]:
    task_models = await TaskRpository.get_all()
    return task_models