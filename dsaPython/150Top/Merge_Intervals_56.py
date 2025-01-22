from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda i: i[0])
    r = []

    for interval in intervals:
        if not r or r[-1][1] < interval[0]:
            r.append(interval)
        else:
            if r[-1][1] < interval[1]:
                r[-1][1] = interval[1]
    return r


intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals1))
intervals2 = [[1, 4], [4, 5]]
print(merge(intervals2))
