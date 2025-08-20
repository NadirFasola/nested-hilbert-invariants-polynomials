from sage.all import QQ, PolynomialRing, Partitions, prod
from sage.combinat.sf.sf import SymmetricFunctions

class NestedHilbConjectureCalculator:
    def __init__(self):
        self.R = PolynomialRing(QQ, 'q, t')
        self.q, self.t = self.R.gens()
        self.RF = self.R.fraction_field()
        self.Sym = SymmetricFunctions(self.RF)
        
    def B(self, p):
        return self.R(sum(self.q**j * self.t**i for i, j in p.cells()))

    def pExp(self, f):
        f = self.RF(f)
        mon = f.denominator().monomials()
        assert len(mon) == 1
        mon = mon[0]
        f *= mon
        f = self.R(f)
        res = prod((1 - w / mon)**(-c) for c, w in f)
        return res

    def enum_nested(self, big, sizes):
        if len(sizes) == 0:
            yield (big,)
        else:
            sz1 = sizes[:-1]
            sz0 = sizes[-1]
            for p in Partitions(sz0, outer = big):
                for seq in self.enum_nested(p, sz1):
                    yield seq + (big,)

    def WT(self, seq):
        res = 0
        q,t = self.q, self.t
        for k in range(len(seq) - 1):
            res -= (q-1)*(t-1)*(self.B(seq[k])-self.B(seq[-1]))*(self.B(seq[k])-(self.B(seq[k-1]) if k>0 else 0)).subs(q=1/q,t=1/t)
        res -= q*t*(self.B(seq[-1])-self.B(seq[0]))
        return res

    def WT_sum(self, big, sizes):
        return sum(self.pExp(self.WT(s)) for s in self.enum_nested(big, sizes))
    
    def get_macdonald_monomial(self, big):
        macdonald_poly = self.Sym.macdonald().Ht()[big]
        monomial_basis_poly = self.Sym.monomial()(macdonald_poly)
        return monomial_basis_poly
