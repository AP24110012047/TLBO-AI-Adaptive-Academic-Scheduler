import random
import copy
def generate_population(
        population_size,
        classes,
        subjects,
        timetable_generator
):

    population = []

    for _ in range(population_size):

        timetable = timetable_generator(
            classes,
            subjects
        )

        population.append(timetable)

    return population

def evaluate_population(
        population,
        subjects,
        subject_faculty_map,
        fitness_function
):

    scores = []

    for timetable in population:

        fitness = fitness_function(
            timetable,
            subjects,
            subject_faculty_map
        )

        scores.append(fitness)

    return scores

def select_teacher(
        population,
        fitness_scores
):

    best_index = fitness_scores.index(
        min(fitness_scores)
    )

    return (
        population[best_index],
        fitness_scores[best_index]
    )

def teacher_phase(
        population,
        fitness_scores,
        teacher
):

    new_population = []

    for timetable in population:

        if timetable == teacher:

            new_population.append(
                timetable
            )

            continue

        candidate = copy.deepcopy(
            timetable
        )

        class_id = random.choice(
            list(candidate.keys())
        )

        day = random.choice(
            list(candidate[class_id].keys())
        )

        candidate[class_id][day] = copy.deepcopy(
            teacher[class_id][day]
        )

        new_population.append(
            candidate
        )

    return new_population

def teacher_phase_selection(
        old_population,
        new_population,
        subjects,
        subject_faculty_map,
        fitness_function
):

    final_population = []

    for old_tt, new_tt in zip(
            old_population,
            new_population
    ):

        old_fitness = fitness_function(
            old_tt,
            subjects,
            subject_faculty_map
        )

        new_fitness = fitness_function(
            new_tt,
            subjects,
            subject_faculty_map
        )

        if new_fitness < old_fitness:

            final_population.append(
                new_tt
            )

        else:

            final_population.append(
                old_tt
            )

    return final_population

def learner_phase(
        population,
        fitness_scores
):

    import random
    import copy

    new_population = []

    for i, timetable in enumerate(population):

        candidate = copy.deepcopy(
            timetable
        )

        partner_index = random.randint(
            0,
            len(population) - 1
        )

        while partner_index == i:

            partner_index = random.randint(
                0,
                len(population) - 1
            )

        partner = population[
            partner_index
        ]

        if fitness_scores[
            partner_index
        ] < fitness_scores[i]:

            class_id = random.choice(
                list(candidate.keys())
            )

            day = random.choice(
                list(candidate[class_id].keys())
            )

            candidate[class_id][day] = (
                copy.deepcopy(
                    partner[class_id][day]
                )
            )

        new_population.append(
            candidate
        )

    return new_population

def mutation_phase(
        population,
        mutation_rate=0.2
):

    import random
    import copy

    mutated_population = []

    for timetable in population:

        candidate = copy.deepcopy(
            timetable
        )

        if random.random() < mutation_rate:

            class_id = random.choice(
                list(candidate.keys())
            )

            day = random.choice(
                list(candidate[class_id].keys())
            )

            periods = candidate[
                class_id
            ][day]

            p1 = random.randint(
                0,
                len(periods) - 1
            )

            p2 = random.randint(
                0,
                len(periods) - 1
            )

            periods[p1], periods[p2] = (
                periods[p2],
                periods[p1]
            )

        mutated_population.append(
            candidate
        )

    return mutated_population

def run_tlbo(
        population_size,
        iterations,
        classes,
        subjects,
        subject_faculty_map,
        timetable_generator,
        fitness_function
):

    population = generate_population(
        population_size,
        classes,
        subjects,
        timetable_generator
    )

    best_history = []

    for iteration in range(iterations):

        fitness_scores = evaluate_population(
            population,
            subjects,
            subject_faculty_map,
            fitness_function
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

        population = teacher_phase_selection(
            population,
            teacher_population,
            subjects,
            subject_faculty_map,
            fitness_function
        )

        fitness_scores = evaluate_population(
            population,
            subjects,
            subject_faculty_map,
            fitness_function
        )

        learner_population = learner_phase(
            population,
            fitness_scores
        )

        population = teacher_phase_selection(
            population,
            learner_population,
            subjects,
            subject_faculty_map,
            fitness_function
        )

        mutation_population = mutation_phase(
            population,
            mutation_rate=0.2
        )

        population = teacher_phase_selection(
            population,
            mutation_population,
            subjects,
            subject_faculty_map,
            fitness_function
    )

        fitness_scores = evaluate_population(
            population,
            subjects,
            subject_faculty_map,
            fitness_function
        )

        best_history.append(
            min(fitness_scores)
        )

        print(
            f"Iteration {iteration+1} "
            f"Best Fitness = {min(fitness_scores)}"
        )

    return (
        population,
        best_history
    )