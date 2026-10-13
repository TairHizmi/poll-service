from fastapi import APIRouter, Depends, status

from app.controllers.dependencies import get_answer_service
from app.schemas.answer_schema import AnswerRequest, AnswerResponse
from app.services.answer_service import AnswerService

router = APIRouter(prefix="/answers", tags=["Answers"])


@router.post("", response_model=AnswerResponse, status_code=status.HTTP_201_CREATED)
def submit_answer(data: AnswerRequest, service: AnswerService = Depends(get_answer_service)):
    return service.submit_answer(data)


@router.put("", response_model=AnswerResponse)
def update_answer(data: AnswerRequest, service: AnswerService = Depends(get_answer_service)):
    return service.update_answer(data)


@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_answers(user_id: int, service: AnswerService = Depends(get_answer_service)):
    service.delete_user_answers(user_id)
