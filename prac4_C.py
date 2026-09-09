def max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum


numbers = [10, 25, 5, 40, 15]

maximum, minimum = max_min(numbers)

print("Maximum value =", maximum)
print("Minimum value =", minimum)