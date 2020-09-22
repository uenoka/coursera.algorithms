class quick_find:
    def __init__(self,n):
        self.id = [0]*n
        self.n = n
        for i in range(n):
            self.id[i] = i

    def connected(self,p,q):
        return self.id[p] == self.id[q]
    
    def union(self,p,q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.n):
            if self.id[i]==pid:
                self.id[i]=qid

