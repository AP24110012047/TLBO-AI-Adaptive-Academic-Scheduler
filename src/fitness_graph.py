import matplotlib.pyplot as plt

fitness = [
    576,576,576,576,576,576,
    574,574,554,550,
    546,546,526,526,
    504,504,504,486,484,484
]

iterations = list(range(1,21))

plt.figure(figsize=(6,4))
plt.plot(iterations, fitness, marker='o')
plt.xlabel("Iteration")
plt.ylabel("Best Fitness Score")
plt.title("Fitness Score Across TLBO Iterations")
plt.grid(True)

plt.savefig("fitness_graph.png", dpi=300, bbox_inches="tight")
plt.show()