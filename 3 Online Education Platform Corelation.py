import pandas as pd
data = {'Student_ID': [1, 2, 3, 4, 5, 6],
        'Course': ['Math', 'Math', 'Physics', 'Physics', 'English', 'English'],
        'Score': [90, 85, 78, 80, 95, 92],
        'Hours_Studied': [10, 12, 8, 10, 15, 14]}

student_data = pd.DataFrame(data)

correlation_by_course = student_data.groupby('Course').apply(lambda x: x['Hours_Studied'].corr(x['Score']))
print(correlation_by_course)

correlations = student_data.groupby('Course').corr().loc[:, 'Hours_Studied']['Score']

strongest_correlation_course = correlations.idxmax()
strongest_correlation_value = correlations.max()

weakest_correlation_course = correlations.idxmin()
weakest_correlation_value = correlations.min()

print(f"The course with the strongest correlation is '{strongest_correlation_course}' with a correlation value of {strongest_correlation_value:.2f}.")
print(f"The course with the weakest correlation is '{weakest_correlation_course}' with a correlation value of {weakest_correlation_value:.2f}.")
