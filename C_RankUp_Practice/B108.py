# 観覧車の問題

li = input().split()
Gondora_Count = li[0]
Group_Count = li[1]
Cap_List = [0] * int(Gondora_Count)

for i in range(int(Gondora_Count)):
    Cap_List[i] = int(input())

print(Cap_List)

People_List = [0] * int(Group_Count)

for i in range(int(Group_Count)):
    People_List[i] = int(input())

print(People_List)
Summary = sum(People_List)
print(Summary)



People_List[0] = People_List[0] - Cap_List[0]
People_List[1] = People_List[1] - Cap_List[1]
print(People_List)