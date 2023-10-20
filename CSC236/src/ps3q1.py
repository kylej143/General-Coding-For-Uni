"""
ps3q1 file

NOTE for the TA:

For part (c)
the line from the pdf file:
a_{m − 1 + 1} = (1 + a_{m − 1}) / 2 < (1 + 1) / 2 (from a_{m − 1} < 1) = 1.
uses - (minus) that is not equivalent to the other - (hyphen-minus) in the pdf file or the standard - (hyphen-minus).

a = "−"  # - from that line of the file (Minus: U+2212)
b = "-"  # - that i typed or any other - in the file (Hyphen-Minus: U+002D)
assert a == b
False

Just to let you know that specific line was like that (maybe a copy-paste thing from Latex during creation?)
Probably not that important; anyway, onto the actual file!
"""


"""
Answers Start Here
"""
base = "a_{0} = 1/5 < 1."


def p(n: str) -> str:
    """
    p() is a unary function
    Takes in a string n, and returns a_{n} < 1
    """
    return "a_{" + n + "} < 1"


def step(n: str, pn_name: str) -> str:
    """
    step() is a binary function
    Takes in n and pn_name, and returns a_{n+1} = (1+a_{n}) / 2 < (1+1) / 2 (from pn_name) = 1
    """
    return "a_{" + n + " + 1} = (1 + a_{" + n + "}) / 2 < (1 + 1) / 2 (from " + pn_name + ") = 1."


def SI(p, base, step) -> str:
    """
    SI() is a tenary function
    Takes in p, base, step; returns a proof by Simple Induction to show p is true.
    """
    return "Base Case: " + base + "\nInductive Step: Let n ∈ N. Assume (IH) " + p("n") + ".\n" + step("n", "IH")


def WOP(p, base, step) -> str:
    """
    WOP() is a tenary function
    Takes in p, base, step; returns a proof by Well-Ordering Principle that p is True.
    Similar reasoning and implementation to SI.
    """
    s = \
        "Assume, for contradiction, there is an n ∈ N where " + p("n") + " is false.\n" \
        "Let C = { n ∈ N : " + p("n") + " is false }.\n" \
        "Then C ⊆ N and by the assumption is non−empty.\n" \
        "So C has a minimum element m.\n" \
        "Then " + p("m") + " is false but " + p("n") + " is true for each natural n < m.\n" \
        "Case m = 0: But " + base[:-1] + " contradicting that " + p("m") + " is false.\n" \
        "Case m > 0: Then m − 1 < m, and m − 1 ∈ N since m > 0, so a_{m − 1} < 1.\n" \
        + step("m - 1", p("m - 1")) + "\n" \
        "But m = m − 1 + 1, so that contradicts that " + p("m") + " is false.\n" \
        "Conclusion: there is no n ∈ N where " + p("n") + " is false, so " + p("n") + " is true for every n ∈ N."
    return s


def unroll(p, base, step, n) -> str:
    """
    unroll() is a quaternary function
    that takes p, base, step, n and gives you a direct proof for P(n) (p is true for n)
    """
    s = base  # first line should be the base case
    for i in range(1, n+1):  # repeat for 1 to n
        # we take the \n before concatnating a string since we do not want a \n at the end of the string
        s = s + "\n" + p(str(i)) + ", since " + str(i) + " = " + str(i - 1) + " + 1 and\n" \
            + step(str(i-1), p(str(i-1)) + " above")  # convert i to str to meet the precondition for step and p.
    return s


"""
Answers End Here
Below are unit tests (if you wan to see)
"""


def test_base() -> None:
    assert base == "a_{0} = 1/5 < 1."


def test_p() -> None:
    assert p("n_0 - 1") == "a_{n_0 - 1} < 1"


def test_step() -> None:
    assert step("n - 1", "IH") == "a_{n - 1 + 1} = (1 + a_{n - 1}) / 2 < (1 + 1) / 2 (from IH) = 1."


def test_SI() -> None:
    ansSI = \
        "Base Case: a_{0} = 1/5 < 1.\n" \
        "Inductive Step: Let n ∈ N. Assume (IH) a_{n} < 1.\n" \
        "a_{n + 1} = (1 + a_{n}) / 2 < (1 + 1) / 2 (from IH) = 1."
    assert SI(p, base, step) == ansSI


def test_WOP() -> None:
    """all (minus) were converted to (hyphen minus) for the test (see docstring)"""
    ansWOP = \
        "Assume, for contradiction, there is an n ∈ N where a_{n} < 1 is false.\n" \
        "Let C = { n ∈ N : a_{n} < 1 is false }.\n" \
        "Then C ⊆ N and by the assumption is non−empty.\n" \
        "So C has a minimum element m.\n" \
        "Then a_{m} < 1 is false but a_{n} < 1 is true for each natural n < m.\n" \
        "Case m = 0: But a_{0} = 1/5 < 1 contradicting that a_{m} < 1 is false.\n" \
        "Case m > 0: Then m − 1 < m, and m − 1 ∈ N since m > 0, so a_{m − 1} < 1.\n" \
        "a_{m - 1 + 1} = (1 + a_{m - 1}) / 2 < (1 + 1) / 2 (from a_{m - 1} < 1) = 1.\n" \
        "But m = m − 1 + 1, so that contradicts that a_{m} < 1 is false.\n" \
        "Conclusion: there is no n ∈ N where a_{n} < 1 is false, so a_{n} < 1 is true for every n ∈ N."
    assert WOP(p, base, step) == ansWOP


def test_unroll() -> None:
    ansUnroll = "a_{0} = 1/5 < 1.\n" \
                "a_{1} < 1, since 1 = 0 + 1 and\n" \
                "a_{0 + 1} = (1 + a_{0}) / 2 < (1 + 1) / 2 (from a_{0} < 1 above) = 1.\n" \
                "a_{2} < 1, since 2 = 1 + 1 and\n" \
                "a_{1 + 1} = (1 + a_{1}) / 2 < (1 + 1) / 2 (from a_{1} < 1 above) = 1.\n" \
                "a_{3} < 1, since 3 = 2 + 1 and\n" \
                "a_{2 + 1} = (1 + a_{2}) / 2 < (1 + 1) / 2 (from a_{2} < 1 above) = 1.\n" \
                "a_{4} < 1, since 4 = 3 + 1 and\n" \
                "a_{3 + 1} = (1 + a_{3}) / 2 < (1 + 1) / 2 (from a_{3} < 1 above) = 1.\n" \
                "a_{5} < 1, since 5 = 4 + 1 and\n" \
                "a_{4 + 1} = (1 + a_{4}) / 2 < (1 + 1) / 2 (from a_{4} < 1 above) = 1."
    assert unroll(p, base, step, 5) == ansUnroll


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
