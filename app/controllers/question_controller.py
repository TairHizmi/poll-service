from fastapi import APIRouter, Depends, status

from app.controllers.dependencies import get_question_service
from app.schemas.question_schema import QuestionCreate, QuestionResponse, QuestionUpdate
from app.services.question_service import QuestionService

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
def create_question(
    data: QuestionCreate, service: QuestionService = Depends(get_question_service)
):
    return service.create_question(data)


@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, service: QuestionService = Depends(get_question_service)):
    return service.get_question(question_id)


@router.put("/{question_id}", response_model=QuestionResponse)
def update_question(
    question_id: int,
    data: QuestionUpdate,
    service: QuestionService = Depends(get_question_service),
):
    return service.update_question(question_id, data)


@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(
    question_id: int, service: QuestionService = Depends(get_question_service)
):
    service.delete_question(question_id)
