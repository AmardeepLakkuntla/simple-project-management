from fastapi import FastAPI
from src.tasks import router as task_router
from src.projects import router as project_router

app=FastAPI()


app.include_router(project_router)
app.include_router(task_router)

