from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
