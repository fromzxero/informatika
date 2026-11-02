from models.role import Role
from repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository):
    def get_by_id(self, role_id: int) -> Role | None:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT role_id, name FROM roles WHERE role_id = ?",
                (role_id,),
            )
            row = cursor.fetchone()
        finally:
            self.close()
        return Role(*row) if row else None

    def get_all(self) -> list[Role]:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT role_id, name FROM roles")
            rows = cursor.fetchall()
        finally:
            self.close()
        return [Role(*row) for row in rows]

    def create(self, role: Role) -> int:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO roles (name) VALUES (?)",
                (role.name,),
            )
            connection.commit()
            role_id = cursor.lastrowid
        finally:
            self.close()
        return role_id

    def update(self, role: Role) -> None:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE roles SET name = ? WHERE role_id = ?",
                (role.name, role.role_id),
            )
            connection.commit()
        finally:
            self.close()

    def delete(self, role_id: int) -> int:
        connection = self.connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM roles WHERE role_id = ?",
                (role_id,),
            )
            connection.commit()
            deleted = cursor.rowcount
        finally:
            self.close()
        return deleted