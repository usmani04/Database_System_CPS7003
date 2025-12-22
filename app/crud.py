import sqlite3

DB_PATH = "database/heritageplus.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def add_exhibit(museum_id, title, description, start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO exhibit (museum_id, title, description, start_date, end_date)
        VALUES (?, ?, ?, ?, ?)
    """, (museum_id, title, description, start_date, end_date))

    conn.commit()
    conn.close()

def list_exhibits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT e.exhibit_id, e.title, m.name
        FROM exhibit e
        JOIN museum m ON e.museum_id = m.museum_id
        ORDER BY e.start_date
    """)

    results = cursor.fetchall()
    conn.close()
    return results

def add_artefact(exhibit_id, name, material, acquisition_date, origin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO artefact (exhibit_id, name, material, acquisition_date, origin)
        VALUES (?, ?, ?, ?, ?)
    """, (exhibit_id, name, material, acquisition_date, origin))

    conn.commit()
    conn.close()

def add_museum(name, location):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO museum (name, location)
        VALUES (?, ?)
    """, (name, location))

    conn.commit()
    conn.close()

def add_visitor(full_name, age, gender, country):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO visitor (full_name, age, gender, country)
        VALUES (?, ?, ?, ?)
    """, (full_name, age, gender, country))

    conn.commit()
    conn.close()

def add_conservation_record(artefact_id, condition_status, treatment_details, last_checked):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conservation_record
        (artefact_id, condition_status, treatment_details, last_checked)
        VALUES (?, ?, ?, ?)
    """, (artefact_id, condition_status, treatment_details, last_checked))

    conn.commit()
    conn.close()

def list_artefacts_by_exhibit(exhibit_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, material, origin
        FROM artefact
        WHERE exhibit_id = ?
    """, (exhibit_id,))

    results = cursor.fetchall()
    conn.close()
    return results

def update_visitor(visitor_id, age, country):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE visitor
        SET age = ?, country = ?
        WHERE visitor_id = ?
    """, (age, country, visitor_id))

    conn.commit()
    conn.close()

def update_conservation_status(record_id, condition_status, last_checked):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE conservation_record
        SET condition_status = ?, last_checked = ?
        WHERE record_id = ?
    """, (condition_status, last_checked, record_id))

    conn.commit()
    conn.close()

def delete_artefact(artefact_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM artefact
        WHERE artefact_id = ?
    """, (artefact_id,))

    conn.commit()
    conn.close()

def delete_visitor(visitor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM visitor
        WHERE visitor_id = ?
    """, (visitor_id,))

    conn.commit()
    conn.close()
