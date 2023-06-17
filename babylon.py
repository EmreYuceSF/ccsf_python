def close_enough(x: float, y: float, maximum_allowable_difference: float) -> bool:
    """This Function returns boolean,
    checks  if 2 values are close enough as user wanted
    x, y are the 2 floats and maximum_allowable_difference
    is the precision expected by user"""
    return abs(x - y) < maximum_allowable_difference


def babylonian_square_root(N: float, estimate: float, precision: float) -> float:
    """This function finds square root with ancient babylonian way.
    finds new estimates with the formula till new estimates and the old estimate close enough.
    """
    new_estimate = (estimate + (N / estimate)) / 2  # formula to find new_estimate
    while not close_enough(new_estimate, estimate, precision):
        estimate = new_estimate
        new_estimate = (estimate + (N / estimate)) / 2
    return new_estimate


number = 101
estimate = 2
presicion = 1 / 10**5
square_root = babylonian_square_root(number, estimate, presicion)
print("\n**********************")
print(f"Square root of {number} is {square_root:.4f}")
print("**********************")
how_close = square_root**2 / number
if 1 - presicion < how_close < 1 + presicion:  # checks if result is correct!
    print("Calculation is right")
print("**********************\n")
