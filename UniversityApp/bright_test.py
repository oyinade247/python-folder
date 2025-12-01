import unittest
from bright_functions import *

class TestUniversityApp(unittest.TestCase):

    def test_create_details_works(self):
        details = {}
        student_courses = ["maths", "physics"]
        name = "oyin"
        age = 15
        courses = ["maths"]
        city = "ogun"
        zip_codes = 22343

        expected = {"oyin": {"age": 15, "courses": ["maths"], "city": "ogun", "zip_codes": 22343}}
        actual = create_details(details, student_courses, name, age, courses, city, zip_codes)
        self.assertEqual(actual, expected)

    def test_create_details_invalid_course_raises_value_error(self):
        self.assertRaises(ValueError, create_details, {}, ["maths"], "oyin", 15, ["physics"], "ogun", 22343)

    def test_create_details_invalid_age_type_raises_type_error(self):
        self.assertRaises(TypeError, create_details, {}, ["maths"], "oyin", "fifteen", ["maths"], "ogun", 22343)

    def test_add_course_success(self):
        details = create_details({}, ["maths", "physics"], "oyin", 15, ["maths"], "ogun", 22343)
        student_courses = ["maths", "physics"]
        name = "oyin"
        add_course_name = "physics"
        actual = add_course(details, student_courses, name, add_course_name)
        expected = {"oyin": {"age": 15, "courses": ["maths", "physics"], "city": "ogun", "zip_codes": 22343}}
        self.assertEqual(actual, expected)

    def test_add_course_invalid_student_raises_value_error(self):
        self.assertRaises(ValueError, add_course, {}, ["maths"], "oyin", "maths")

    def test_add_course_invalid_course_raises_value_error(self):
        details = create_details({}, ["maths"], "oyin", 15, ["maths"], "ogun", 22343)
        self.assertRaises(ValueError, add_course, details, ["maths"], "oyin", "physics")

    def test_remove_course_success(self):
        details = create_details({}, ["maths", "physics"], "oyin", 15, ["maths", "physics"], "ogun", 22343)
        name = "oyin"
        remove_course_name = "physics"

        actual = remove_course(details, name, remove_course_name)
        expected = {"oyin": {"age": 15, "courses": ["maths"], "city": "ogun", "zip_codes": 22343}}
        self.assertEqual(actual, expected)

    def test_remove_course_invalid_student_raises_value_error(self):
        self.assertRaises(ValueError, remove_course, {}, "oyin", "maths")

    def test_remove_course_invalid_course_raises_value_error(self):
        details = create_details({}, ["maths"], "oyin", 15, ["maths"], "ogun", 22343)
        self.assertRaises(ValueError, remove_course, details, "oyin", "physics")

    def test_update_details_work_as_expected(self):
        details = create_details({}, ["maths"], "oyin", 15, ["maths"], "ogun", 22343)
        actual = update_details(details, "oyin", "oyinbaby", 15, 16, "ogun", "lagos", 22343, 12345)
        expected = {"oyinbaby": {"age": 16, "courses": ["maths"], "city": "lagos", "zip_codes": 12345}}
        self.assertEqual(actual, expected)

    def test_that_student_courses_work_as_expected(self):
        details = create_details({}, ["maths"], "oyin", 15, ["maths"], "ogun", 22343)
        actual = get_student_courses(details, "oyin")
        expected = ["maths"]
        self.assertEqual(actual, expected)

    def test_that_getting_student_zip_codes_work_as_expected(self):
        details = create_details({}, ["maths"], "oyin", 15, ["maths"], "ogun", 22343)
        actual = get_student_zip(details, "oyin")
        expected = 22343
        self.assertEqual(actual, expected)

    def test_that_getting_student_cities_work_as_expected(self):
        details = create_details({}, ["maths"], "oyin", 15, ["maths"], "ogun", 22343)
        actual = get_student_city(details, "oyin")
        expected = "ogun"
        self.assertEqual(actual, expected)


