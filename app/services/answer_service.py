from fastapi import HTTPException

from app.clients.user_client import UserClient
from app.models.answer_model import Answer
from app.repositories.answer_repository import AnswerRepository
from app.repositories.question_repository import QuestionRepository
from app.schemas.answer_schema import AnswerRequest


class AnswerService:
    def __init__(
        self,
        answer_repository: AnswerRepository,
        question_repository: QuestionRepository,
        user_client: UserClient,
    ):
        self.answer_repository = answer_repository
        self.question_repository = question_repository
        self.user_client = user_client

    def _validate_request(self, data: AnswerRequest) -> None:
        if not self.question_repository.get_by_id(data.question_id):
            raise HTTPException(status_code=404, detail="Question not found")
        user = self.user_client.get_user(data.user_id)
        if not user["is_registered"]:
            raise HTTPException(status_code=403, detail="User is not registered")

    def submit_answer(self, data: AnswerRequest) -> Answer:
        self._validate_request(data)
        if self.answer_repository.get_by_user_and_question(data.user_id, data.question_id):
            raise HTTPException(
                status_code=409, detail="User already answered this question"
            )
        return self.answer_repository.create(Answer(**data.model_dump()))

    def update_answer(self, data: AnswerRequest) -> Answer:
        self._validate_request(data)
        answer = self.answer_repository.get_by_user_and_question(
            data.user_id, data.question_id
        )
        if not answer:
            raise HTTPException(status_code=404, detail="Answer not found")
        answer.selected_option = data.selected_option
        return self.answer_repository.update(answer)

    def delete_user_answers(self, user_id: int) -> None:
        self.answer_repository.delete_by_user(user_id)
