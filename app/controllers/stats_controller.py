from fastapi import APIRouter, Depends

from app.controllers.dependencies import get_stats_service
from app.schemas.answer_schema import (
    QuestionResults,
    QuestionTotal,
    UserAnswerResponse,
    UserTotal,
)
from app.services.stats_service import StatsService

router = APIRouter(prefix="/stats", tags=["Stats"])


@router.get("/questions", response_model=list[QuestionResults])
def get_all_questions_results(service: StatsService = Depends(get_stats_service)):
    return service.get_all_questions_results()


@router.get("/questions/{question_id}/options", response_model=QuestionResults)
def get_question_results(question_id: int, service: StatsService = Depends(get_stats_service)):
    return service.get_question_results(question_id)


@router.get("/questions/{question_id}/total", response_model=QuestionTotal)
def get_question_total(question_id: int, service: StatsService = Depends(get_stats_service)):
    return service.get_question_total(question_id)


@router.get("/users/{user_id}/answers", response_model=list[UserAnswerResponse])
def get_user_answers(user_id: int, service: StatsService = Depends(get_stats_service)):
    return service.get_user_answers(user_id)


@router.get("/users/{user_id}/total", response_model=UserTotal)
def get_user_total(user_id: int, service: StatsService = Depends(get_stats_service)):
    return service.get_user_total(user_id)
