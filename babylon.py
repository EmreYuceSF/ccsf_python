def close_enough(x: float, y: float, maximum_allowable_difference: float) -> bool:
    """ Returns True if x and y are within maximum_allowable_difference of each other, or False otherwise. """
    # DO NOT CHANGE THIS FUNCTION. CALL IT IN YOUR IMPLEMENTATION OF babylonian_square_root() BELOW.
    return abs(x - y) < maximum_allowable_difference

def babylonian_square_root(N: float, estimate: float, precision: float) -> float:
    new_estimate = (estimate + (N / estimate)) / 2  # DO NOT CHANGE THIS LINE; LEAVE IT HERE.
    # N         - the number whose square root you are calculating
    # estimate  - the caller's first estimate
    # precision - how close to get before you return a value
    # Imitate the iterative process shown below in the Introduction section using a while loop.
    # Keep looping until new_estimate and estimate are CLOSE ENOUGH (hint, hint).
    # Return the last calculated estimate (i.e. new_estimate).
    ...