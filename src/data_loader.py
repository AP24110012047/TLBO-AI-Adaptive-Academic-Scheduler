import pandas as pd


def load_data():
    faculty = pd.read_csv("../data/faculty.csv")
    classes = pd.read_csv("../data/classes.csv")
    rooms = pd.read_csv("../data/rooms.csv")
    subjects = pd.read_csv("../data/subjects.csv")
    
    return faculty, classes, rooms, subjects


def display_summary(faculty, classes, rooms, subjects):
    print("\n===== DATASET SUMMARY =====")

    print(f"Total Faculties : {len(faculty)}")
    print(f"Total Classes   : {len(classes)}")
    print(f"Total Rooms     : {len(rooms)}")
    print(f"Total Subjects  : {len(subjects)}")

    print("\nClasses:")
    print(classes["class_id"].tolist())

    print("\nRoom Types:")
    print(rooms["type"].value_counts())