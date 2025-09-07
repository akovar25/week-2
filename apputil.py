import numpy as np

def ways(n, coin_types=[1, 5]):
    #Add helper function for recursion
    def helper(n, idx):
        #Base cases, if n is 0, we found a way, if n<0 or no coins left, no way
        if n == 0:
            return 1
        if n < 0 or idx < 0:
            return 0
        # Use coin_types[idx] or skip to next smaller coin
        return helper(n - coin_types[idx], idx) + helper(n, idx - 1)
    #Initial call with full amount and largest coin index
    return helper(n, len(coin_types) - 1)

def lowest_score(names, scores):
        # Return name with lowest score
        return names[np.argmin(scores)]

def sort_names(names, scores):
     # Return names sorted by descending scores
     sorted_indices = np.argsort(scores)[::-1]  # reverse for descending order
    return names[sorted_indices]