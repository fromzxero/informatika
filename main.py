#
#
#
# import sqlite3
#
# # Подключаемся к нашей базе данных
# conn = sqlite3.connect('C:/Users/drago/IdeaProjects/untitled/.idea/database/journal.db')
# cursor = conn.cursor()
#
# # Пример: вытащить всех пользователей
# cursor.execute("SELECT login, password FROM users")
# users = cursor.fetchall()
# print("Список пользователей:")
# for user in users:
#     print(f"Логин: {user[0]}, Пароль: {user[1]}")

# Не забываем закрыть соединение
#conn.close()


from services.user_service import UserService
from services.article_service import ArticleService
from services.role_service import RoleService
from services.favorite_service import FavoriteService

from models.users import User
from models.article import Article
from models.favorite import Favorite


user_service = UserService()
article_service = ArticleService()
role_service = RoleService()
favorite_service = FavoriteService()


def register():
    print("\n=== Регистрация ===")

    login = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()

    roles = role_service.get_all()

    if not roles:
        print("В базе данных нет ролей.")
        return

    # Новые пользователи получают роль user
    user_role = next(
        (role for role in roles if role.name.lower() == "читатель"),
        None
    )

    if user_role is None:
        print("Роль user не найдена в базе данных.")
        return

    user = User(
        user_id=0,
        login=login,
        password=password,
        role_id=user_role.role_id
    )

    try:
        user_service.create(user)
        print("Регистрация прошла успешно!")
    except ValueError as error:
        print(error)


def login():
    print("\n=== Авторизация ===")

    login_value = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()

    users = user_service.get_all()

    for user in users:
        if user.login == login_value and user.password == password:
            print(f"Добро пожаловать, {user.login}!")
            return user

    print("Неверный логин или пароль.")
    return None


def show_articles():
    print("\n=== Список статей ===")

    articles = article_service.get_all()

    if not articles:
        print("Статей пока нет.")
        return

    for article in articles:
        print(f"\nID: {article.article_id}")
        print(f"Название: {article.title}")
        print(f"Содержание: {article.content}")
        print(f"Автор ID: {article.author_id}")


def add_article(current_user):
    print("\n=== Добавление статьи ===")

    title = input("Введите название: ")
    content = input("Введите содержание: ")

    article = Article(
        article_id=0,
        title=title,
        content=content,
        author_id=current_user.user_id
    )

    try:
        article_service.create(article)
        print("Статья успешно добавлена!")
    except ValueError as error:
        print(error)


def delete_article():
    print("\n=== Удаление статьи ===")

    try:
        article_id = int(input("Введите ID статьи: "))
        article_service.delete(article_id)
        print("Статья удалена!")
    except ValueError as error:
        print(error)


def add_favorite(current_user):
    print("\n=== Добавление в избранное ===")

    try:
        article_id = int(input("Введите ID статьи: "))

        favorite = Favorite(
            user_id=current_user.user_id,
            article_id=article_id
        )

        favorite_service.create(favorite)
        print("Статья добавлена в избранное!")

    except ValueError as error:
        print(error)


def show_favorites(current_user):
    print("\n=== Избранное ===")

    favorites = favorite_service.get_all()

    user_favorites = [
        favorite for favorite in favorites
        if favorite.user_id == current_user.user_id
    ]

    if not user_favorites:
        print("Избранное пустое.")
        return

    for favorite in user_favorites:
        article = article_service.get_by_id(favorite.article_id)

        if article:
            print(f"ID: {article.article_id} — {article.title}")


def delete_favorite(current_user):
    print("\n=== Удаление из избранного ===")

    try:
        article_id = int(input("Введите ID статьи: "))

        favorite_service.delete(
            current_user.user_id,
            article_id
        )

        print("Статья удалена из избранного!")

    except ValueError as error:
        print(error)


def show_users():
    print("\n=== Список пользователей ===")

    users = user_service.get_all()

    for user in users:
        print(f"ID: {user.user_id}, Логин: {user.login}, Роль ID: {user.role_id}")



def user_menu(current_user):
    while True:
        print("\n=== Меню читателя ===")
        print("1. Просмотреть статьи")
        print("2. Добавить в избранное")
        print("3. Посмотреть избранное")
        print("4. Удалить из избранного")
        print("5. Выйти из аккаунта")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_articles()
        elif choice == "2":
            add_favorite(current_user)
        elif choice == "3":
            show_favorites(current_user)
        elif choice == "4":
            delete_favorite(current_user)
        elif choice == "5":
            break
        else:
            print("Неверный выбор.")



def admin_menu(current_user):
    while True:
        print("\n=== Меню администратора ===")
        print("1. Просмотреть статьи")
        print("2. Добавить статью")
        print("3. Удалить статью")
        print("4. Просмотреть пользователей")
        print("5. Выйти из аккаунта")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_articles()

        elif choice == "2":
            add_article(current_user)

        elif choice == "3":
            delete_article()

        elif choice == "4":
            show_users()

        elif choice == "5":
            break

        else:
            print("Неверный выбор.")


def main():
    while True:
        print("\n========== ЖУРНАЛ СТАТЕЙ ==========")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            register()

        elif choice == "2":
            current_user = login()

            if current_user:
                role = role_service.get_by_id(current_user.role_id)

                if role and role.name.lower() == "автор":
                    admin_menu(current_user)
                else:
                    user_menu(current_user)

        elif choice == "3":
            print("До свидания!")
            break

        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
