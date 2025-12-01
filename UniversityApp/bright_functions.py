def create_details(student_details, student_courses, name, age, course_set, city, zip_codes):
    for course in course_set:
        if course not in student_courses:
            raise ValueError("Course  does not exist")
    if type(age) is not int:
        raise TypeError("Age must be an integer")

    student_details[name] = {
        "age": age,
        "courses": list(course_set),
        "city": city,
        "zip_codes": zip_codes
    }
    return student_details


def add_course(student_details, student_courses, name, add_course_name):
    add_course_name = add_course_name.strip().lower()
    if add_course_name not in student_courses:
        raise ValueError("Course does not exist")
    if name not in student_details:
        raise ValueError("Student does not exist")

    if add_course_name not in student_details[name]["courses"]:
        student_details[name]["courses"].append(add_course_name)
    return student_details


def remove_course(student_details, name, remove_course_name):
    remove_course_name = remove_course_name.strip().lower()
    if name not in student_details:
        raise ValueError("Student does not exist")
    if remove_course_name not in student_details[name]["courses"]:
        raise ValueError("Course does not exist for this student")

    student_details[name]["courses"].remove(remove_course_name)
    return student_details


def update_details(student_details, name, change_name, age, change_age, city, change_city, zip_codes, change_zip_codes):
    if name not in student_details:
        raise ValueError("Student does not exist")

    current = student_details[name]
    if age is not None and current["age"] != age:
        raise ValueError("Previous age does not match record")
    if city and current["city"] != city:
        raise ValueError("Previous city does not match record")
    if zip_codes is not None and current["zip_codes"] != zip_codes:
        raise ValueError("Previous zip code does not match record")

    if change_name:
        student_details[change_name] = student_details.pop(name)
        name = change_name
    if change_age is not None:
        student_details[name]["age"] = change_age
    if change_city:
        student_details[name]["city"] = change_city
    if change_zip_codes is not None:
        student_details[name]["zip_codes"] = change_zip_codes

    return student_details


def number_of_student(student_details):
    return len(student_details)


def student_records(student_details, name):
    if name not in student_details:
        raise ValueError("Student does not exist")
    return student_details[name]


def get_student_courses(student_details, name):
    if name not in student_details:
        raise ValueError("Student does not exist")
    return student_details[name]["courses"]


def get_student_zip(student_details, name):
    if name not in student_details:
        raise ValueError("Student does not exist")
    return student_details[name]["zip_codes"]


def get_student_city(student_details, name):
    if name not in student_details:
        raise ValueError("Student does not exist")
    return student_details[name]["city"]
