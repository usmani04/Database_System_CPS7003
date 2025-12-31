from datetime import date
from security.auth import authenticate_user
from services.museum_service import MuseumService
from services.analytics_service import AnalyticsService


SEPARATOR = "-" * 50


# ===================== STARTUP MENU =====================

def startup_menu():
    while True:
        print(f"\n{SEPARATOR}")
        print(" WELCOME TO HERITAGEPLUS ")
        print(" MUSEUM MANAGEMENT SYSTEM ")
        print(SEPARATOR)
        print("1. Login")
        print("2. Exit")

        choice = input("\nSelect an option (1–2): ").strip()

        if choice == "1":
            return True
        elif choice == "2":
            print("\nExiting system. Goodbye!")
            return False
        else:
            print("Invalid option. Please try again.")


# ===================== MAIN MENU =====================

def main_menu(service, analytics):
    while True:
        print(f"\n{SEPARATOR}")
        print(" HERITAGEPLUS – MAIN MENU ")
        print(SEPARATOR)
        print("1. Manage Museums")
        print("2. Manage Exhibits")
        print("3. Manage Visitors")
        print("4. Manage Visits")
        print("5. View Reports")
        print("6. Logout")

        choice = input("\nSelect an option (1–6): ").strip()

        if choice == "1":
            museum_menu(service)
        elif choice == "2":
            exhibit_menu(service)
        elif choice == "3":
            visitor_menu(service)
        elif choice == "4":
            visit_menu(service)
        elif choice == "5":
            report_menu(service, analytics)
        elif choice == "6":
            print("\nLogging out...")
            break
        else:
            print("Invalid option. Please try again.")


# ===================== MUSEUM MENU =====================

def museum_menu(service):
    while True:
        print(f"\n{SEPARATOR}")
        print(" MUSEUM MANAGEMENT ")
        print(SEPARATOR)
        print("1. Create Museum (Admin)")
        print("2. List Museums")
        print("3. Update Museum (Admin)")
        print("4. Delete Museum (Admin)")
        print("5. Back")

        choice = input("\nSelect (1–5): ").strip()

        try:
            if choice == "1":
                name = input("Museum name: ").strip()
                location = input("Location: ").strip()
                service.create_museum(name, location)
                print("✔ Museum created successfully.")

            elif choice == "2":
                museums = service.list_museums()
                if not museums:
                    print("No museums found.")
                for m in museums:
                    print(f"[{m.museum_id}] {m.name} — {m.location}")

            elif choice == "3":
                museum_id = int(input("Museum ID: "))
                name = input("New name: ").strip()
                location = input("New location: ").strip()
                service.update_museum(museum_id, name, location)
                print("✔ Museum updated successfully.")

            elif choice == "4":
                museum_id = int(input("Museum ID: "))
                service.delete_museum(museum_id)
                print("✔ Museum deleted successfully.")

            elif choice == "5":
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print("✖ Error:", e)


# ===================== EXHIBIT MENU =====================

def exhibit_menu(service):
    while True:
        print(f"\n{SEPARATOR}")
        print(" EXHIBIT MANAGEMENT ")
        print(SEPARATOR)
        print("1. Create Exhibit (Admin)")
        print("2. List Exhibits")
        print("3. Update Exhibit (Admin)")
        print("4. Delete Exhibit (Admin)")
        print("5. Back")

        choice = input("\nSelect (1–5): ").strip()

        try:
            if choice == "1":
                museum_id = int(input("Museum ID: "))
                title = input("Title: ").strip()
                description = input("Description: ").strip()
                start_date = date.fromisoformat(input("Start date (YYYY-MM-DD): "))
                end_date = date.fromisoformat(input("End date (YYYY-MM-DD): "))
                service.create_exhibit(
                    museum_id, title, description, start_date, end_date
                )
                print("✔ Exhibit created successfully.")

            elif choice == "2":
                exhibits = service.list_exhibits()
                if not exhibits:
                    print("No exhibits found.")
                for e in exhibits:
                    print(e)

            elif choice == "3":
                exhibit_id = int(input("Exhibit ID: "))
                title = input("New title: ").strip()
                description = input("New description: ").strip()
                service.update_exhibit(exhibit_id, title, description)
                print("✔ Exhibit updated successfully.")

            elif choice == "4":
                exhibit_id = int(input("Exhibit ID: "))
                service.delete_exhibit(exhibit_id)
                print("✔ Exhibit deleted successfully.")

            elif choice == "5":
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print("✖ Error:", e)


