CREATE TABLE roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

CREATE TABLE articles (
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES users(user_id)
);

CREATE TABLE favorites (
    user_id INTEGER NOT NULL,
    article_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, article_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (article_id) REFERENCES articles(article_id)
);

INSERT INTO roles (name)
VALUES ('Автор'), ('Читатель');

INSERT INTO users (login, password, role_id)
VALUES
    ('ivan', '12345', 1),
    ('anna', 'qwerty', 1),
    ('petr', '11111', 2),
    ('maria', '22222', 2);

INSERT INTO articles (title, content, author_id)
VALUES
    ('Современные технологии', 'Статья о современных технологиях.', 1),
    ('История науки', 'Статья об истории науки.', 2),
    ('Будущее образования', 'Статья о будущем образования.', 1);

INSERT INTO favorites (user_id, article_id)
VALUES
    (3, 1),
    (3, 2),
    (4, 1);