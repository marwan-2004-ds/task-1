import numpy as np
import matplotlib.pyplot as plt

scores = np.random.normal(70, 10, 100)

mean_score = np.mean(scores)
std_score = np.std(scores)
z_scores = (scores - mean_score) / std_score

outliers = (z_scores > 2) | (z_scores < -2)
outliers_values = scores[outliers]

plt.figure(figsize=(8, 4))
plt.scatter(np.ones_like(scores), scores, alpha=0.7)
plt.ylabel("Scores")
plt.title("Dot Plot of Student Exam Scores")
plt.xticks([])
plt.show()

plt.figure(figsize=(8, 4))
plt.hist(scores, bins=10, edgecolor='black', alpha=0.7)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Histogram of Student Exam Scores")
plt.show()

print("Outliers:", outliers_values)
