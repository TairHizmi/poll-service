from fastapi import HTTPException

from app.models.question_model import Question
from app.repositories.answer_repository import AnswerRepository
from app.repositories.question_repository import QuestionRepository
from app.schemas.answer_schema import (
    OptionResult,
    QuestionResults,
    QuestionTotal,
    UserAnswerResponse,
    UserTotal,
)


def _option_text(question: Question, option_number: int) -> str:
    return getattr(question, f"option_{option_number}")


class StatsService:
    def __init__(
        self, answer_repository: AnswerRepository, question_repository: QuestionRepository
    ):
        self.answer_repository = answer_repository
        self.question_repository = question_repository

    def _get_question(self, question_id: int) -> Question:
        question = self.question_repository.get_by_id(question_id)
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        return question

    @staticmethod
    def _build_results(question: Question, counts: dict[int, int]) -> QuestionResults:
        options = [
            OptionResult(
                option_number=number,
                option_text=_option_text(question, number),
                users_count=counts.get(number, 0),
            )
            for number in range(1, 5)
        ]
        return QuestionResults(question_id=question.id, title=question.title, options=options)

    def get_question_results(self, question_id: int) -> QuestionResults:
        question = self._get_question(question_id)
        counts = self.answer_repository.count_options_by_question(question_id)
        return self._build_results(question, counts)

    def get_question_total(self, question_id: int) -> QuestionTotal:
        self._get_question(question_id)
        total = self.answer_repository.count_by_question(question_id)
        return QuestionTotal(question_id=question_id, total_answers=total)

    def get_user_answers(self, user_id: int) -> list[UserAnswerResponse]:
        result = []
        for answer in self.answer_repository.get_by_user(user_id):
            question = self.question_repository.get_by_id(answer.question_id)
            result.append(
                UserAnswerResponse(
                    question_id=question.id,
                    question_title=question.title,
                    selected_option=answer.selected_option,
                    selected_option_text=_option_text(question, answer.selected_option),
                )
            )
        return result

    def get_user_total(self, user_id: int) -> UserTotal:
        total = self.answer_repository.count_by_user(user_id)
        return UserTotal(user_id=user_id, total_answers=total)

    def get_all_questions_results(self) -> list[QuestionResults]:
        all_counts = self.answer_repository.count_options_all_questions()
        results = []
        for question in self.question_repository.get_all():
            counts = {
                number: all_counts.get((question.id, number), 0) for number in range(1, 5)
            }
            results.append(self._build_results(question, counts))
        return results
