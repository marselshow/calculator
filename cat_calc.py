print("Введите возраст кота(кошки):")

old = int(input())
if old > 15:
    print("Введите возраст до 15 лет.")
else:
    print("Вашему коту(кошке) осталось жить:",15-int(old),"лет")
    
if old== 15:
    print("Ваш кот прожил больше 15 лет, он может скоро умереть :(")
