# Импорт sqlite и random для игры
import sqlite3
from random import randint
# Объявляем db и sql глабальными , что бы небыло проблем использования в различных методах
global db
global sql
# Зоздаем базу и курсор
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash INT
)""")
# Всегда подтверждаем
db.commit()

# функция регестрации
def reg():
    user_login = input("Login:")
    user_password = input("Password")

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES ('{user_login}','{user_password}',{0})")
        db.commit()

        print("Зарегался")
    else:
        print("Такая запись уже есть")

        for value in sql.execute("SELECT * FROM users"):
            print(value[0])

# Функция удаления
def delete_db():
    sql.execute(f"DELETE FROM users WHERE login='{user_login}'")
    db.commit()

    print("Запись удалена")

# Игра
def casino():
    global user_login
    user_login = input("Log in: ")
    number = randint(1, 2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]


    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print("Такого пользователя нет, Зереагайся")
        reg()
    else:
        if number == 1:
            sql.execute(f'UPDATE users SET cash = {1000+ balance} WHERE login ="{user_login}"')
            db.commit()
        else:
            print("lose")
            delete_db()

# Вывод на экран авторизации
def enter():
    for i in sql.execute('SELECT login,cash FROM users'):
        print(i)

# Вывод всех вункций
def main():
    casino()
    enter()

main()