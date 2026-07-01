from constraints import (
    lab_constraint_violations,
    faculty_clash_violations
)
def count_subject_frequency_violations(
        timetable,
        subjects
):

    violations = 0

    for class_id, schedule in timetable.items():

        required_hours = {}

        class_subjects = subjects[
            subjects["class_id"] == class_id
        ]

        for _, row in class_subjects.iterrows():

            required_hours[
                row["subject_name"]
            ] = row["hours_per_week"]

        actual_hours = {}

        for day in schedule:

            for subject in schedule[day]:

                actual_hours[subject] = (
                    actual_hours.get(subject, 0) + 1
                )

        for subject, required in required_hours.items():

            actual = actual_hours.get(subject, 0)

            violations += abs(
                actual - required
            )

    return violations

def calculate_fitness(
        timetable,
        subjects,
        subject_faculty_map
):

    subject_violations = count_subject_frequency_violations(
        timetable,
        subjects
    )

    lab_violations = lab_constraint_violations(
        timetable
    )

    faculty_violations = faculty_clash_violations(
        timetable,
        subject_faculty_map
    )

    fitness = (
        subject_violations
        +
        (lab_violations * 10)
        +
        (faculty_violations * 20)
    )

    return fitness
