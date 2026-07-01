import random


DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

PERIODS = 6


def generate_random_timetable(classes, subjects):

    timetable = {}

    for class_id in classes["class_id"]:

        class_subjects = subjects[
            subjects["class_id"] == class_id
        ]["subject_name"].tolist()

        timetable[class_id] = {}

        for day in DAYS:

            timetable[class_id][day] = []

            for _ in range(PERIODS):

                subject = random.choice(class_subjects)

                timetable[class_id][day].append(subject)

    return timetable

def display_timetable(timetable):

    for class_id, schedule in timetable.items():

        print("\n" + "=" * 50)
        print(class_id)
        print("=" * 50)

        for day, periods in schedule.items():

            print(f"\n{day}")

            for i, subject in enumerate(periods):

                print(f"P{i+1} -> {subject}")

def create_subject_faculty_map(subjects):

    mapping = {}

    for _, row in subjects.iterrows():

        mapping[row["subject_name"]] = row["faculty_id"]

    return mapping