class quick_find:
    def __init__(self, n):
        self.n = n
        self.data = [i for i in range(n)]

    def connected(self, p, q):
        return self.data[p] == self.data[q]

    def union(self, p, q):
        pid = self.data[p]
        qid = self.data[q]
        for i in range(self.n):
            if self.data[i] == pid:
                self.data[i] = qid


qf = quick_find(100000000)
print(qf.connected(1, 2))
# print(qf.data)
qf.union(1, 2)
print(qf.connected(1, 2))
# print(qf.data)
