import csv
from datetime import datetime
from db.dal import DataAccessLayer


class CSVImportService:
    def __init__(self):
        self.dal = DataAccessLayer()

    def import_artefacts(self, csv_path, exhibit_id):
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.dal.add_artefact(
                    exhibit_id=exhibit_id,
                    name=row["name"],
                    material=row["material"],
                    acquisition_date=datetime.strptime(
                        row["acquisition_date"], "%Y-%m-%d"
                    ).date(),
                    origin=row["origin"]
                )
