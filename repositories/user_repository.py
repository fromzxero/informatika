from models.users import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def get_by_id(self, user_id: int) -> User | None:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT user_id, login, password, role_id FROM users WHERE user_id = ?",
                (user_id,)
            )
            row = cursor.fetchone()
        finally:
            self.close()
        return User(*row) if row else None

    def get_all(self) -> list[User]:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT user_id, login, password, role_id FROM users")
            rows = cursor.fetchall()
        finally:
            self.close()
        return [User(*row) for row in rows]

    def create(self, user: User) -> int:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (login, password, role_id) VALUES (?, ?, ?)",
                (user.login, user.password, user.role_id)
            )
            connection.commit()
            user_id = cursor.lastrowid
        finally:
            self.close()
        return user_id

    def update(self, user: User) -> None:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE users SET login = ?, password = ?, role_id = ? WHERE user_id = ?",
                (user.login, user.password, user.role_id, user.user_id)
            )
            connection.commit()
        finally:
            self.close()

    def delete(self, user_id: int) -> int:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            connection.commit()
            deleted = cursor.rowcount
        finally:
            self.close()
        return deleted