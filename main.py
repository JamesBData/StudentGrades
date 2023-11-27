import numpy as np


names = ["Adam", "Anna", "James", "Corey", "Alisha", "Jodie", "John"]
math_grades = np.array([11, 12, 11, 7, 9.5, 15, 18])
science_grades = np.array([9, 11, 18, 15.5, 12, 18.5, 15.5])
reading_grades = np.array([16, 8.5, 11.5, 11, 10.5, 7, 11])
history_grades = np.array([13.5, 10, 9, 14, 14, 12, 7.5])

mean_grades = np.mean([math_grades, science_grades, reading_grades, history_grades], axis=1)


median_math = np.median(math_grades)


history_counts = {}
for grade in history_grades:
    if grade in history_counts:
        history_counts[grade] += 1
    else:
        history_counts[grade] = 1

mode_history_result = max(history_counts, key=history_counts.get)
mode_history = mode_history_result if history_counts[mode_history_result] > 1 else "No mode"

print("Mean for each subject:", mean_grades)
print("Median grade in Math:", median_math)
print("Mode for History:", mode_history)


grades = np.array([math_grades, science_grades, reading_grades, history_grades])
correlation_matrix = np.corrcoef(grades)
subjects = ["Math", "Science", "Reading", "History"]
max_correlation = 0
strongest_correlation = ()

for i in range(len(subjects)):
    for j in range(i + 1, len(subjects)):
        correlation = correlation_matrix[i, j]
        if abs(correlation) > max_correlation:
            max_correlation = abs(correlation)
            strongest_correlation = (subjects[i], subjects[j])

print(f"Strongest correlation: {strongest_correlation[0]} and {strongest_correlation[1]}")


def desc_stats(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    unique, counts = np.unique(numbers, return_counts=True)
    mode_counts = dict(zip(unique, counts))
    mode_result = max(mode_counts, key=mode_counts.get)
    mode = mode_result if mode_counts[mode_result] > 1 else "No mode"
    minimum = np.min(numbers)
    maximum = np.max(numbers)
    data_range = np.ptp(numbers)
    variance = np.var(numbers)
    std_dev = np.std(numbers)

    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Range: {data_range}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")


exam_scores = [24, 5, 15, 60, 54, 82, 99, 80, 70, 98, 93, 60, 33, 22, 65, 61, 51, 58, 83, 86, 42, 67, 60]
print("\n=== Exam Scores ===")
desc_stats(exam_scores)
