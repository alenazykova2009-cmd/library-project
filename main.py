from storage import load_books, add_book, remove_book


def main():
    books = load_books()

    print("--- 1. Проверяем добавление книги Пушкина ---")
    books = add_book(books, "Капитанская дочка", "Пушкин")

    print("\n--- 2. Пробуем добавить дубликат (не должен добавиться) ---")
    books = add_book(books, "Евгений Онегин", "Пушкин")

    print("\n--- 3. Удаляем книгу ---")
    books = remove_book(books, "Война и мир")

    print("\nИтоговый список книг на диске:")
    for b in books:
        print(f" - {b['title']} ({b['author']})")


if __name__ == "__main__":
    main()