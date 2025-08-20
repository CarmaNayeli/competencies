import unittest
from models import Course
from catalog import CourseCatalog
from exceptions import CourseNotFoundError

class TestCourseCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = CourseCatalog()
        self.catalog.add_course(Course("CS101", "Intro to CS"))
        self.catalog.add_course(Course("CS102", "Data Structures", ["CS101"]))
        self.catalog.add_course(Course("CS103", "Algorithms", ["CS102"]))

    def test_course_retrieval(self):
        course = self.catalog.get_course("CS101")
        self.assertEqual(course.name, "Intro to CS")

    def test_prerequisites(self):
        prereqs = self.catalog.find_all_prerequisites("CS103")
        self.assertIn("CS101", prereqs)
        self.assertIn("CS102", prereqs)

    def test_nonexistent_course(self):
        with self.assertRaises(CourseNotFoundError):
            self.catalog.get_course("CS999")

if __name__ == '__main__':
    unittest.main()
