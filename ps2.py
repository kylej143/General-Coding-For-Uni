# Problem Set 2 for CSC236
import random


def main():
    playGame(23452, 12534, True)
    # for _ in range(0, 101):
    #     i = random.randint(1, 50)
    #     j = random.randint(1, 50)
    #     if i == j:
    #         j -= 1
    #     playGame(i, j, True)


def playGame(i: int, j: int, t: bool) -> None:
    """
    Play the game until someone wins
    You can assume that you cannot first call the method i, j = 0;
    but it is okay if it is called recursively.

    Preconditions:
        - i is a natural number in N = {0, 1, 2...}
        - j is a natural number in N = {0, 1, 2...};
        - t is True when it is player 1's turn, False if player 2's.
        - if t, then i != j
        - if not t, then i == j
    """
    # end of recursion
    if i == 0 and j == 0 and not t:
        print("player 1 wins")
        return
    elif i == 0 and j == 0 and t:
        print("player 2 wins")
        return

    if t and i > j:
        k = i - j
        i -= k  # as for some k in N, i = j + k, makes i smaller
        print("from pile i, take: " + str(k))
        # i = j, and j, i is in N; it was P1's turn so next recursion should be P2's
        playGame(i, j, False)  # i is smaller, and i == j (satisfies all precon)
    elif t and i < j:
        k = j - i
        j -= k  # as for some k in N, j = i + k, makes j smaller
        print("from pile j, take: " + str(k))
        # j = i, and i, j is in N; it was P1's turn so next recursion should be P2's
        playGame(i, j, False)  # j is smaller, and i == j (satisfies all precon)
    else:  # player 2's turn
        if 0 == random.randint(0, 1) and i != 0:
            x = random.randint(1, i)  # at least 1, at most all
            i -= x  # makes i smaller by at least 1
            print("from pile i, take: " + str(x))
        else:
            x = random.randint(1, j)  # at least 1, at most all
            j -= x  # makes j smaller by at least 1
            print("from pile j, take: " + str(x))
        # j = i, and i, j is in N; it was P2's turn so next recursion should be P1's
        playGame(i, j, True)  # either i or j is smaller, and i != j (satisfies all precon)


if __name__ == "__main__":
    main()
