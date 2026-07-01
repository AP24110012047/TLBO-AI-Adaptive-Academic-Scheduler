from data_loader import load_data, display_summary
from fitness import (
    calculate_fitness,
    count_subject_frequency_violations
)
from ai_predictor import (
    display_attendance_data,
    train_attendance_model,
    predict_attendance
)
from adaptive_scheduler import (
    find_subjects_by_faculty,
    find_affected_slots,
    reschedule_affected_slots
)
from tlbo import (
    generate_population,
    evaluate_population,
    select_teacher,
    teacher_phase,
    teacher_phase_selection,
    learner_phase,
    run_tlbo,
    mutation_phase
)
from timetable_generator import create_subject_faculty_map
from timetable_generator import (
    generate_random_timetable,
    display_timetable
)
from constraints import (
    lab_constraint_violations,
    faculty_clash_violations
)


def main():

    faculty, classes, rooms, subjects = load_data()

    display_summary(
        faculty,
        classes,
        rooms,
        subjects
    )

    timetable = generate_random_timetable(
        classes,
        subjects
    )

    display_timetable(timetable)

    subject_faculty_map = create_subject_faculty_map(
    subjects
    )

    print("\nSUBJECT FACULTY MAP")
    print(subject_faculty_map)

    subject_violations = count_subject_frequency_violations(
        timetable,
        subjects
    )

    lab_v = lab_constraint_violations(
        timetable
    )

    faculty_v = faculty_clash_violations(
        timetable,
        subject_faculty_map
    )

    print("\nCONSTRAINT REPORT")
    print("=" * 50)
    print("SUBJECT VIOLATIONS :", subject_violations)
    print("LAB VIOLATIONS     :", lab_v)
    print("FACULTY CLASHES    :", faculty_v)

    fitness = calculate_fitness(
    timetable,
    subjects,
    subject_faculty_map
    )

    print("\n")
    print("=" * 50)
    print(f"FITNESS SCORE : {fitness}")
    print("=" * 50)

    print("\n")
    print("=" * 50)
    print("TLBO POPULATION TEST")
    print("=" * 50)

    population = generate_population(
        10,
        classes,
        subjects,
        generate_random_timetable
    )

    fitness_scores = evaluate_population(
        population,
        subjects,
        subject_faculty_map,
        calculate_fitness
    )

    teacher, best_fitness = select_teacher(
        population,
        fitness_scores
    )

    teacher_population = teacher_phase(
        population,
        fitness_scores,
        teacher
    )

    improved_population = teacher_phase_selection(
        population,
        teacher_population,
        subjects,
        subject_faculty_map,
        calculate_fitness
    )

    new_scores = evaluate_population(
        improved_population,
        subjects,
        subject_faculty_map,
        calculate_fitness
    )

    print("\nAFTER TEACHER PHASE")
    print("=" * 50)
    print("New Fitness Scores :", new_scores)
    print("Best Fitness       :", min(new_scores))

    learner_population = learner_phase(
        improved_population,
        new_scores
    )

    final_population = teacher_phase_selection(
        improved_population,
        learner_population,
        subjects,
        subject_faculty_map,
        calculate_fitness
    )

    final_scores = evaluate_population(
        final_population,
        subjects,
        subject_faculty_map,
        calculate_fitness
    )

    print("\nAFTER LEARNER PHASE")
    print("=" * 50)
    print("Final Fitness Scores :", final_scores)
    print("Best Fitness         :", min(final_scores))

    print("Population Size :", len(population))
    print("Fitness Scores  :", fitness_scores)
    print("Best Fitness    :", best_fitness)

    print("\n")
    print("=" * 50)
    print("FULL TLBO RUN")
    print("=" * 50)

    final_population, history = run_tlbo(
        population_size=10,
        iterations=20,
        classes=classes,
        subjects=subjects,
        subject_faculty_map=subject_faculty_map,
        timetable_generator=generate_random_timetable,
        fitness_function=calculate_fitness
    )

    print("\nFitness History")
    print(history)
    display_attendance_data()
    print("\nTRAINING MODEL...")
    model = train_attendance_model()
    print("MODEL TRAINED")

    prediction = predict_attendance(
        model,
        "F3",
        "Tuesday"
    )

    print("\nATTENDANCE PREDICTION")
    print("=" * 50)

    if prediction == 1:

        print("F3 predicted PRESENT")

    else:

        print("F3 predicted ABSENT")

    faculty_subjects = find_subjects_by_faculty(
        subjects,
        "F3"
    )

    print("\nSUBJECTS TAUGHT BY F3")
    print("=" * 50)
    print(faculty_subjects)

    affected_slots = find_affected_slots(
        timetable,
        faculty_subjects
    )

    print("\nAFFECTED SLOTS")
    print("=" * 50)

    for slot in affected_slots:

        print(slot)

    adapted_timetable = reschedule_affected_slots(
        timetable,
        affected_slots
    )

    print("\nADAPTIVE RESCHEDULING COMPLETED")
    print("=" * 50)

    print(
        "Affected slots replaced with FREE periods"
    )

if __name__ == "__main__":
    main()