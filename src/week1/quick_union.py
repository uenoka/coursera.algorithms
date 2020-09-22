# quick_union.py
class quick_union:
    def __init__(self,n):
        self.id = [0]*n
        self.n = n
        for i in range(n):
            self.id[i] = i

    def root(self,p):
        while p!=self.id[p]:
            p=self.id[p]
        return p

    def connected(self,p,q):
        return self.root(p) == self.root(q)

    def union(self,p,q):
        proot = self.root(p)
        qroot = self.root(q)
        self.id[proot]=qroot

