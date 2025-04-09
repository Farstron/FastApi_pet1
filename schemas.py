from pydantic import BaseModel, ConfigDict

class STaskAdd(BaseModel):
    name: str
    desciption: str | None = None

class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class STaskID(BaseModel):
    ok: bool = True
    task_id: int