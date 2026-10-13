from fastapi import HTTPException

from app.models.question_model import Question
from app.repositories.question_repository import QuestionRepository
from app.schemas.question_schema import QuestionCreate, QuestionUpdate


class QuestionService:
    def __init__(self, repository: QuestionRepository):
        self.repository = repository

    def create_question(self, data: QuestionCreate) -> Question:
        return self.repository.create(Question(**data.model_dump()))

    def get_question(self, question_id: int) -> Question:
        question = self.repository.get_by_id(question_id)
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        return question

    def update_question(self, question_id: int, data: QuestionUpdate) -> Question:
        question = self.get_question(question_id)
        for field, value in data.model_dump().items():
            setattr(question, field, value)
        return self.repository.update(question)

    def delete_question(self, question_id: int) -> None:
        question = self.get_question(question_id)
        self.repository.delete(question)
