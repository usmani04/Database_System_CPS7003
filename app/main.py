from datetime import date
from services.museum_service import MuseumService
from services.analytics_service import AnalyticsService
from services.csv_import_service import CSVImportService
from security.auth import authenticate_user


def main():
    try:
        user = authenticate_user()
        service = MuseumService(user)

        # NEW: analytics & external integration
        analytics = AnalyticsService(service.dal)
        csv_service = CSVImportService()

        print("\n--- HeritagePlus Museum Management System ---")

        # Admin workflow
        service.create_museum(
            name="HeritagePlus Central Museum",
            location="London"
        )

        service.create_exhibit(
            museum_id=1,
            title="Ancient Civilisations",
            description="Historical artefacts exhibition",
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31)
        )

        # Visitor registration
        service.register_visitor(
            full_name="John Smith",
            age=32,
            gender="Male",
            country="UK"
        )

        service.record_visit(
            visitor_id=1,
            exhibit_id=1,
            rating=5
        )

        # Reports (existing)
        print("\nTop Exhibits:")
        for row in service.get_top_exhibits():
            print(row)

        print("\nVisitors by Country:")
        for row in service.get_visitors_by_country():
            print(row)

        # NEW: analytics output (80–100 requirement)
        print("\nMonthly Visitor Trends:")
        for row in service.dal.monthly_visit_trends():
            print(row)

        print("\nForecasted Next Month Visits:")
        print(analytics.forecast_next_month_visits())

        service.close()

    except PermissionError as e:
        print("Access denied:", e)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
