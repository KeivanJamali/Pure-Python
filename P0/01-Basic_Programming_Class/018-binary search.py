def search_binary(xs, target):
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:  # If region of interest (ROI) becomes empty
            return -1
        mid_index = (lb + ub) // 2  # Next probe should be in the middle of the ROI
        item_at_mid = xs[mid_index]  # Fetch the item at that position
        if item_at_mid == target:
            return mid_index  # Found it!
        if item_at_mid < target:
            lb = mid_index + 1  # Use upper half of ROI next time
        else:
            ub = mid_index


def search_binary_recursive(xs, target, lb, ub):
    if lb == ub:
        return -1
    mid_index = (lb + ub) // 2
    item_at_mid = xs[mid_index]
    if item_at_mid == target:
        return mid_index
    if item_at_mid < target:
        return search_binary_recursive(xs, target, mid_index + 1, ub)
    else:
        return search_binary_recursive(xs, target, lb, mid_index)


def jaigasht(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
    ag = jaigasht(s[1:])
    for w in ag:
        for pos in range(len(w) + 1):
            t = w[:pos] + s[0] + w[pos:]
            result.append(t)
    return result
