import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
engineers = np.random.exponential(80000, 100) + 40000
teachers = np.random.normal(55000, 8000, 100)
artists = np.random.lognormal(10.5, 0.4, 100)



median_engineers = np.median(engineers)
median_teachers = np.median(teachers)
median_artists = np.median(artists)
iqr_engineers = np.percentile(engineers, 75) - np.percentile(engineers, 25)
iqr_teachers = np.percentile(teachers, 75) - np.percentile(teachers, 25)
iqr_artists = np.percentile(artists, 75) - np.percentile(artists, 25)
outliers_engineers = engineers[(engineers < (np.percentile(engineers, 25) - 1.5 * iqr_engineers)) | 
                                (engineers > (np.percentile(engineers, 75) + 1.5 * iqr_engineers))]
outliers_teachers = teachers[(teachers < (np.percentile(teachers, 25) - 1.5 * iqr_teachers)) |
                                (teachers > (np.percentile(teachers, 75) + 1.5 * iqr_teachers))]
outliers_artists = artists[(artists < (np.percentile(artists, 25) - 1.5 * iqr_artists)) |
                                (artists > (np.percentile(artists, 75) + 1.5 * iqr_artists))]

plt.figure(figsize=(12, 6))
plt.boxplot([engineers, teachers, artists], labels=['Engineers', 'Teachers', 'Artists'])
plt.title("Box Plot of Salaries by Profession")
plt.ylabel("Salary ($)")
plt.grid(axis='y')
plt.show()