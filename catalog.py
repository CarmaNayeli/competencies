import json
from typing import List, Dict
from models import Course
from exceptions import CourseNotFoundError

class CourseCatalog:
    def __init__(self):
        self.courses: Dict[str, Course] = {}

    def add_course(self, course: Course):
        self.courses[course.code] = course

    def get_course(self, code: str) -> Course:
        if code not in self.courses:
            raise CourseNotFoundError(f"Course {code} not found.")
        return self.courses[code]

    def list_courses(self):
        return list(self.courses.values())

    def find_all_prerequisites(self, code: str, visited=None) -> List[str]:
        if visited is None:
            visited = set()
        course = self.get_course(code)
        prereqs = []
        for pre in course.prerequisites:
            if pre not in visited:
                visited.add(pre)
                prereqs.append(pre)
                prereqs.extend(self.find_all_prerequisites(pre, visited))
        return list(set(prereqs))

    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            json.dump([c.to_dict() for c in self.courses.values()], f, indent=4)

    def load_from_file(self, filename: str):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for c in data:
                    self.add_course(Course.from_dict(c))
        except FileNotFoundError:
            print("Catalog file not found. Starting with an empty catalog.")
