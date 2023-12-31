# Precondition: x ∈ R, y ∈ N.
# Postcondition: return x ** y (return 1 if x = y = 0).
def Pow1(x, y):
    # Precondition: y ∈ N, x ** y = (xi ** yi) * zi 
    # Postcondition: return x ** y (return 1 if x = y = 0).
    def r(xi, yi, zi):
        if yi <= 0:
            return zi
        else:
            if yi % 2 == 1:
                return r(xi * xi, yi // 2, zi * xi)
            else:
                return r(xi * xi, yi // 2, zi)
    return r(x, y, 1)


def test_Pow1() -> None:
    assert 5.123 ** 3 == Pow2(5.123, 3)
    assert 0 ** 0 == Pow2(0,0)
    assert (-2) ** 15 == Pow2(-2,15)
    assert (-2) ** 10 == Pow2(-2,10)


# Precondition: x ∈ R, y ∈ N.
# Postcondition: return x ** y (return 1 if x = y = 0).
def Pow2(x, y):
    return r(x, y, 1)


# Precondition: xi ∈ R, yi ∈ N, zi ∈ R.
# Postcondition: return (xi ** yi) * zi (return zi if y = 0).
def r(xi, yi, zi):
        if yi <= 0:  # here we can also say yi == 0, as yi ∈ N
            return zi
        else:
            if yi % 2 == 1:
                return r(xi * xi, yi // 2, zi * xi)
            else:
                return r(xi * xi, yi // 2, zi)


def test_Pow2() -> None:
    assert 5.123 ** 3 == Pow2(5.123, 3)
    assert 0 ** 0 == Pow2(0,0)
    assert (-2) ** 15 == Pow2(-2,15)
    assert (-2) ** 10 == Pow2(-2,10)


def test_r() -> None:
    assert 5.123 ** 3 * 5 == r(5.123, 3, 5)
    assert 0 ** 0 * 4 == r(0,0, 4)
    assert (-2) ** 15 * 0.3 == r(-2,15, 0.3)
    assert (-2) ** 10 * -5 == r(-2,10, -5)


# Precondition: x ∈ R, y ∈ N.
# Postcondition: return x ** y (return 1 if x = y = 0).
def PowR(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 == 1:
        return PowR(x * x, y // 2) * x
    else:
        return PowR(x * x, y // 2)


def test_PowR() -> None:
    assert 5.123 ** 3 == Pow2(5.123, 3)
    assert 0 ** 0 == Pow2(0,0)
    assert (-2) ** 15 == Pow2(-2,15)
    assert (-2) ** 10 == Pow2(-2,10)

