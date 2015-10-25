import numpy as np
rating = np.array([3.41, 3.90, 3.52, 3.36, 3.47, 3.76, 3.55, 3.49, 3.78, 3.86, 3.65, 3.86])
n_students = np.array([65, 10, 68, 28, 61, 12, 60, 20, 64, 10, 6, 96])

print np.size(rating)
print n_students.sum()
print sum(rating * n_students)/sum(n_students)
