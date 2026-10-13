from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.answer_model import Answer


class AnswerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, answer: Answer) -> Answer:
        self.db.add(answer)
        self.db.commit()
        self.db.refresh(answer)
        return answer

    def get_by_user_and_question(self, user_id: int, question_id: int) -> Answer | None:
        return (
            self.db.query(Answer)
            .filter(Answer.user_id == user_id, Answer.question_id == question_id)
            .first()
        )

    def update(self, answer: Answer) -> Answer:
        self.db.commit()
        self.db.refresh(answer)
        return answer

    def get_by_user(self, user_id: int) -> list[Answer]:
        return self.db.query(Answer).filter(Answer.user_id == user_id).all()

    def count_by_user(self, user_id: int) -> int:
        return self.db.query(func.count(Answer.id)).filter(Answer.user_id == user_id).scalar()

    def count_by_question(self, question_id: int) -> int:
        return (
            self.db.query(func.count(Answer.id))
            .filter(Answer.question_id == question_id)
            .scalar()
        )

    def count_options_by_question(self, question_id: int) -> dict[int, int]:
        rows = (
            self.db.query(Answer.selected_option, func.count(Answer.id))
            .filter(Answer.question_id == question_id)
            .group_by(Answer.selected_option)
            .all()
        )
        return {option: count for option, count in rows}

    def count_options_all_questions(self) -> dict[tuple[int, int], int]:
        rows = (
            self.db.query(Answer.question_id, Answer.selected_option, func.count(Answer.id))
            .group_by(Answer.question_id, Answer.selected_option)
            .all()
        )
        return {(question_id, option): count for question_id, option, count in rows}

    def delete_by_user(self, user_id: int) -> None:
        self.db.query(Answer).filter(Answer.user_id == user_id).delete()
        self.db.commit()
