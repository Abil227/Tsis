import psycopg2
from psycopg2 import OperationalError

def connect_db():
    try:
        # Устанавливаем соединение с базой данных PostgreSQL
        return psycopg2.connect(
            host="localhost",
            port="5432",
            database="suppliers",
            user="postgres",
            connect_timeout=10,
            sslmode="prefer"
        )
    except OperationalError as e:
        # Выводим сообщение об ошибке, если соединение не удалось
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def search_records(pattern):
    conn = connect_db()
    if conn is None:
        return []

    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT id, name, phone FROM phonebook
            WHERE name LIKE %s OR phone LIKE %s
        """, ('%' + pattern + '%', '%' + pattern + '%'))
        return cur.fetchall()
    except OperationalError as e:
        print(f"Ошибка выполнения запроса: {e}")
        return []
    finally:
        cur.close()
        conn.close()

def insert_or_update_user(user_name, user_phone):
    conn = connect_db()
    if conn is None:
        return

    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO phonebook(name, phone)
            VALUES(%s, %s)
            ON CONFLICT (name)
            DO UPDATE SET phone = %s
        """, (user_name, user_phone, user_phone))
        conn.commit()
        print("Пользователь успешно добавлен или обновлен.")
    except OperationalError as e:
        print(f"Ошибка выполнения запроса: {e}")
    finally:
        cur.close()
        conn.close()

# Другие функции (insert_users, get_records_with_pagination, delete_record) могут быть реализованы аналогичным образом...

def main():
    while True:
        print("\n1. Поиск записей по шаблону")
        print("2. Добавить или обновить пользователя")
        # Добавьте остальные варианты подобным образом...
        print("6. Выйти")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            pattern = input("Введите шаблон для поиска: ")
            records = search_records(pattern)
            if records:
                print("Найденные записи:")
                for record in records:
                    print(record)
            else:
                print("Записи не найдены.")
        elif choice == '2':
            user_name = input("Введите имя пользователя: ")
            user_phone = input("Введите номер телефона пользователя: ")
            insert_or_update_user(user_name, user_phone)
        # Добавьте остальные варианты подобным образом...
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()