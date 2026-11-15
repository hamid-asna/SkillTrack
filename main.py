
# SkillTrack - Main Application

# Course Information
course_name = "Python for Data Engineering"
total_lessons = 60
completed_lessons = 12
study_hours = 18

# Calculate Progress


def calculate_progress(completed, total):
    if total == 0:
        return 0

    return (completed / total) * 100


# Determine Course Status
def get_course_status(progress):
    if progress == 100:
        return "Completed"
    elif progress >= 50:
        return "In Progress"
    else:
        return "Just Started"


# Display Course Information
def show_course_info():
    progress = calculate_progress(
        completed_lessons,
        total_lessons
    )

    status = get_course_status(progress)

    print("\n===== SKILLTRACK =====")
    print(f"Course: {course_name}")
    print(f"Total Lessons: {total_lessons}")
    print(f"Completed Lessons: {completed_lessons}")
    print(f"Study Hours: {study_hours}")
    print(f"Progress: {progress:.1f}%")  # .1f means one decimal number
    print(f"Status: {status}")
    print("======================\n")


# Run Application
show_course_info()


# ==========================================
# SkillTrack - Course Management
# Version: 0.2
# ==========================================


# Initial course list
courses = [
    "Python for Data Engineering",
    "Machine Learning",
    "Advanced SQL",
    "Database"
]

# Available course statuses
COURSE_STATUSES = (
    "Not Started",
    "In Progress",
    "Completed"
)


# Display all courses
def show_courses(course_list):
    print("\n===== YOUR COURSES =====")

    if not course_list:
        print("No courses found.")
        return

    for index, course in enumerate(course_list, start=1):
        print(f"{index}. {course}")

    print("========================")


# Add a new course
def add_course(course_list, course_name):
    course_name = course_name.strip()

    if not course_name:
        print("Course name cannot be empty.")
        return

    if course_name in course_list:
        print("This course already exists.")
        return

    course_list.append(course_name)
    print(f"'{course_name}' added successfully.")


# Remove an existing course
def remove_course(course_list, course_name):
    course_name = course_name.strip()

    if course_name not in course_list:
        print("Course not found.")
        return

    course_list.remove(course_name)
    print(f"'{course_name}' removed successfully.")

# Show the last two courses


def show_recent_courses(course_list):
    recent_courses = course_list[-2:]

    print("\n===== RECENT COURSES =====")

    for course in recent_courses:
        print(course)


# Sort courses alphabetically
def sort_courses(course_list):
    course_list.sort()

    print("\nCourses sorted successfully!")
    show_courses(course_list)


# Show courses with long names
def show_long_courses(course_list):
    long_courses = [
        course for course in course_list
        if len(course) > 6
    ]

    print("\n===== LONG COURSE NAMES =====")
    show_courses(long_courses)


def filter_courses_by_length(course_list, minimum_length):

    filtered_courses = list(
        filter(
            lambda course: len(course) >= minimum_length,
            course_list
        )
    )

    if not filtered_courses:
        print("No matching courses found.")
        return

    print("\n===== FILTERED COURSES =====")
    show_courses(filtered_courses)


def show_course_statuses():
    print("\n===== AVAILABLE STATUSES =====")

    for index, status in enumerate(COURSE_STATUSES, start=1):
        print(f"{index}. {status}")

# Main application


def main():
    while True:
        print("\n===== SKILLTRACK =====")
        print("1. Show courses")
        print("2. Add a course")
        print("3. Remove a course")
        print("4. Exit")
        print("5. Sort courses")
        print("6. Show recent courses")
        print("7. Show long course names")
        print("8. Filter courses by name length")
        print("9. show available course statuses")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_courses(courses)

        elif choice == "2":
            course_name = input("Enter course name: ")
            add_course(courses, course_name)

        elif choice == "3":
            course_name = input("Enter course name to remove: ")
            remove_course(courses, course_name)

        elif choice == "4":
            print("Thank you for using SkillTrack!")
            break

        elif choice == "5":
            sort_courses(courses)

        elif choice == "6":
            show_recent_courses(courses)

        elif choice == "7":
            show_long_courses(courses)

        elif choice == "8":
            minimum_length = int(input("Minimum name length: "))
            filter_courses_by_length(courses, minimum_length)
        elif choice == "9":
            show_course_statuses()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

# List comprehension
# temp = [
#     # expression for item in iterable if condition
#     "🐍" for course in courses
#     if len(course) > 6
# ]
# print(temp)
# map ==> on every element will be applied
mapped = list(map(
    str.upper,
    courses
))
print(mapped)

# filter ==> on specific(filtered) elements in the iterable will be applied
# lambda arguments: expression
long_course = list(
    filter(
        lambda course: len(course) > 6, courses
    )
)
print(long_course)

# we must use comma , for indicating Python that we want to use tuples
course = ("Python",)
course = "Python",  # also this is valid
# course_list = list(course_tuple) convert to list or tuple ==> tuple()
print(type(course))
