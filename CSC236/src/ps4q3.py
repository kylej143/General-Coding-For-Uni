# Precondition: v is comparable with the elements of A;
# A is a 2D array with each row and each column sorted.
# Postcondition: returns True if A contains v; False otherwise
def IsIn(v, A):
    # Precondition: [r0,r1][c0,c1] should be a valid index contained in A.
    # Postcondition: returns True if A[r0:r1][c0:c1] contains v; False otherwise.
    def Helper(r0, r1, c0, c1):
        for row in A[r0: r1]:
            for item in row[c0: c1]:
                if item == v:
                    return True
        return False

    return Helper(0, len(A), 0, len(A[0]))


def test_IsIn() -> None:
    A = [[1, 2, 3, 4], [5, 6, 7, 8]]
    for v in range(1, 9):
        assert IsIn(v, A)
    assert not IsIn(9, A)


# Precondition: v is comparable with the elements of A;
# A is a 2D array with each row and each column sorted.
# Postcondition: returns True if A contains v; False otherwise
def IsInBinary(v, A):
    # Precondition: [r0:r1][c0:c1] should be a valid index contained in A.
    # Postcondition: returns True if A[r0:r1][c0:c1] contains v; False otherwise.
    def Helper(r0, r1, c0, c1):
        # Base Case:
        if r0 == r1 - 1:  # since A[r0] == A[r0:r1] that has v in its range
            if c0 == c1 - 1:  # Base Case since A[...][c0] == A[...][c0:c1]
                # at this point we at the number equal to or nearest number that is bigger
                return A[r0][c0] == v
            else:
                m = (c0 + c1 - 1) // 2  # account the fact that c1 is the end index + 1
                if v <= A[r0][m]:
                    return Helper(r0, r1, c0, m + 1)  # m + 1 since indexing includes up to m + 1 - 1
                else:  # v > A[r0:r1][m]
                    return Helper(r0, r1, m + 1, c1)
        else:  # looks for the row that contains v
            m = (r0 + r1 - 1) // 2  # account the fact that r1 is the end index + 1
            if v <= A[m][0]:
                return Helper(r0, m + 1, c0, c1)  # m + 1 since indexing includes up to m + 1 - 1
            else:  # v > A[m][0]
                return Helper(m + 1, r1, c0, c1)

    return Helper(0, len(A), 0, len(A[0]))


def test_IsInBinary() -> None:
    A = [[1, 2, 5, 7, 10],
         [15, 18, 19, 19, 20],
         [21, 24, 25, 26, 27],
         [43, 45, 46, 47, 48]]
    answer = [1, 2, 5, 7, 10, 15, 18, 19, 20, 21, 24, 25, 26, 27, 43, 45, 46, 47, 48]
    for v in answer:
        assert IsIn(v, A)
    for n in [x for x in range(0, 50) if x not in answer]:
        assert not IsInBinary(n, A)
