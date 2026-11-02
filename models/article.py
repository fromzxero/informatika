from dataclasses import dataclass

@dataclass
class Article:
    article_id: int
    title: str
    content: str
    author_id: int