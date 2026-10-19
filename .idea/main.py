c=input()


print('Helo')


с=200
print(c)


import sqlite3

# Подключаемся к нашей базе данных
conn = sqlite3.connect('C:/Users/drago/IdeaProjects/untitled/.idea/database/journal.db')
cursor = conn.cursor()

# Пример: вытащить всех пользователей
cursor.execute("SELECT login, password FROM users")
users = cursor.fetchall()
print("Список пользователей:")
for user in users:
    print(f"Логин: {user[0]}, Пароль: {user[1]}")

# Не забываем закрыть соединение
conn.close()