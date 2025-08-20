from sage.all import Partition, Partitions

from nested_hilbert_invariants import NestedHilbConjectureCalculator

calculator = NestedHilbConjectureCalculator()
q, t = calculator.q, calculator.t

def test_equality(big, sizes):
    A = calculator.WT_sum(big, sizes)/(1-q*t)**len(sizes)
    sizes = [0] + list(sizes) + [sum(big)]
    p = Partition([sizes[i+1] - sizes[i] for i in range(len(sizes)-1)])
    H = calculator.get_macdonald_monomial(big)
    B = H[p]
    return A == B

def find_equalities(N):
    for big in Partitions(N):
        for p in Partitions(N):
            sizes = [0]
            for x in p:
                sizes.append(sizes[-1]+x)
            sizes = sizes[1:-1]
            if test_equality(big, sizes):
                print(big, sizes)
                assert all(sizes[i] == i + N - len(sizes) for i in range(len(sizes)))
            else:
                assert not all(sizes[i] == i + N - len(sizes) for i in range(len(sizes)))

test_size = eval(input("Max of external partition: "))

for n in range(test_size + 1):
    print('n0: ', n)
    find_equalities(n)
    print()