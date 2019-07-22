import sqlite3

DB_FILE = "blog.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

def save():
    db.commit()
    db.close()

# CREATE TABLES
tables = {
    "users":   "user_id INTEGER, username TEXT, password TEXT",
    "blogs":   "user_id INTEGER, blog_id INTEGER, blog_title TEXT",
    "entries": "user_id INTEGER, blog_id INTEGER, entry_id INTEGER, entry_title TEXT, entry_data TEXT"
}

def create_table(table_name, metadata):
    create = "CREATE TABLE IF NOT EXISTS " + table_name + " (" + metadata + ");"
    print(create)
    c.execute(create)

def create_tables():
    for name in tables:
        create_table(name, tables[name])
    save()

create_tables()

# USER
def add_user(username, password):
    save()

def change_password(username, password):
    save()

def get_user_id(username):
    pass

def get_password(username):
    pass

# BLOG
def add_blog(user_id, blog_title):
    save()

def change_blog_title(user_id, blog_id, blog_title):
    save()

# ENTRY
def add_entry(user_id, blog_id, entry_id, entry_title, entry_data):
    save()

def change_entry(user_id, blog_id, entry_id, entry_title, entry_data):
    save()
