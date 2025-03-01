# Calculate mean, median, and mode
import statistics

# Data
data = [62000, 64000, 49000, 324000, 1264000, 54330, 64000, 51000, 55000, 48000, 53000]


x = statistics.variance(data)
y = statistics.stdev(data)
z = statistics.pstdev(data)
p = statistics.mean(data)
q = statistics.median(data)
r = statistics.mode(data)
print(f"Variance {x}")
print(f"Standard Deviation {y}")
print(f"Population Standard Deviation {z}")
print(f"Mean {p}")
print(f"Median {q}")
print(f"Mode {r}")