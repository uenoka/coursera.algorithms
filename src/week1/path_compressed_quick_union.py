class path_compressed_quick_union:
    def __init__(self, n):
        self.n = n
        self.data = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def root(self, p):
        while p != self.data[p]:
            self.data[p] = self.data[self.data[p]]
            p = self.data[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        if self.size[proot] < self.size[qroot]:
            self.data[qroot] = proot
            self.size[qroot] += self.size[proot]
        else:
            self.data[proot] = qroot
            self.size[proot] += self.size[qroot]


qu = path_compressed_quick_union(100)

qu.union(1, 2)
qu.union(3, 2)
qu.union(3, 4)
qu.union(5, 4)
qu.union(10, 20)
qu.union(30, 20)
qu.union(30, 40)
qu.union(50, 40)
