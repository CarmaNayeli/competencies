from models import Course
from catalog import CourseCatalog
from exceptions import CourseNotFoundError

def main():
    catalog = CourseCatalog()
    catalog.load_from_file("catalog.json")

    while True:
        print("\n--- University Course Management System ---")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Find Prerequisites")
        print("4. Save & Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            code = input("Course code: ").upper()
            name = input("Course name: ")
            prereq_input = input("Prerequisites (comma-separated codes): ").upper()
            prerequisites = [p.strip() for p in prereq_input.split(',')] if prereq_input else []
            try:
                for pre in prerequisites:
                    catalog.get_course(pre)
                course = Course(code, name, prerequisites)
                catalog.add_course(course)
                print("Course added.")
            except CourseNotFoundError as e:
                print(f"Error: {e}")

        elif choice == '2':
            for course in catalog.list_courses():
                print(course)

        elif choice == '3':
            code = input("Enter course code: ").upper()
            try:
                prereqs = catalog.find_all_prerequisites(code)
                print("All prerequisites:", ", ".join(prereqs) if prereqs else "None")
            except CourseNotFoundError as e:
                print(f"Error: {e}")

        elif choice == '4':
            catalog.save_to_file("catalog.json")
            print("Catalog saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
