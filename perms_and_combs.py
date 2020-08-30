def combination(n: int, r: int) -> tuple:
    """
    returns: a generator of all possible combinations of r elements from the set {0, 1, 2, ..., n-1}
    """
    assert r <= n
    assert r > 0
    assert n > 0

    comb = tuple(range(r))

    while True:
        yield comb

        # i = index of number that needs to be incremented next
        i = r - 1
        while True:
            if comb[i] != n - r + i:
                break
            i -= 1

        if i < 0:
            # end of sequence
            break

        comb = comb[:i] + tuple(range(comb[i] + 1, comb[i] + 1 + r - i))


def permutation_no_repetition(n: int, r: int) -> tuple:
    """
    returns: a generator of all possible perms_and_combs of r elements from the set {0, 1, 2, ..., n-1},
    not allowing repetition
    """
    assert r <= n
    assert r > 0
    assert n > 0

    perm = tuple(range(r))

    while True:
        yield perm

        # i = index of number that needs to be incremented next
        # increment_to = what to increase the ith number to
        i = r - 1
        while i >= 0:
            increment_to = min([c for c in range(n) if c > perm[i] and c not in perm[:i]], default=None)
            if increment_to is not None:
                break
            i -= 1

        if i < 0:
            # no increments to do, so terminate sequence
            break

        perm = perm[:i] + (increment_to, )
        # fill the rest with the minimum possible
        while len(perm) < r:
            perm = perm + (min([c for c in range(n) if c not in perm]),)
