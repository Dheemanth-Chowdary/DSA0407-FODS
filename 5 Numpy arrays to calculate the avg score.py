import numpy as np

student_scores = np.array([
    [85, 90, 88, 78],
    [92, 89, 78, 85],
    [80, 85, 90, 88],
    [75, 82, 95, 79],
    [88, 92, 84, 90],
    [78, 85, 88, 92],
    [90, 88, 92, 85],
    [85, 78, 90, 88],
    [92, 89, 78, 85],
    [80, 85, 90, 88],
    [75, 82, 95, 79],
    [88, 92, 84, 90],
    [78, 85, 88, 92],
    [90, 88, 92, 85],
    [85, 78, 90, 88]
])

print(student_scores)
average_scores_per_subject = np.mean(student_scores, axis=0)

subject_with_highest_average = np.argmax(average_scores_per_subject)

print("Average score for each subject:")
print(average_scores_per_subject)

print("\nSubject with the highest average score:", subject_with_highest_average)
