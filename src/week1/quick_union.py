# quick_union.py
class quick_union:
    def __init__(self, n):
        self.n = n
        self.data = [i for i in range(n)]

    def root(self, p):
        while p != self.data[p]:
            p = self.data[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        self.data[proot] = qroot


qu = quick_union(10)
print(qu.connected(1, 2))
print(qu.data)
qu.union(1, 2)
print(qu.connected(1, 2))
qu.union(1, 3)
print(qu.data)
