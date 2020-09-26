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
        print(self.size[proot], self.size[qroot])
        if self.size[proot] < self.size[qroot]:
            self.data[qroot] = proot
            self.size[qroot] += self.size[proot]
        else:
            self.data[proot] = qroot
            self.size[proot] += self.size[qroot]


qu = weighted_quick_union(10)

qu.union(1, 2)
print("size", qu.size)
print("data", qu.data)
qu.union(3, 4)
print("size", qu.size)
print("data", qu.data)
qu.union(5, 6)
print("size", qu.size)
print("data", qu.data)
qu.union(7, 8)
print("size", qu.size)
print("data", qu.data)
print("====")

qu.union(1, 3)
print("size", qu.size)
print("data", qu.data)
qu.union(5, 7)
print("size", qu.size)
print("data", qu.data)
qu.union(1, 5)
print("size", qu.size)
print("data", qu.data)

print("====")
print("size", qu.size)
print("data", qu.data)
