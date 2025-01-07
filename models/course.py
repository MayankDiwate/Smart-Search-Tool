from typing import List

from pydantic import BaseModel, Field


class Course(BaseModel):
    title: str = Field(..., description="The title of the course")
    image: str = Field(description="The image URL of the course", default="")
    curriculums: List[str] = Field(description="The curriculums of the course", default=[])

    @property
    def content(self) -> str:
        return f"{self.title}\n{self.curriculums}"

class SearchResult(BaseModel):
    courses: List[Course] = Field(..., description="List of courses matching the search query")
    query: str = Field(..., description="The search query used")
