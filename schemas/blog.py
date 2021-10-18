from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    slug: str
    description: str