from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.controllers.answer_controller import router as answer_router
from app.controllers.question_controller import router as question_router
from app.controllers.stats_controller import router as stats_router
from app.database import Base, engine
from app.models import answer_model, question_model  # noqa: F401  (registers the tables)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Poll Service", lifespan=lifespan)
app.include_router(question_router)
app.include_router(answer_router)
app.include_router(stats_router)
