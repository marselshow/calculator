print("Введите ваш возраст:")

old = int(input())
if old > 74:
     print("Введите возраст до 74 лет.")
else:
     print("Вам осталось жить:", 74 - int(old), "лет(года)")
if old == 74:
     print("Скорее всего вы скоро умрете :(")
