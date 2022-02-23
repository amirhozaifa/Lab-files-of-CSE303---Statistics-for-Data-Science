def largest_number_2019_3_60_109(a):
    """Finds the largest number in a list."""
    largest = a[0]
    for x in a:
        if x > largest:
            largest = x
    return largest


def smallest_number_2019_3_60_109(a):
    """Finds the smallest number in a list."""
    smallest = a[0]
    for x in a:
        if x < smallest:
            smallest = x
    return smallest


a = [1, 2, 3, 4, 5]
print(largest_number_2019_3_60_109(a))
print(smallest_number_2019_3_60_109(a))