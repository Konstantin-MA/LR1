a = set()
b = set()

i = 0
print("Введите первое множество чисел")
while i<5 :
    number = input()
    a.add(number)
    i = i + 1
i = 0
print("Введите второе множество чисел")
while i<5 :
    number = input()
    b.add(number)
    i = i + 1
uni =  a.union(b)
intersct = a.intersection(b)
diff = a.difference(b)
sym_diff = a.symmetric_difference(b)
iss = a.issubset(b)
i = 0
while i<1 :
    print("Введите операцию с множествами")
    print("uni = объединение")
    print("intersct = пересечение")
    print("diff = разность a-b")
    print("sym_diff = симметрическая разность")
    print("iss = принадлежность a к b")
    n = input()
    if n == "uni" :
        print(uni)
    elif n == "intersct" :
        print(intersct)
    elif n == "diff" :
        print(diff)
    elif n == "sym_diff" :
        print(sym_diff)
    elif n == "iss" :
        print(iss)
    print("Желаете продолжить?")
    print("Введиде 0 , если да, введите 1 ,если нет")
    n = input()
    if n == 0 :
        i = 0
    elif n == 1 :
        i = 1