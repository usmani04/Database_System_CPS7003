import sqlite3

DB_PATH = "database/heritageplus.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_exhibits_with_museum():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT e.title, m.name AS museum_name
        FROM exhibit e
        JOIN museum m ON e.museum_id = m.museum_id
        ORDER BY e.start_date ASC
    """)

    results = cursor.fetchall()
    conn.close()
    return results

def most_visited_exhibits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT e.title, COUNT(v.visit_id) AS total_visits
        FROM visit v
        JOIN exhibit e ON v.exhibit_id = e.exhibit_id
        GROUP BY e.title
        ORDER BY total_visits DESC
    """)

    results = cursor.fetchall()
    conn.close()
    return results

def conservation_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.name, c.condition_status, c.last_checked
        FROM conservation_record c
        JOIN artefact a ON c.artefact_id = a.artefact_id
        ORDER BY c.last_checked DESC
    """)

    results = cursor.fetchall()
    conn.close()
    return results

def visitors_by_country():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT country, COUNT(visitor_id) AS total_visitors
        FROM visitor
        GROUP BY country
        ORDER BY total_visitors DESC
    """)

    results = cursor.fetchall()
    conn.close()
    return results
