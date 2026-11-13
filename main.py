
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
