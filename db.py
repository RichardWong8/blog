import sqlite3

DB_FILE = "blog.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

# CREATE TABLES
tables = {
    "users":   "user_id INTEGER, username TEXT, password TEXT",
    "blogs":   "user_id INTEGER, blog_id INTEGER, blog_title TEXT",
    "entries": "user_id INTEGER, blog_id INTEGER, entry_id INTEGER, entry_title TEXT, entry_data TEXT"
}

def open_db():
    global db, c
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

def save():
    global db
    db.commit()
    db.close()

def create_table(table_name, metadata):
    create = "CREATE TABLE IF NOT EXISTS " + table_name + " (" + metadata + ");"
    #print(create)
    c.execute(create)

def create_tables():
    open_db()
    for name in tables:
        create_table(name, tables[name])
    save()

create_tables()

# USER
def add_user(username, password):
    open_db()

    select = "SELECT username FROM users"
    c.execute(select)
    users = c.fetchall()
    user_id = len(users) + 1

    values = (user_id, username, password)
    insert = "INSERT INTO users VALUES (?, ?, ?)"
    c.execute(insert, values)

    save()

def change_password(username, password):
    open_db()
    save()

def get_user_id(username):
    open_db()

    select = "SELECT user_id, username FROM users"
    c.execute(select)
    users = c.fetchall()

    for user_info in users:
        if user_info[1] == username:
            return user_info[0]
    return -1

def authenticate_user(username, password):
    open_db()

    select = "SELECT username, password FROM users"
    c.execute(select)
    users = c.fetchall()

    for user_info in users:
        if user_info[0] == username and user_info[1] == password:
            return True
    return False

# BLOG
def add_blog(user_id, blog_title):
    open_db()
    save()

def change_blog_title(user_id, blog_id, blog_title):
    open_db()
    save()

# ENTRY
def add_entry(user_id, blog_id, entry_id, entry_title, entry_data):
    open_db()
    save()

def change_entry(user_id, blog_id, entry_id, entry_title, entry_data):
    open_db()
    save()

add_user("johnjacobsmith", "donkeyhorsecow")
print(get_user_id("johnjacobsmith"))
print(get_user_id("joejacobsmith"))

print(authenticate_user("johnjacobsmith", "honk"))
print(authenticate_user("joe", "honk"))
print(authenticate_user("johnjacobsmith", "donkeyhorsecow"))
