import sqlite3


class BaseRepository:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(
            r"C:\Users\drago\IdeaProjects\untitled\.idea\database\journal.db"
        )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None