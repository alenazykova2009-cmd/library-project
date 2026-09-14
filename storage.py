import json
import os

DATA_FILE = "data/books.json"
LOG_FILE = "logs/operations.log"


def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_books(books):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def log_operation(message):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def add_book(books, title, author):
    # ИСПРАВЛЕНИЕ 1: Сравниваем и название, И автора!
    for book in books:
        if book["title"] == title and book["author"] == author:
            print(f"Книга '{title}' уже есть в списке!")
            return books

    books.append({"title": title, "author": author})
    print(f"Книга '{title}' успешно добавлена")
    log_operation(f"ADD: {title} — {author}")

    # ИСПРАВЛЕНИЕ 2: Сразу сохраняем изменения на диск!
    save_books(books)
    return books


def remove_book(books, title):
    for book in books:
        if book["title"] == title:
            books.remove(book)
            print(f"Книга '{title}' удалена")
            log_operation(f"REMOVE: {title}")

            # ИСПРАВЛЕНИЕ 2: Сохраняем на диск после удаления!
            save_books(books)
            return books

    print(f"Книга '{title}' не найдена")
    return books