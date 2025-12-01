from bright_functions import *

def main_menu(student_details, student_courses):
    prompt = """
        1 => Enter details
        2 => Add more courses
        3 => remove courses
        4 => update details
        5 => number of student
        6 => student database
        7 => check a student subject
        8 => check a student zip
        9 => check a student city
        0 => Exit
    """
    print(prompt)

    menu = input("Enter any choice from above: ")

    for index, value in enumerate(student_courses):
        print(f"{value} | ", end="")
    print("")

    match menu:
        case "1":
            course_set = []
            print("  FORM TO FILL  ")
            name = ""
            age = 0
            while name.strip() == "" or age < 0:
                name = input("Enter your name: ").lower()
                age = int(input("Enter your age: "))
                if name.strip() == "":
                    print("Invalid input: enter valid name")
                if age < 0:
                    print("Invalid input: enter valid age")

            courses = ""
            while courses != "1":
                courses = input("Enter your course of choice or enter 1 to stop: ").strip().lower()
                if courses != "1":
                    course_set.append(courses)

            city = input("Enter your address (city): ").lower()
            zip_codes = int(input("Enter zip code: "))

            student_details = create_details(student_details, student_courses, name, age, course_set, city, zip_codes)
            print(student_details)
            main_menu(student_details, student_courses)

        case "2":
            print()
            name = input("Enter your name: ").lower()
            add_course_name = input("Enter more courses: ").strip().lower()
            student_details = add_course(student_details, student_courses, name, add_course_name)
            print(student_details)
            main_menu(student_details, student_courses)

        case "3":
            print()
            name = input("Enter your name: ").lower()
            remove_course_name = input("Enter course you want to remove: ").strip().lower()
            student_details = remove_course(student_details, name, remove_course_name)
            print(student_details)
            main_menu(student_details, student_courses)

        case "4":
            print()
            name = input("Enter your previous name: ").lower()
            change_name = input("Enter your correct name: ").lower()
            age = int(input("Enter your previous age: "))
            change_age = int(input("Enter your correct age: "))
            city = input("Enter your previous address (city): ").lower()
            change_city = input("Enter your correct address (city): ").lower()
            zip_codes = int(input("Enter previous zip code: "))
            change_zip_codes = int(input("Enter correct zip code: "))

            student_details = update_details(student_details, name, change_name, age, change_age, city, change_city, zip_codes, change_zip_codes)
            print(student_details)
            main_menu(student_details, student_courses)

        case "5":
            print()
            student_count = number_of_student(student_details)
            print(student_count)
            main_menu(student_details, student_courses)

        case "6":
            print()
            name = input("Enter student name: ").lower()
            details = student_records(student_details, name)
            print(details)
            main_menu(student_details, student_courses)

        case "7":
            print()
            name = input("Enter student name: ").lower()
            student_subject = get_student_courses(student_details, name)
            print("".join(student_subject))
            main_menu(student_details, student_courses)

        case "8":
            print()
            name = input("Enter student name: ").lower()
            get_zip = get_student_zip(student_details, name)
            print(get_zip)
            main_menu(student_details, student_courses)

        case "9":
            print()
            name = input("Enter student name: ").lower()
            get_city = get_student_city(student_details, name)
            print(get_city)
            main_menu(student_details, student_courses)

        case "0":
            print("Exiting...")

        case _:
            print("Invalid input")
            main_menu(student_details, student_courses)


def main():
    student_details = {}
    student_courses = [
        "math", "physics", "computer science", "biology", "chemistry", "statistics",
        "english", "economics", "history", "philosophy", "sociology", "political science",
        "geography", "psychology", "art", "music", "engineering", "law", "medicine", "business"
    ]
    main_menu(student_details, student_courses)


main()