# ===================== VISITOR MENU =====================

def visitor_menu(service):
    while True:
        print(f"\n{SEPARATOR}")
        print(" VISITOR MANAGEMENT ")
        print(SEPARATOR)
        print("1. Register Visitor")
        print("2. List Visitors")
        print("3. Update Visitor")
        print("4. Delete Visitor")
        print("5. Back")

        choice = input("\nSelect (1–5): ").strip()

        try:
            if choice == "1":
                full_name = input("Full name: ").strip()
                age = int(input("Age: "))
                gender = input("Gender: ").strip()
                country = input("Country: ").strip()
                service.register_visitor(full_name, age, gender, country)
                print("✔ Visitor registered successfully.")

            elif choice == "2":
                visitors = service.list_visitors()
                if not visitors:
                    print("No visitors found.")
                for v in visitors:
                    print(f"[{v.visitor_id}] {v.full_name}, {v.age}, {v.country}")

            elif choice == "3":
                visitor_id = int(input("Visitor ID: "))
                age = int(input("New age: "))
                country = input("New country: ").strip()
                service.update_visitor(visitor_id, age, country)
                print("✔ Visitor updated successfully.")

            elif choice == "4":
                visitor_id = int(input("Visitor ID: "))
                service.delete_visitor(visitor_id)
                print("✔ Visitor deleted successfully.")

            elif choice == "5":
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print("✖ Error:", e)


# ===================== VISIT MENU =====================

def visit_menu(service):
    while True:
        print(f"\n{SEPARATOR}")
        print(" VISIT MANAGEMENT ")
        print(SEPARATOR)
        print("1. Record Visit")
        print("2. List Visits")
        print("3. Update Visit Rating")
        print("4. Delete Visit")
        print("5. Back")

        choice = input("\nSelect (1–5): ").strip()

        try:
            if choice == "1":
                visitor_id = int(input("Visitor ID: "))
                exhibit_id = int(input("Exhibit ID: "))
                rating = int(input("Rating (1–5): "))
                service.record_visit(visitor_id, exhibit_id, rating)
                print("✔ Visit recorded successfully.")

            elif choice == "2":
                visits = service.list_visits()
                if not visits:
                    print("No visits found.")
                for v in visits:
                    print(v)

            elif choice == "3":
                visit_id = int(input("Visit ID: "))
                rating = int(input("New rating (1–5): "))
                service.update_visit(visit_id, rating)
                print("✔ Visit updated successfully.")

            elif choice == "4":
                visit_id = int(input("Visit ID: "))
                service.delete_visit(visit_id)
                print("✔ Visit deleted successfully.")

            elif choice == "5":
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print("✖ Error:", e)


# ===================== REPORTS =====================

def report_menu(service, analytics):
    print(f"\n{SEPARATOR}")
    print(" REPORTS & ANALYTICS ")
    print(SEPARATOR)

    print("\nTop Exhibits:")
    for row in service.get_top_exhibits():
        print("•", row)

    print("\nVisitors by Country:")
    for row in service.get_visitors_by_country():
        print("•", row)

    print("\nMonthly Visitor Trends:")
    for row in service.dal.monthly_visit_trends():
        print("• Month", row.month, "→", row.visits, "visits")

    print("\nForecasted Next Month Visits:")
    print("•", analytics.forecast_next_month_visits())


# ===================== ENTRY POINT =====================

def main():
    while True:
        if not startup_menu():
            break

        try:
            user = authenticate_user()
            service = MuseumService(user)
            analytics = AnalyticsService(service.dal)

            main_menu(service, analytics)

            service.close()

        except PermissionError as e:
            print("Access denied:", e)
        except Exception as e:
            print("Fatal error:", e)


if __name__ == "__main__":
    main()
