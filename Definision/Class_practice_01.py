# クラスを作成する

class Player: # クラス名　先頭は大文字にしよう
    def walk(self): # メソッドと呼ぶ
        print("勇者は荒野を歩いていた")
    
    def attack(self, enemy = "何か"):
        print("勇者は" + enemy + "を攻撃した")

player1 = Player() # オブジェクトを作成（変数に代入）
player1.walk() #変数名.メソッド
player1.attack("スライム")
player1.attack()


print("■ 変数をクラスで管理する")
# 変数をクラスで管理する

class Player:
    def __init__(self, job):
        self.job = job # self.job インスタンス変数
    
    def walk(self):
        print(self.job + "は荒野を歩いていた")

player1 = Player("戦士") # オブジェクト作成
player1.walk()

player2 = Player("魔法使い") # オブジェクト作成
player2.walk()

player1.walk() # 命令しているようなイメージ


print()

# RPGの敵クラスを作る

class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(self.name + "は勇者を攻撃した")

enemies = []
enemies.append(Enemy("スライム")) # オブジェクトもリストに入れられる
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:
    enemy.attack()


print()


# 引数と戻り値のあるメソッドを作る

class Item:
    tax = 1.08

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    
    def total(self):
        return int(self.price * self.quantity * Item.tax)
        # int関数は小数点以下を切り捨てるため
        # クラス内で変数を参照する場合 == クラス名.変数名

apple = Item(120, 15)
total = apple.total()

print("合計金額は" + str(total)+ "円です")

orange = Item(85, 32)
print("合計金額は" + str(orange.total()) + "円です")


print()