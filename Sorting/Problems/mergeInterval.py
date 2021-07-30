from typing import List, Any


def merge(intervals):
    intervals.sort(key=lambda arr: arr[0])
    merged: list[Any] = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
