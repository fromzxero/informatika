from repositories.favorite_repository import FavoriteRepository
from repositories.user_repository import UserRepository
from repositories.article_repository import ArticleRepository
from models.favorite import Favorite


class FavoriteService:

    def __init__(self):
        self.repository = FavoriteRepository()
        self.user_repository = UserRepository()
        self.article_repository = ArticleRepository()

    def get_all(self) -> list[Favorite]:
        return self.repository.get_all()

    def create(self, favorite: Favorite) -> None:
        user = self.user_repository.get_by_id(favorite.user_id)
        if user is None:
            raise ValueError("Пользователь не найден")

        article = self.article_repository.get_by_id(favorite.article_id)
        if article is None:
            raise ValueError("Статья не найдена")

        favorites = self.repository.get_all()
        for existing in favorites:
            if (existing.user_id == favorite.user_id
                    and existing.article_id == favorite.article_id):
                raise ValueError("Статья уже добавлена в избранное")

        self.repository.create(favorite)

    def delete(self, user_id: int, article_id: int) -> None:
        favorites = self.repository.get_all()

        for favorite in favorites:
            if favorite.user_id == user_id and favorite.article_id == article_id:
                self.repository.delete(user_id, article_id)
                return

        raise ValueError("Статья не найдена в избранном")