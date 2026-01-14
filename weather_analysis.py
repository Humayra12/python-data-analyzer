# weather_analysis.py
# Analysis functions for hourly temperature time series

import math
import statistics

def compute_min(values):
    return min(values) if values else None


def compute_max(values):
    return max(values) if values else None


def compute_mean(values):
    if not values:
        return None
    return sum(values) / len(values)


def compute_median(values):
    if not values:
        return None
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 1:
        return sorted_vals[mid]
    else:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


def compute_std(values):
    # population standard deviation (simple + fine for this assignment)
    if not values:
        return None
    mean = compute_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


def analyze_time_series(times, temperatures):
    """
    Returns a dictionary of summary stats + original lists.
    """
    return {
        "times": times,
        "temperatures": temperatures,
        "min": compute_min(temperatures),
        "max": compute_max(temperatures),
        "mean": compute_mean(temperatures),
        "median": compute_median(temperatures),
        "std_dev": compute_std(temperatures),
    }
