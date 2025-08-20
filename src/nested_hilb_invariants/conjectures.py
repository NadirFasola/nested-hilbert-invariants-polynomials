# It's crucial to note that this is a SageMath file, not a standard Python file.
# It must be run within a SageMath environment.

from sage.all import *

# Define the ring and its fraction field globally for the module
R.<q,t>=QQ[]
RF = R.fraction_field()
Sym = SymmetricFunctions(RF)


def B(p):
    """
    Calculates the polynomial weigth B(p) for a given partition.

    Args:
        p: A SageMath Partition object

    Returns:
        A polynomial in the ring Q[q,t]
    """
    return R(sum(q^j*t^i for i,j in p.cells()))


def pExp(f):
    """
    Computes the plethystic exponential of a rational function.

    This is equivalent to exp( sum_{k>0} f(q^k,t^k)/k ).

    Args:
        f: A rational function in q,t.

    Returns:
        The plethystic exponential as a rational function.
    """
    f = RF(f)
    mon = f.denominator().monomials()
    assert len(mon)==1
    mon = mon[0]
    f *= mon
    f = R(f)
    res = prod((1-w/mon)^-c for c, w in f)
    return res


def enum_nested(big, sizes):
    """
    Constructs an iterator of partitions nested in in `big`.

    Args:
        big: the **given** outer partition. A SageMath Partition object.
        sizes: a List of sizes of all nested smaller partitions.
    """
    if len(sizes)==0:
        yield (big,)
    else:
        sz1 = sizes[:-1]
        sz0 = sizes[-1]
        for p in Partitions(sz0, outer=big):
            for seq in enum_nested(p, sz1):
                yield seq+(big,)


def WT(seq):
    """
    Computes the equivariant weight of the virtual tangent space to a fixed point given by a sequence of nested partitions.

    Args:
        seq: a List of SageMath Partition objects. Partitions **are assumed** to be nested.

    Returns:
        The equivariant weight of the virtual tangent space as a Laurent polynomial.
    """
    res = 0
    for k in range(len(seq)-1):
        res -= (q-1)*(t-1)*(B(seq[k])-B(seq[-1]))*(B(seq[k])-(B(seq[k-1]) if k>0 else 0)).subs(q=1/q,t=1/t)
    res -= q*t*(B(seq[-1])-B(seq[0]))
    return res


def WT_sum(big, sizes):
    """
    Computes the equivariant K-theoretic invariant associated to a set of fixed points, where the biggest partition in the nesting is fixed.

    Args:
        big: outer SageMath Partition.
        sizes: list[int], defines the sizes of the subsequent nestings.

    Returns:
        The equivariant K-theoretic invariant obtained by summing over fixed point with fixed max partition, as a rational function in q,t.
    """
    return sum(pExp(WT(s)) for s in enum_nested(big, sizes))



def test_pos_conjecture(big, sizes):
    A = WT_sum(big, sizes)/(1-q*t)^len(sizes)
    sizes = [0]+list(sizes)+[sum(big)]
    p = Partition([sizes[i+1]-sizes[i] for i in range(len(sizes)-1)])
    f = Sym.macdonald().Ht()[big]
    f = Sym.monomial()(f)
    B = f[p]
    print(A)
    print(B)
    diff = R(B-A)
    assert all(x>0 for x in diff.coefficients())

def test_equality(big, sizes):
    A = WT_sum(big, sizes)/(1-q*t)^len(sizes)
    sizes = [0]+list(sizes)+[sum(big)]
    p = Partition([sizes[i+1]-sizes[i] for i in range(len(sizes)-1)])
    f = Sym.macdonald().Ht()[big]
    f = Sym.monomial()(f)
    B = f[p]
    return A==B


def test_all(N):
    for big in Partitions(N):
        for p in Partitions(N):
            sizes = [0]
            for x in p:
                sizes.append(sizes[-1]+x)
            sizes = sizes[1:-1]
            print(big, sizes)
            test_conjecture(big, sizes)


def find_equalities(N):
    for big in Partitions(N):
        for p in Partitions(N):
            sizes = [0]
            for x in p:
                sizes.append(sizes[-1]+x)
            sizes = sizes[1:-1]
            if test_equality(big, sizes):
                print(big, sizes)
                assert all(sizes[i]==i+N-len(sizes) for i in range(len(sizes)))
            else:
                assert not all(sizes[i]==i+N-len(sizes) for i in range(len(sizes))) 
