
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
    "Advanced SQL"
]


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


# Main application
def main():
    while True:
        print("\n===== SKILLTRACK =====")
        print("1. Show courses")
        print("2. Add a course")
        print("3. Remove a course")
        print("4. Exit")

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

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
