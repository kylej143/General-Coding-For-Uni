# Problem Set 1 for CSC236

def ps1q2(x: float, n: float) -> float:
    """
    Return the value of C_n = (x ** n) + 1 / (x ** n).

    Preconditions:
        - x is a non-zero number (and Assume for all cases)
        - n is a natural number in N = {0, 1, 2...};

    This function is built so such that:
        - function must be recursive
        - Does not use loops, helper functions, call any exponentiation functions.

    We Know (Lemma 1): ps1q2(x, n) = ps1q2(x, 1) * ps1q2(x, n-1) - ps1q2(x, n-2) for n >= 2

    Note that the function (since we're dealing with floats and exponentials)
    for some answers are approximatley the answers but not the exact answers.
    >>> ps1q2(3, 2)
    9.111111111111112
    >>> ps1q2(2.54, 7)
    682.0825671131605
    """
    # base case when n = 0.
    if n == 0:
        return 2
    # base case when n = 1
    elif n == 1:
        return x + 1 / x
    # case when n >= 2 (Recursive Step)
    else:
        # based on (Lemma 1)
        # Handles recursive calls for n = 1, n - 1, and n - 2
        # the lowest n can be is 2, hence n-2 = 0, which meets the preconditions.
        # x is unchanged, hence will also meet the preconditions for the recursive calls.
        # recursively, the calls will only call upon smaller cases, as we are taking values
        # of n that is smaller than the current n; until it hits either n = 0 or n = 1
        answer = ps1q2(x, 1) * ps1q2(x, n - 1) - ps1q2(x, n - 2)
    return answer


def ps1q3(n: int) -> int:
    """
    Return the value of A_n = A_(floor(sqrt(n))) ** 2 + 2 * A_(floor(sqrt(n))).

    Preconditions:
        - n is a positive natural number in N = {1, 2...};

    This function is built so such that:
        - function must be recursive
        - Does not use loops, helper functions.

    This function uses Module math. (import math needed)
    Note that the function (since we're dealing with floats and exponentials)
    for some answers are approximatley the answers but not the exact answers.
    >>> ps1q3(1)
    1
    >>> ps1q3(2)
    3
    >>> ps1q3(4)
    15
    """
    import math
    # base case when n = 1
    if n == 1:
        return 1
    # case when n >= 2 (Recursive Step)
    else:
        # set a variable equal to the floored square root of n
        flooredSqrtN = math.floor(math.sqrt(n))
        # Handles recursive calls for flooredSqrtN which is always greater than or equal to 1 since n >= 2;
        # which meets the precondition that n is a positive natural number.
        # recursively, the calls will only call upon smaller cases, as floor of a square root is always smaller
        # than the original (for natural numbers); except for n = 1 (which is the base case, recursion stops)
        answer = ps1q3(flooredSqrtN) ** 2 + 2 * ps1q3(flooredSqrtN)
    return answer


def ps1q3e(n: int) -> int:
    """
    Return the value of A_n = A_(floor(sqrt(n))) ** 2 + 2 * A_(floor(sqrt(n))). Error if n = 1.

    Preconditions:
        - n is a positive natural number in N = {1, 2...};

    This function is built so such that:
        - function must be recursive
        - Does not use loops, helper functions.

    This function uses Module math. (import math needed)
    Note that the function (since we're dealing with floats and exponentials)
    for some answers are approximatley the answers but not the exact answers.

    ps1q3e(1) -> returns exception
    >>> ps1q3e(2)
    3
    >>> ps1q3e(4)
    15
    """
    import math
    # base case when n = 1
    # this will raise an exception when the initial n value we put is 1
    if n == 1:
        raise Exception("n = 1 exception raised")
    # case when n >= 2 (Recursive Step)
    else:
        # set a variable equal to the floored square root of n
        flooredSqrtN = math.floor(math.sqrt(n))
        # stops recursion from reaching n = 1 as that will return an exception, let flooredSqrtN = 1, which is always 3.
        if flooredSqrtN == 1:
            answer = 3
        # Handles recursive calls for flooredSqrtN which is always greater than or equal to 1 since n >= 2;
        # which meets the precondition that n is a positive natural number.
        # recursively, the calls will only call upon smaller cases, as floor of a square root is always smaller
        # than the original (for natural numbers); except for n = 1 (where it stops on the if above)
        else:
            answer = ps1q3e(flooredSqrtN) ** 2 + 2 * ps1q3e(flooredSqrtN)
    return answer


if __name__ == '__main__':
    import doctest

    doctest.testmod()
