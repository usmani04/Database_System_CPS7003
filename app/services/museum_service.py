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

    def get_top_exhibits(self):
        return self.dal.visit_counts_per_exhibit()

    def get_visitors_by_country(self):
        return self.dal.visitors_by_country()

    def close(self):
        self.dal.close()
