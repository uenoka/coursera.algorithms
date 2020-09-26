# Quick find algorithm

## 概要

SNS での友達やネットワーク内のコンピュータなど、実社会でもAとBが繋がる、繋がっているかを確認する、ということが多くある。  
問題を抽象化すると、次のようになる

- N個のオブジェクトがある
- Union コマンドで2つのオブジェクトをつなげる
- Find, connected クエリで2つのオブジェクトにつながりがあるかを確認する

ということをしたい。

これを行うためのデータ構造・アルゴリズムが Union find tree

## どのように実装するか

### 1. 同じグループであることを高速に判定する

#### 処理のイメージ

まず最初に、「同じグループであることを高速に判定する」ことだけに焦点を当てて、データ構造を見てみると、次のような実装ができる。

- 0 ~ N-1 の N 個の要素を持った配列を用意して、各要素を index と同じ値で初期化する。
- 同じグループに入れる際は、対象の要素を同じ値にする
- 同じグループかの確認は要素を比較することで実現する

（講義ではこのデータ構造を Quick Find と呼んでいたのでここでも Quick Find とします）

##### 初期化後の配列の中身

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |

##### 2, 3 が同じグループかの判定をする

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |

→data[2] = 2 ,data[3] = 3 なので False となる。

##### 2, 3 をunionした時の処理の流れ

data の各要素が 3 かどうかを見ていき、data[i]= 3 となる箇所を 2 にする。

| 0   | 1   | 2   | 3      | 4   | 5   | 6   | 7   | 8   | 9   |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3 -> 2 | 4   | 5   | 6   | 7   | 8   | 9   |
| NO  | NO  | NO  | YES    | NO  | NO  | NO  | NO  | NO  | NO  |

##### 再度 2, 3 が同じグループかの判定をする

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 2   | 4   | 5   | 6   | 7   | 8   | 9   |

→data[2] = 2 ,data[3] = 2 なので True となる。

#### 実装

Python で実装すると下記のようなものになる。

```Python
class quick_find:
    def __init__(self,n):
        self.n = n
        self.data = [i for i in range(n)]

    def connected(self,p,q):
        return self.data[p] == self.data[q]

    def union(self,p,q):
        pid = self.data[p]
        qid = self.data[q]
        for i in range(self.n):
            if self.data[i]==pid:
                self.data[i]=qid

qf = quick_find(10)
print(qf.connected(2, 3))
qf.union(2, 3)
print(qf.connected(2, 3))
```

#### 計算量

この時、connected は配列にアクセスするだけなので、O(1) と高速に実行できる。
しかし union は毎回配列のすべての要素を見て、要素を変更する必要があるため、O(N) の計算量がかかってしまう。
**これだと N が大きく union の操作が多数発生するような場合では実用的にはならない**

| init | union | connected |
| ---- | ----- | --------- |
| O(N) | O(N)  | O(1)      |

### 2. 結合処理を早くなるよう実装する

#### 処理のイメージ

そこで次に、データ構造を木構造にすることを考える。
こうすることにより、 union 時には、片方の要素の親をもう片方の要素の値に変更してやるだけで同じグループとして扱うことができる。
また、connected では、比較した要素の root 要素の値が同じかどうかを比較することで、同じグループかどうかを確認出来る。

（うまく Markdown で書けなかったので画像等作成して後で載せます…）

#### 実装

```Python
class quick_union:
    def __init__(self, n):
        self.n = n
        self.data = [i for i in range(n)]

    def root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        self.id[proot] = qroot


qu = quick_union(10)
print(qu.connected(1, 2))
print(qu.id)
qu.union(1, 2)
print(qu.connected(1, 2))
qu.union(1, 3)
print(qu.id)

```

#### 計算量

この方法によって、union は O(1) で実現することができた。
しかし、connected は場合によっては木構造が非常に高い階層になった場合 O(N) かかってしまうことになる。

| init | union | connected |
| ---- | ----- | --------- |
| O(N) | O(1)  | O(N)      |

### 3. Quick Union を高速化する（Union Find）

Quick Find では union が遅く、Quick Union では connected が遅いため、どうにかする必要があります。
そこで Quick Union をベースに、2つの高速手法を実装します。

#### 1. Weighted quick-union

先ほどの Quick Union の実装では、高さが高くなってしまった際に O(N) の計算量がかかってしまう状態でした。
そこで木構造が高くならないようにデータの持ち方を工夫する方法が、Weighted quick-union です。
簡単に言うと、union する木構造の大きさを調べ、小さいほうの木を大きいほうの木の下に入れる（逆に言うと小さいほうの木の root の親を 大きいほうの木の root 要素に書き換えてあげる）という形です。
こうすることによって、connected の計算量は木の高さ程度まで抑えられるため、 O(lgN) (lgN は底が2のlog) になる。

```Python
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


qu = weighted_quick_union(10)
print(qu.connected(1, 2))
print(qu.data)
qu.union(1, 2)
print(qu.connected(1, 2))
qu.union(1, 3)
print(qu.data)

```

| init | union  | connected |
| ---- | ------ | --------- |
| O(N) | O(lgN) | O(lgN)    |

#### 2. 経路圧縮

これは非常に高速に動作するのですが、1つ無駄なところがあります。
それは、pのrootを見に行くときに毎回同じルートをたどっていることです。

たとえば、1->2->3->4->5->6 と毎回たどっていたら毎回5回のステップを踏まないといけません。
1度目にroot を見つけてあげたら1,2,3,4,5の親を6で書き換えてあげる、ということを行うことで、再アクセスする際に非常に高速にすることができます。

```Python
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


qu = path_compressed_quick_union(7)

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

```
