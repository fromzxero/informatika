from models.article import Article
from repositories.base_repository import BaseRepository


class ArticleRepository(BaseRepository):
    def get_by_id(self, article_id: int) -> Article | None:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT article_id, title, content, author_id FROM articles WHERE article_id = ?",
                (article_id,),
            )
            row = cursor.fetchone()
        finally:
            self.close()
        return Article(*row) if row else None

    def get_all(self) -> list[Article]:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT article_id, title, content, author_id FROM articles")
            rows = cursor.fetchall()
        finally:
            self.close()
        return [Article(*row) for row in rows]

    def create(self, article: Article) -> int:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO articles (title, content, author_id) VALUES (?, ?, ?)",
                (article.title, article.content, article.author_id),
            )
            connection.commit()
            article_id = cursor.lastrowid
        finally:
            self.close()
        return article_id

    def update(self, article: Article) -> None:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE articles SET title = ?, content = ?, author_id = ? WHERE article_id = ?",
                (article.title, article.content, article.author_id, article.article_id),
            )
            connection.commit()
        finally:
            self.close()

    def delete(self, article_id: int) -> int:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM articles WHERE article_id = ?", (article_id,))
            connection.commit()
            deleted = cursor.rowcount
        finally:
            self.close()
        return deleted