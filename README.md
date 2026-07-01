# TLBO and AI-Based Adaptive Academic Scheduling Framework

## Project Overview

This project presents an **AI-Based Adaptive Academic Scheduling Framework** that combines the **Teaching-Learning-Based Optimization (TLBO)** algorithm with **Machine Learning** to generate optimized academic timetables.

The system automatically generates timetables, evaluates scheduling quality using multiple constraints, optimizes schedules through TLBO, predicts faculty availability using a Random Forest model, and performs adaptive timetable rescheduling when faculty are predicted to be unavailable.

---

## Features

- Automatic timetable generation
- Subject–Faculty mapping
- Constraint validation
- Fitness evaluation
- Teaching-Learning-Based Optimization (TLBO)
- Teacher Phase
- Learner Phase
- Mutation Phase
- Random Forest based faculty attendance prediction
- Adaptive timetable rescheduling
- Performance evaluation using fitness scores

---

## Project Structure

```
adaptive_scheduler/
│
├── data/
│   ├── faculty.csv
│   ├── subjects.csv
│   ├── classes.csv
│   ├── rooms.csv
│   └── faculty_attendance.csv
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── timetable_generator.py
│   ├── constraints.py
│   ├── fitness.py
│   ├── tlbo.py
│   ├── ai_predictor.py
│   └── adaptive_scheduler.py
│
├── requirements.txt
└── README.md
```

---

# Requirements

- Python 3.10 or above
- pip

---

# Installation

### 1. Clone the repository

```bash
git clone https://github.com/AP24110012047/TLBO-AI-Adaptive-Academic-Scheduler.git
```

### 2. Open the project folder

```bash
cd TLBO-AI-Adaptive-Academic-Scheduler
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

---

# Execution

Move to the source directory.

```bash
cd src
```

Run the project.

```bash
python main.py
```

---

# Expected Output

The program performs the following operations:

- Loads academic datasets
- Generates a random timetable
- Displays timetable information
- Evaluates scheduling constraints
- Calculates fitness score
- Performs TLBO optimization
- Displays fitness improvement history
- Predicts faculty attendance
- Detects affected timetable slots
- Performs adaptive timetable rescheduling

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Teaching-Learning-Based Optimization (TLBO)

---

# Future Enhancements

- Dynamic classroom allocation
- Multi-objective optimization
- Web-based dashboard
- Real-time timetable updates
- Automatic substitute faculty allocation

---

# Author

**Jyothsna Lahari Chereddy**

SRM University AP

B.Tech Computer Science and Engineering
