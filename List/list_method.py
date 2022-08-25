# 文字列とリストのメソッド

text = "pYthon"
print(text)
print(text.capitalize()) # 頭文字だけ大文字化 (他は小文字化)
print(text.upper()) # すべて大文字化

players = "勇者,戦士,魔法使い,忍者"
list = players.split(",") # split関数 引数から分割してリスト化
print(list)
list.remove("忍者") # リストから除去
list.append("盗賊") # リストに追加
print(list)
print(text.islower()) # すべて小文字なら True
list.insert(2,"格闘家") # リストに挿入 (インデックス番号, 挿入するもの)
print(list)
