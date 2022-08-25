# キーワード引数
def say_hello(greeting = "hello", target = "world"):
    print(greeting + " " + target)

say_hello()
say_hello("こんにちは", "皆さん")
say_hello("good morning!")
say_hello(greeting = "こんにちは", target = "皆さん")
say_hello(target = "先生", greeting = "おはようございます")
say_hello(target = "ネコさん")
say_hello(greeting = "こんばんは")