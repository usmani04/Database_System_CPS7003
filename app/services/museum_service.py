from datetime import date
from db.dal import DataAccessLayer


class MuseumService:
    """
    Business layer:
    - Enforces rules
    - Validates input
    - Applies role-based access
    """

    def __init__(self, user):
        self.user = user
        self.dal = DataAccessLayer()

    # ---------- Admin-only operations ----------

    def create_museum(self, name: str, location: str):
        if self.user.role != "admin":
            raise PermissionError("Only admins can create museums")

        if not name or not location:
            raise ValueError("Museum name and location are required")

        return self.dal.add_museum(name, location)

    def create_exhibit(
        self,
        museum_id: int,
        title: str,
        description: str,
        start_date: date,
        end_date: date
    ):
        if self.user.role != "admin":
            raise PermissionError("Only admins can create exhibits")

        if not title:
            raise ValueError("Exhibit title cannot be empty")

        if start_date > end_date:
            raise ValueError("Start date must be before end date")

        return self.dal.add_exhibit(
            museum_id, title, description, start_date, end_date
        )

    # ---------- Staff/Admin operations ----------

    def update_conservation_status(
        self, record_id: int, condition_status: str
    ):
        if self.user.role not in ("admin", "staff"):
            raise PermissionError("Insufficient privileges")

        return self.dal.update_conservation_status(
            record_id, condition_status
        )

    # ---------- Public operations ----------

    def register_visitor(
        self, full_name: str, age: int, gender: str, country: str
    ):
        if not full_name:
            raise ValueError("Visitor name is required")

        return self.dal.add_visitor(full_name, age, gender, country)
    
    def record_visit(self, visitor_id, exhibit_id, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        return self.dal.add_visit(
            visitor_id, exhibit_id, date.today(), rating
        )

    def get_top_exhibits(self):
        return self.dal.visit_counts_per_exhibit()

    def get_visitors_by_country(self):
        return self.dal.visitors_by_country()

    def list_museums(self):
        return self.dal.list_museums()

    def list_exhibits(self):
        return self.dal.list_exhibits()

    def list_visitors(self):
        return self.dal.list_visitors()

    def list_visits(self):
        return self.dal.list_visits()
    
    # ---------- ADMIN-ONLY UPDATE / DELETE ----------

    def update_museum(self, museum_id, name, location):
        if self.user.role != "admin":
            raise PermissionError("Only admins can update museums")

        return self.dal.update_museum(museum_id, name, location)

    def delete_museum(self, museum_id):
        if self.user.role != "admin":
            raise PermissionError("Only admins can delete museums")

        self.dal.delete_museum(museum_id)

    def update_exhibit(self, exhibit_id, title, description):
        if self.user.role != "admin":
            raise PermissionError("Only admins can update exhibits")

        return self.dal.update_exhibit(exhibit_id, title, description)

    def delete_exhibit(self, exhibit_id):
        if self.user.role != "admin":
            raise PermissionError("Only admins can delete exhibits")

        self.dal.delete_exhibit(exhibit_id)

    # ---------- PUBLIC UPDATE / DELETE ----------

    def update_visitor(self, visitor_id, age, country):
        return self.dal.update_visitor(visitor_id, age, country)

    def delete_visitor(self, visitor_id):
        self.dal.delete_visitor(visitor_id)

    def update_visit(self, visit_id, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        return self.dal.update_visit(visit_id, rating)

    def delete_visit(self, visit_id):
        self.dal.delete_visit(visit_id)

    def close(self):
        self.dal.close()
