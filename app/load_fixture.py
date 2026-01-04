import json, os
from datetime import date
from db.dal import DataAccessLayer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURE_PATH = os.path.join(BASE_DIR, "heritageplus_fixture.json")


def load_fixture():
    dal = DataAccessLayer()

    with open(FIXTURE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # ---------------- Museums ----------------
    museum_map = {}
    for m in data["museums"]:
        museum = dal.add_museum(m["name"], m["location"])
        museum_map[m["id"]] = museum.museum_id

    # ---------------- Exhibits ----------------
    exhibit_map = {}
    for e in data["exhibits"]:
        exhibit = dal.add_exhibit(
            museum_id=museum_map[e["museum_id"]],
            title=e["title"],
            description=e["description"],
            start_date=date.fromisoformat(e["start_date"]),
            end_date=date.fromisoformat(e["end_date"]),
        )
        exhibit_map[e["id"]] = exhibit.exhibit_id

    # ---------------- Visitors ----------------
    visitor_map = {}
    for v in data["visitors"]:
        visitor = dal.add_visitor(
            v["full_name"],
            v["age"],
            v["gender"],
            v["country"]
        )
        visitor_map[v["id"]] = visitor.visitor_id

    # ---------------- Visits ----------------
    for visit in data["visits"]:
        dal.add_visit(
            visitor_id=visitor_map[visit["visitor_id"]],
            exhibit_id=exhibit_map[visit["exhibit_id"]],
            visit_date=date.fromisoformat(visit["visit_date"]),
            feedback_rating=visit["rating"]
        )

    dal.close()
    print("✔ Fixture data loaded successfully.")


if __name__ == "__main__":
    load_fixture()
