import pandas as pd


# Example 1:
#
# Input:
# student_data:
# [
#     [1, 15],
#     [2, 11],
#     [3, 11],
#     [4, 20]
# ]
# Output:
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1 | 15 |
# | 2 | 11 |
# | 3 | 11 |
# | 4 | 20 |
# +------------+-----+
# Explanation:
# A DataFrame was created on top of student_data, with two columns named student_id and age.

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])
