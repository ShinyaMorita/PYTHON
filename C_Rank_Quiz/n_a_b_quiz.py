#　nはゼロ埋め後の桁数、aは開始の値、bは終了の値
n, a, b = map(int, input().split())
print(n)
print(a)
print(b)

# 開始～終了までの値をリストに入れる
num_list = []
for i in range(b - a + 1):
    num_list.append(a + i)

# num_listの値をn桁になるようにゼロ埋め
for j in range(len(num_list)):
    print(str(num_list[j]).zfill(n))