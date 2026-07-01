def lab_constraint_violations(timetable):

    violations = 0

    for class_id, schedule in timetable.items():

        for day, periods in schedule.items():

            for i, subject in enumerate(periods):

                if "_LAB" in subject:

                    if i == len(periods) - 1:

                        violations += 1

                    elif periods[i + 1] != subject:

                        violations += 1

    return violations


def faculty_clash_violations(
        timetable,
        subject_faculty_map
):

    violations = 0

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]

    periods = 6

    for day in days:

        for period in range(periods):

            faculty_used = []

            for class_id in timetable:

                subject = timetable[class_id][day][period]

                faculty = subject_faculty_map.get(subject)

                if faculty in faculty_used:

                    violations += 1

                else:

                    faculty_used.append(faculty)

    return violations