# stack

## stack API

stack の API は以下の通り

```python
class StackOfStrings():
    def push(item: string):
    def pop()->string:
    def isEmpty()->boolean:
    def size()->int:
```

## test client

テストデータ : 文字列がスペース区切りで与えられ、それぞれが1単語として扱われる。  
`-` が入力されたときのみ、文字列を pop する。  
例

test data

```txt
to bo or not to - be that - - - is
```

run result

```sh
to bo not that or be
```

test client

```python
stack = StackOfStrings()
line = stdin.readline().split()
for word in line:
     if word=="-":
        print(stack.pop())
     else:
        stack.push(word)
```

## linked list での実装

### linked list でのパフォーマンス

## array (Python では list) での実装

### array での問題点

- サイズ指定が必要になるので API が変わってしまう

## resizing-array での実装

### サイズを増やす方法

array のサイズを超えたときに、大きいサイズの array を作成する必要がある。  
方法としては以下のようなものが考えられる

- サイズが増えるにしたがって1つ大きな array を作成する

実装

```py
TBD
```

しかしこれでは push のたびに array を作り直し、そのたび計算が必要になるので O(N^2) 時間となってしまう。  
そこで以下のような解決策がある。

- サイズが超えたら倍のサイズにする

実装

```py
TBD
```

これにより push の計算量が O(N) になる。  
（最初の N + 2 + 4 + 8 + ... + N ≒ 3N となるため）

### サイズを減らす方法

無駄なメモリを持ってしまっているので pop 後にサイズを減らす必要がある。  
これもサイズ増加と同様に以下のような実装を考える。

- 今の array のサイズの半分に達したら array のサイズを半分にする

実装

```py
TBD
```

しかしこれでは以下のような場合に毎回 O(N) の計算量がかかってしまう。

- array が full の時に push, pop を交互に繰り返す場合

N  = 5

| 1   | 2   | 3   | 4   | 5   | 6    | 7    | 8    |
| --- | --- | --- | --- | --- | ---- | ---- | ---- |
| to  | be  | or  | not | to  | null | null | null |

N  = 4

| 1   | 2   | 3   | 4   |
| --- | --- | --- | --- |
| to  | be  | or  | not |

N  = 5

| 1   | 2   | 3   | 4   | 5   | 6    | 7    | 8    |
| --- | --- | --- | --- | --- | ---- | ---- | ---- |
| to  | be  | or  | not | to  | null | null | null |

N  = 4

| 1   | 2   | 3   | 4   |
| --- | --- | --- | --- |
| to  | be  | or  | not |

そのため、  

- array のサイズが 1/4 になったらサイズを半分に減らす

という方法で実装する。

### resizing-array での時間計算量パフォーマンス

|           | best | worst | amortized |
| --------- | ---- | ----- | --------- |
| construct | 1    | 1     | 1         |
| push      | 1    | N     | 1         |
| pop       | 1    | N     | 1         |
| size      | 1    | 1     | 1         |

### resizing-array での空間計算量パフォーマンス

8N ~ 32N byte

8N は array が full の時
32N は array が 1/4 full の時

## resizing array VS linked list

### トレードオフ

resizing array, linked list どちらでも stack は実装ができる。  
クライアントは両方使える。ではどっちがいい?

- Linked-list  

  - 最悪ケースですべての操作が定数時間
  - リンク処理のために無駄ない時間とメモリがある

- Resizing-array
  - ならし計算量で定数時間
  - 無駄なしスペースが少ない
