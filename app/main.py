from datetime import date
from db.dal import DataAccessLayer

dal = DataAccessLayer()

# Create museum
dal.add_museum(
    name="HeritagePlus Central Museum",
    location="London"
)

# Create exhibit (FIX: use date objects)
dal.add_exhibit(
    museum_id=1,
    title="Ancient Civilisations",
    description="Historical artefacts exhibition",
    start_date=date(2024, 1, 1),
    end_date=date(2024, 12, 31)
)

# Create visitor
dal.add_visitor(
    full_name="John Smith",
    age=32,
    gender="Male",
    country="UK"
)

# Demonstrate queries
print("\nExhibits with museums:")
for row in dal.get_exhibits_with_museum():
    print(row)

print("\nVisitors by country:")
for row in dal.visitors_by_country():
    print(row)

print("\nVisit counts per exhibit:")
for row in dal.visit_counts_per_exhibit():
    print(row)

dal.close()
