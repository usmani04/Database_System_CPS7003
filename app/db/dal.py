from sqlalchemy import *
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
    
    # ---------- READ / LIST ----------

    def list_museums(self):
        return self.session.query(Museum).all()

    def list_exhibits(self):
        return (
            self.session.query(
                Exhibit.exhibit_id,
                Exhibit.title,
                Museum.name
            )
            .join(Museum)
            .all()
        )

    def list_visitors(self):
        return self.session.query(Visitor).all()

    def list_visits(self):
        return (
            self.session.query(
                Visit.visit_id,
                Visitor.full_name,
                Exhibit.title,
                Visit.visit_date,
                Visit.feedback_rating
            )
            .join(Visitor)
            .join(Exhibit)
            .all()
        )
    
    # ---------- UPDATE ----------

    def update_museum(self, museum_id, name, location):
        museum = self.session.query(Museum).get(museum_id)
        if not museum:
            raise ValueError("Museum not found")

        museum.name = name
        museum.location = location
        self.session.commit()
        return museum


    def update_exhibit(self, exhibit_id, title, description):
        exhibit = self.session.query(Exhibit).get(exhibit_id)
        if not exhibit:
            raise ValueError("Exhibit not found")

        exhibit.title = title
        exhibit.description = description
        self.session.commit()
        return exhibit


    def update_visitor(self, visitor_id, age, country):
        visitor = self.session.query(Visitor).get(visitor_id)
        if not visitor:
            raise ValueError("Visitor not found")

        visitor.age = age
        visitor.country = country
        self.session.commit()
        return visitor


    def update_visit(self, visit_id, rating):
        visit = self.session.query(Visit).get(visit_id)
        if not visit:
            raise ValueError("Visit not found")

        visit.feedback_rating = rating
        self.session.commit()
        return visit


    # ---------- DELETE ----------

    def delete_museum(self, museum_id):
        museum = self.session.query(Museum).get(museum_id)
        if not museum:
            raise ValueError("Museum not found")

        self.session.delete(museum)
        self.session.commit()


    def delete_exhibit(self, exhibit_id):
        exhibit = self.session.query(Exhibit).get(exhibit_id)
        if not exhibit:
            raise ValueError("Exhibit not found")

        self.session.delete(exhibit)
        self.session.commit()


    def delete_visitor(self, visitor_id):
        visitor = self.session.query(Visitor).get(visitor_id)
        if not visitor:
            raise ValueError("Visitor not found")

        self.session.delete(visitor)
        self.session.commit()


    def delete_visit(self, visit_id):
        visit = self.session.query(Visit).get(visit_id)
        if not visit:
            raise ValueError("Visit not found")

        self.session.delete(visit)
        self.session.commit()

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
    
    def add_visit(self, visitor_id, exhibit_id, visit_date, feedback_rating):
        visit = Visit(
            visitor_id=visitor_id,
            exhibit_id=exhibit_id,
            visit_date=visit_date,
            feedback_rating=feedback_rating
        )
        self.session.add(visit)
        self.session.commit()
        return visit


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
    
    def update_conservation_status(self, record_id, condition_status):
        record = (
            self.session.query(ConservationRecord)
            .filter(ConservationRecord.record_id == record_id)
            .first()
        )

        if not record:
            raise ValueError("Conservation record not found")

        record.condition_status = condition_status
        self.session.commit()
        return record

    def add_artefact(self, exhibit_id, name, material, acquisition_date, origin):
        artefact = Artefact(
            exhibit_id=exhibit_id,
            name=name,
            material=material,
            acquisition_date=acquisition_date,
            origin=origin
        )
        self.session.add(artefact)
        self.session.commit()
        return artefact

    def monthly_visit_trends(self):
        return (
            self.session.query(
                extract("month", Visit.visit_date).label("month"),
                func.count(Visit.visit_id).label("visits")
            )
            .group_by("month")
            .order_by("month")
            .all()
        )

    def close(self):
        self.session.close()
