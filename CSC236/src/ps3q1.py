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
import pytest


def test_a() -> None:
    assert base == "a_{0} = 1/5 < 1."
    assert p("n_0 - 1") == "a_{n_0 - 1} < 1"
    assert step("n - 1", "IH") == "a_{n - 1 + 1} = (1 + a_{n - 1}) / 2 < (1 + 1) / 2 (from IH) = 1."


def test_b() -> None:
    ansSI = \
        "Base Case: a_{0} = 1/5 < 1.\n" \
        "Inductive Step: Let n ∈ N. Assume (IH) a_{n} < 1.\n" \
        "a_{n + 1} = (1 + a_{n}) / 2 < (1 + 1) / 2 (from IH) = 1."
    assert SI(p, base, step) == ansSI


def test_c() -> None:
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


def test_d() -> None:
    assert True


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
    WOP() is a tenary function
    Takes in p, base, step; returns a proof by Well-Ordering Principle that p is True.
    """
    return "Base Case: " + base + "\nInductive Step: Let n ∈ N. Assume (IH) " + p("n") + ".\n" + step("n", "IH")


def WOP(p, base, step) -> str:
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
