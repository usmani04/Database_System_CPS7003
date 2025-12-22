import sqlite3

def create_database():
    conn = sqlite3.connect("database/heritageplus.db")
    cursor = conn.cursor()

    with open("sql/schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == "__main__":
    create_database()
