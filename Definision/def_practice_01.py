#関数の練習
def sum(x,y):
    return x + y

num1 = sum(3,10)
print(num1)
num2 = sum(300,400)
print(num2)


# 掛け算関数を作成
def multiply(x, y):
    # この下に処理を記述する
    return x * y

print(multiply(3, 4))
print(multiply(5, 7))
print(multiply(12, 34))


# 九九の表
def multiply(x, y):
    return x * y

for step in range(1, 10): #ネストすることでシンプルにすることを可能にしている！
    for num in range(1, 10):
        print(multiply(step, num), end="")
        if num < 9:
            print(", ", end="")
    print()

# スコープを理解する
message = "Global Variable"
a = 10
b = 20

def sum(x, y):
    a = 3 #スコープ（変数が独立している）ローカル変数
    global message
    message += " add text " # グローバル変数の変更はあまり推奨されていないが
    print(message + " " + str(a))
    return x + y


num = sum(a, b)
print(num)
print(message + " " + str(a))


# RPG攻撃シーン
import random
def attack(enemy):
    print("勇者は" + enemy + "を攻撃した。")
    hit = random.randint(1,10)
    if hit < 9:
        print(enemy + "に、" + str(hit) + "のダメージを与えた！")
    else:
        print("クリティカルヒット！" + enemy + "に、50のダメージを与えた！！")


enemies = ["スライム","モンスター","ドラゴン"]
for enemy in enemies:
    attack(enemy)


print()
# RPGの攻撃シーン2

def attack(person):
    print(person + "はスライムを攻撃した")

def output_enemy_hp(enemy_hp):
    print("敵のHPは残り" + str(enemy_hp) + "です")

enemy_hp = 730
team = {"勇者" : 200, "戦士" : 150, "魔法使い" : 100}

for person, power in team.items():
    attack(person)
    enemy_hp -= power
    output_enemy_hp(enemy_hp)


print()


# 引数のデフォルト値

def introduce(greeting, name = "村人"): #デフォルト値
    print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者")
introduce("こんにちは")


print()#別パターン

def introduceA(greeting, *names): #可変長引数
    for name in names:
        print("私は" + name + "です。" + greeting)

introduceA("こんにちは", "勇者", "村人", "兵士", "王様")
introduceA("こんにちは")

print()#辞書を使ったパターン
def introduceB(**people): #可変長引数
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)
    print(people)

introduceB(hero = "初めまして", villager = "こんにちは", soldier = "よろしく！" , king = "ようこそ")


print()