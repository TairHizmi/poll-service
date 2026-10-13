from fastapi import Depends
from sqlalchemy.orm import Session

from app.clients.user_client import UserClient
from app.database import get_db
from app.repositories.answer_repository import AnswerRepository
from app.repositories.question_repository import QuestionRepository
from app.services.answer_service import AnswerService
from app.services.question_service import QuestionService
from app.services.stats_service import StatsService


def get_question_service(db: Session = Depends(get_db)) -> QuestionService:
    return QuestionService(QuestionRepository(db))


def get_answer_service(db: Session = Depends(get_db)) -> AnswerService:
    return AnswerService(AnswerRepository(db), QuestionRepository(db), UserClient())


def get_stats_service(db: Session = Depends(get_db)) -> StatsService:
    return StatsService(AnswerRepository(db), QuestionRepository(db))
