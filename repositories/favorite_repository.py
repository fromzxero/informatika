from models.favorite import Favorite
from repositories.base_repository import BaseRepository


class FavoriteRepository(BaseRepository):

    def get_all(self) -> list[Favorite]:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT user_id, article_id FROM favorites"
            )
            rows = cursor.fetchall()
        finally:
            self.close()

        return [Favorite(*row) for row in rows]

    def create(self, favorite: Favorite) -> None:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO favorites (user_id, article_id) VALUES (?, ?)",
                (favorite.user_id, favorite.article_id)
            )
            connection.commit()
        finally:
            self.close()

    def delete(self, user_id: int, article_id: int) -> int:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM favorites WHERE user_id = ? AND article_id = ?",
                (user_id, article_id)
            )
            connection.commit()
            deleted = cursor.rowcount
        finally:
            self.close()

        return deleted