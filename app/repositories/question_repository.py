from sqlalchemy.orm import Session

from app.models.question_model import Question


class QuestionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, question: Question) -> Question:
        self.db.add(question)
        self.db.commit()
        self.db.refresh(question)
        return question

    def get_by_id(self, question_id: int) -> Question | None:
        return self.db.get(Question, question_id)

    def get_all(self) -> list[Question]:
        return self.db.query(Question).all()

    def update(self, question: Question) -> Question:
        self.db.commit()
        self.db.refresh(question)
        return question

    def delete(self, question: Question) -> None:
        self.db.delete(question)
        self.db.commit()
