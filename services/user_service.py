from repositories.user_repository import UserRepository
from models.users import User
class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def get_by_id(self, user_id: int) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_all(self) -> list[User]:
        return self.repository.get_all()

    def create(self, user: User) -> int:
        if not user.login.strip():
            raise ValueError("Логин не может быть пустым")

        if not user.password.strip():
            raise ValueError("Пароль не может быть пустым")

        existing_users = self.repository.get_all()
        for existing_user in existing_users:
            if existing_user.login == user.login:
                raise ValueError("Пользователь с таким логином уже существует")

        return self.repository.create(user)

    def update(self, user: User) -> None:
        existing_user = self.repository.get_by_id(user.user_id)

        if existing_user is None:
            raise ValueError("Пользователь не найден")

        if not user.login.strip():
            raise ValueError("Логин не может быть пустым")

        if not user.password.strip():
            raise ValueError("Пароль не может быть пустым")

        users = self.repository.get_all()
        for existing in users:
            if existing.login == user.login and existing.user_id != user.user_id:
                raise ValueError("Этот логин уже занят")

        self.repository.update(user)

    def delete(self, user_id: int) -> None:
        existing_user = self.repository.get_by_id(user_id)

        if existing_user is None:
            raise ValueError("Пользователь не найден")

        self.repository.delete(user_id)