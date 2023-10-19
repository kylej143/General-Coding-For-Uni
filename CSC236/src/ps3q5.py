"""
ps3q5 file
"""


def T(s):
    """
    takes "x_i" for all i in N
    "¬", "∧", "∨"

    Assume that if length of s is 1, it is always a string (because only x_i can be length 1)
    """
    # base case when s = "x_i", len(s) == 1
    if isinstance(s, str):
        # T(p) ≡ p
        return s

    # in the form of ("¬", p)
    elif len(s) == 2:
        if isinstance(s[1], str):  # base case 2 ("¬", "x_i")
            return s
        elif len(s[1]) == 2:  # case where T(¬(¬p)) ≡ T(p)
            return T(s[1][1])  # smaller as: (str, (str, tuple(size c))) -> tuple(size c)
        elif s[1][1] == "∧":  # case where T(¬(p ∧ q)); len(s[1] == 3
            return T(("¬", s[1][0])), "∨", T(("¬", s[1][2]))  # smaller as: (str, tuple(size 3)) -> tuple(size 3)
        else:  # case where T(¬(p ∨ q)); len(s[1] == 3
            return T(("¬", s[1][0])), "∧", T(("¬", s[1][2]))  # smaller as: (str, tuple(size 3)) -> tuple(size 3)

    # in the form of (q, "∧" or "∨", p)
    else:
        # T(s[0]) and T(s[2]) will recursively give a smaller formula;
        # or the formula of this recursion is already at it's simplest, then should just return itself
        # for example: (('x_1', '∨', 'x_2'), '∧', ('¬', 'x_1')) cannot be simplified (computed) more
        return T(s[0]), s[1], T(s[2])


def test_T() -> None:
    # First, base cases should just return themselves as they are already the simplest / computed
    b0 = "x_1"
    b1 = ("¬", "x_1")
    b2 = ("x_1", "∨", "x_2")
    b3 = ("x_1", "∧", "x_2")
    assert T(b0) == b0
    assert T(b1) == b1
    assert T(b2) == b2
    assert T(b3) == b3

    # inductive cases (structurally composed of the bases)
    t2 = ("¬", b1)
    assert T(t2) == "x_1"

    t3 = ("¬", t2)
    assert T(t3) == b1

    t3 = ("¬", b2)
    assert T(t3) == (('¬', 'x_1'), '∧', ('¬', 'x_2'))

    t4 = ("¬", b3)
    assert T(t4) == (('¬', 'x_1'), '∨', ('¬', 'x_2'))

    t5 = ("¬", t3)
    assert T(t5) == b2

    t6 = ("¬", t5)
    assert T(t6) == (('¬', 'x_1'), '∧', ('¬', 'x_2'))

    assert (T(("¬", ((t6, "^", t5), ('¬', t4), ("x_3"))))
            == ((('x_1', '∨', 'x_2'), '∧', (('¬', 'x_1'), '∧', ('¬', 'x_2'))), '∧', ('¬', 'x_3')))


if __name__ == '__main__':
    test_T()
