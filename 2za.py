mesto = int(input("введите место"))
if mesto < 1 or mesto > 64:
    print("таких мест нет")
elif mesto % 8 == 1 or mesto % 8 == 4:
    print("место",mesto,"нижнее место в купе")
elif mesto % 8 == 2 or mesto % 8 == 5:
    print("место", mesto, "верхнее место в купе")
elif mesto % 8 == 3 or mesto % 8 == 6:
    print("место",mesto,"нижнее и боковоее место")
else:
    print("место",mesto,"верхнее и боковоее место")



