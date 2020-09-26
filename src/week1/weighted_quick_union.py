class weighted_quick_union:
    def __init__(self, n):
        self.n = n
        self.data = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def root(self, p):
        while p != self.data[p]:
            p = self.data[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        if self.size[proot] < self.size[qroot]:
            self.data[proot] = qroot
            self.size[proot] += self.size[qroot]
        else:
            self.data[qroot] = proot
            self.size[qroot] += self.size[proot]


qu = weighted_quick_union(7)

qu.union(1, 2)
print('data', qu.data)
print('size', qu.size)
qu.union(3, 2)
print('data', qu.data)
print('size', qu.size)
qu.union(3, 4)
print('data', qu.data)
print('size', qu.size)
qu.union(5, 4)
print('data', qu.data)
print('size', qu.size)
