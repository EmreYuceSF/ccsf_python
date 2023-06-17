def close_enough(x: float, y: float, maximum_allowable_difference: float) -> bool:
    """Checks if two values are close enough within a specified precision.

    Args:
        x (float): The first value.
        y (float): The second value.
        maximum_allowable_difference (float): The maximum allowable difference between the values.

    Returns:
        bool: True if the values are close enough, False otherwise.
    """
    return abs(x - y) < maximum_allowable_difference


def babylonian_square_root(N: float, estimate: float, precision: float) -> float:
    """Calculates the square root of a given number using the Babylonian method.

    Args:
        N (float): The number for which the square root is to be calculated.
        estimate (float): The initial estimate for the square root.
        precision (float): The desired precision or maximum allowable difference between the estimates.

    Returns:
        float: The calculated square root.
    """
    new_estimate = (estimate + (N / estimate)) / 2

    while not close_enough(new_estimate, estimate, precision):
        estimate = new_estimate
        new_estimate = (estimate + (N / estimate)) / 2

    return new_estimate


number = 101
estimate = 2
precision = 1 / 10**5

square_root = babylonian_square_root(number, estimate, precision)
print("\n**********************")
print(f"Square root of {number} is {square_root:.4f}")
print("**********************")

how_close = square_root**2 / number
if 1 - precision < how_close < 1 + precision:  # crosscheck
    print("Calculation is correct")

print("**********************\n")
