god = int(input("введите год"))
if god % 4 == 0 and god % 100 != 0 or god % 400 == 0:
    print("год високосный")
else:
    print("год не високосный")