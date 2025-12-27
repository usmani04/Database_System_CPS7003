PRAGMA foreign_keys = ON;

CREATE TABLE museum (
    museum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE exhibit (
    exhibit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    museum_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (museum_id) REFERENCES museum(museum_id)
);

CREATE TABLE artefact (
    artefact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exhibit_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    material TEXT,
    acquisition_date DATE,
    origin TEXT,
    FOREIGN KEY (exhibit_id) REFERENCES exhibit(exhibit_id)
);

CREATE TABLE visitor (
    visitor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    country TEXT
);

CREATE TABLE visit (
    visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    visitor_id INTEGER NOT NULL,
    exhibit_id INTEGER NOT NULL,
    visit_date DATE,
    feedback_rating INTEGER,
    FOREIGN KEY (visitor_id) REFERENCES visitor(visitor_id),
    FOREIGN KEY (exhibit_id) REFERENCES exhibit(exhibit_id)
);

CREATE TABLE conservation_record (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artefact_id INTEGER NOT NULL,
    condition_status TEXT NOT NULL,
    treatment_details TEXT,
    last_checked DATE,
    FOREIGN KEY (artefact_id) REFERENCES artefact(artefact_id)
);

CREATE INDEX IF NOT EXISTS idx_visit_exhibit_date
ON visit(exhibit_id, visit_date);

CREATE INDEX IF NOT EXISTS idx_visit_date
ON visit(visit_date);

CREATE INDEX IF NOT EXISTS idx_visitor_country
ON visitor(country);

CREATE INDEX IF NOT EXISTS idx_conservation_last_checked
ON conservation_record(last_checked);

CREATE TRIGGER IF NOT EXISTS flag_overdue_conservation
AFTER INSERT ON conservation_record
BEGIN
    UPDATE conservation_record
    SET condition_status = 'Inspection Overdue'
    WHERE julianday('now') - julianday(last_checked) > 180;
END;