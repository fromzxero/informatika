from repositories.role_repository import RoleRepository
from models.role import Role


class RoleService:

    def __init__(self):
        self.repository = RoleRepository()

    def get_by_id(self, role_id: int) -> Role | None:
        return self.repository.get_by_id(role_id)

    def get_all(self) -> list[Role]:
        return self.repository.get_all()

    def create(self, role: Role) -> int:
        if not role.name.strip():
            raise ValueError("Название роли не может быть пустым")

        roles = self.repository.get_all()
        for existing_role in roles:
            if existing_role.name == role.name:
                raise ValueError("Такая роль уже существует")

        return self.repository.create(role)

    def update(self, role: Role) -> None:
        existing_role = self.repository.get_by_id(role.role_id)

        if existing_role is None:
            raise ValueError("Роль не найдена")

        if not role.name.strip():
            raise ValueError("Название роли не может быть пустым")

        roles = self.repository.get_all()
        for existing_role in roles:
            if existing_role.name == role.name and existing_role.role_id != role.role_id:
                raise ValueError("Такая роль уже существует")

        self.repository.update(role)

    def delete(self, role_id: int) -> None:
        existing_role = self.repository.get_by_id(role_id)

        if existing_role is None:
            raise ValueError("Роль не найдена")

        self.repository.delete(role_id)