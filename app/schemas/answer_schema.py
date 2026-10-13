from pydantic import BaseModel, Field


class AnswerRequest(BaseModel):
    user_id: int
    question_id: int
    selected_option: int = Field(ge=1, le=4)


class AnswerResponse(BaseModel):
    user_id: int
    question_id: int
    selected_option: int


class UserAnswerResponse(BaseModel):
    question_id: int
    question_title: str
    selected_option: int
    selected_option_text: str


class OptionResult(BaseModel):
    option_number: int
    option_text: str
    users_count: int


class QuestionResults(BaseModel):
    question_id: int
    title: str
    options: list[OptionResult]


class QuestionTotal(BaseModel):
    question_id: int
    total_answers: int


class UserTotal(BaseModel):
    user_id: int
    total_answers: int
