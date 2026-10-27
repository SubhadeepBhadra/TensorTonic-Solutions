from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    mean = float(np.mean(x))
    median = float(np.median(x))

    counts = Counter(x)

    max_count = max(counts.values())
    mode = min(key for key, value in counts.items()
               if value == max_count)

    return {
        "mean": mean,
        "median": median,
        "mode": float(mode)
    }
    pass