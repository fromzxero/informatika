from repositories.article_repository import ArticleRepository
from models.article import Article


class ArticleService:

    def __init__(self):
        self.repository = ArticleRepository()

    def get_by_id(self, article_id: int) -> Article | None:
        return self.repository.get_by_id(article_id)

    def get_all(self) -> list[Article]:
        return self.repository.get_all()

    def create(self, article: Article) -> int:
        if not article.title.strip():
            raise ValueError("Название статьи не может быть пустым")

        if not article.content.strip():
            raise ValueError("Содержание статьи не может быть пустым")

        return self.repository.create(article)

    def update(self, article: Article) -> None:
        existing_article = self.repository.get_by_id(article.article_id)

        if existing_article is None:
            raise ValueError("Статья не найдена")

        if not article.title.strip():
            raise ValueError("Название статьи не может быть пустым")

        if not article.content.strip():
            raise ValueError("Содержание статьи не может быть пустым")

        self.repository.update(article)

    def delete(self, article_id: int) -> None:
        existing_article = self.repository.get_by_id(article_id)

        if existing_article is None:
            raise ValueError("Статья не найдена")

        self.repository.delete(article_id)