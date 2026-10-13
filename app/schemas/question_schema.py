from pydantic import BaseModel, ConfigDict, Field


class QuestionBase(BaseModel):
    title: str = Field(min_length=1, max_length=500)
    option_1: str = Field(min_length=1, max_length=255)
    option_2: str = Field(min_length=1, max_length=255)
    option_3: str = Field(min_length=1, max_length=255)
    option_4: str = Field(min_length=1, max_length=255)


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
