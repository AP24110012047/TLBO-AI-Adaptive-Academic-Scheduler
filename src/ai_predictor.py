import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def load_attendance_data():

    attendance = pd.read_csv(
        "../data/faculty_attendance.csv"
    )

    return attendance


def display_attendance_data():

    attendance = load_attendance_data()

    print("\nFACULTY ATTENDANCE DATA")
    print("=" * 50)

    print(attendance)


def train_attendance_model():

    attendance = load_attendance_data()

    day_mapping = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5
    }

    attendance["day_num"] = (
        attendance["day_of_week"]
        .map(day_mapping)
    )

    attendance["faculty_num"] = (
        attendance["faculty_id"]
        .str.replace("F", "")
        .astype(int)
    )

    X = attendance[
        ["faculty_num", "day_num"]
    ]

    y = attendance[
        "attendance"
    ]

    model = RandomForestClassifier(
        n_estimators=50,
        random_state=42
    )

    model.fit(X, y)

    return model

def predict_attendance(
        model,
        faculty_id,
        day
):

    day_mapping = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5
    }

    faculty_num = int(
        faculty_id.replace("F", "")
    )

    prediction = model.predict(
        [[faculty_num,
          day_mapping[day]]]
    )

    return prediction[0]