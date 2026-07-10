import random

def find_subjects_by_faculty(
        subjects,
        faculty_id
):

    faculty_subjects = subjects[
        subjects["faculty_id"] == faculty_id
    ]

    return list(
        faculty_subjects["subject_name"]
    )


def find_affected_slots(
        timetable,
        faculty_subjects,
        absent_day
):

    affected_slots = []

    for class_id, schedule in timetable.items():

        for day, periods in schedule.items():

            if day != absent_day:
                continue

            for period_no, subject in enumerate(periods):

                if subject in faculty_subjects:

                    affected_slots.append(
                        (
                            class_id,
                            day,
                            period_no + 1,
                            subject
                        )
                    )

    return affected_slots

def reschedule_affected_slots(
        timetable,
        affected_slots
):

    updated_timetable = timetable.copy()

    for class_id, day, period, subject in affected_slots:

        updated_timetable[
            class_id
        ][day][period - 1] = "FREE"

    return updated_timetable