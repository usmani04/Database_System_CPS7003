from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Museum(Base):
    __tablename__ = "museum"
    museum_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    exhibits = relationship("Exhibit", back_populates="museum")


class Exhibit(Base):
    __tablename__ = "exhibit"
    exhibit_id = Column(Integer, primary_key=True)
    museum_id = Column(Integer, ForeignKey("museum.museum_id"))
    title = Column(String, nullable=False)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    museum = relationship("Museum", back_populates="exhibits")
    artefacts = relationship("Artefact", back_populates="exhibit")
    visits = relationship("Visit", back_populates="exhibit")


class Artefact(Base):
    __tablename__ = "artefact"
    artefact_id = Column(Integer, primary_key=True)
    exhibit_id = Column(Integer, ForeignKey("exhibit.exhibit_id"))
    name = Column(String, nullable=False)
    material = Column(String)
    acquisition_date = Column(Date)
    origin = Column(String)

    exhibit = relationship("Exhibit", back_populates="artefacts")
    conservation_records = relationship("ConservationRecord", back_populates="artefact")


class Visitor(Base):
    __tablename__ = "visitor"
    visitor_id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    country = Column(String)

    visits = relationship("Visit", back_populates="visitor")


class Visit(Base):
    __tablename__ = "visit"
    visit_id = Column(Integer, primary_key=True)
    visitor_id = Column(Integer, ForeignKey("visitor.visitor_id"))
    exhibit_id = Column(Integer, ForeignKey("exhibit.exhibit_id"))
    visit_date = Column(Date)
    feedback_rating = Column(Integer)

    visitor = relationship("Visitor", back_populates="visits")
    exhibit = relationship("Exhibit", back_populates="visits")


class ConservationRecord(Base):
    __tablename__ = "conservation_record"
    record_id = Column(Integer, primary_key=True)
    artefact_id = Column(Integer, ForeignKey("artefact.artefact_id"))
    condition_status = Column(String, nullable=False)
    treatment_details = Column(String)
    last_checked = Column(Date)

    artefact = relationship("Artefact", back_populates="conservation_records")
