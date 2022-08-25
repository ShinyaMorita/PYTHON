n = int(input())

for i in range(n):
    a = input()
    print(len(a))


a = input()
S = input()

if a in S: # S の中に a が含まれるか
    print("YES")
else:
    print("NO")


n = input()

A = int(n[0]) + int(n[3]) # 文字列はリストと同じく[番号]で引き出せる
B = int(n[1]) + int(n[2])

print(str(A) + str(B))

# 自分で書いたコード
n = input()

if len(n) == 3:
    print(n)
elif len(n) == 2:
    print("0" + n)
else:
    print("00" + n)

# 解答例 綺麗
N = input()

while len(N) < 3:
    N = "0" + N

print(N)


