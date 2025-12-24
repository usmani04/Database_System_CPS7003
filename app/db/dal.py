from sqlalchemy import func
from .base import SessionLocal
from .models import (
    Museum, Exhibit, Artefact,
    Visitor, Visit, ConservationRecord
)

class DataAccessLayer:

    def __init__(self):
        self.session = SessionLocal()

    # ---------- CREATE ----------
    def add_museum(self, name, location):
        museum = Museum(name=name, location=location)
        self.session.add(museum)
        self.session.commit()
        return museum

    def add_exhibit(self, museum_id, title, description, start_date, end_date):
        exhibit = Exhibit(
            museum_id=museum_id,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        self.session.add(exhibit)
        self.session.commit()
        return exhibit

    def add_visitor(self, full_name, age, gender, country):
        visitor = Visitor(
            full_name=full_name,
            age=age,
            gender=gender,
            country=country
        )
        self.session.add(visitor)
        self.session.commit()
        return visitor

    # ---------- READ ----------
    def get_exhibits_with_museum(self):
        return (
            self.session.query(Exhibit.title, Museum.name)
            .join(Museum)
            .order_by(Exhibit.start_date)
            .all()
        )

    # ---------- ADVANCED ANALYTICS ----------
    def visitors_by_country(self):
        return (
            self.session.query(
                Visitor.country,
                func.count(Visitor.visitor_id).label("total_visitors")
            )
            .group_by(Visitor.country)
            .order_by(func.count(Visitor.visitor_id).desc())
            .all()
        )

    def visit_counts_per_exhibit(self):
        return (
            self.session.query(
                Exhibit.title,
                func.count(Visit.visit_id).label("total_visits")
            )
            .join(Visit, Visit.exhibit_id == Exhibit.exhibit_id)
            .group_by(Exhibit.title)
            .order_by(func.count(Visit.visit_id).desc())
            .all()
        )

    def close(self):
        self.session.close()
