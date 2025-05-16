from pydantic import BaseModel,Field
from typing import List,Annotated,operator

class State(BaseModel):
    query : str = Field(description='The query given by the user')
    answer : Annotated[List[str],operator.add] = Field(description="Answer given by the application for better understanding of the user")

