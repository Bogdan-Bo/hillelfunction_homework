"""
Function
1) def twentyone():
    a = int(input())
    if a == 21:
        return "You win"
    else:return "Try more"
print(twentyone())

2) def lst(text, text2):
    print(f"Длинна первой строки равна = {len(text)}, длинна второй строки равна = {len(text2)}")
    if len(text) > len(text2):
        return "Первая фраза больше"
    elif len(text2) > len(text):
        return "Вторая фраза больше"
print(lst("привет","пока"))

3) def suma(arg1,arg2):
    arg3 = arg1 + arg2
    return arg3
print(suma(5,6))

4) def square_area(arg1,arg2):
    s = arg1 * arg2
    return f"Square = {s}"
print(square_area(5,6))

5) def lst1(x, lst=None):
   if lst is None: lst=[]
   lst.append(x)
   return lst
print(lst1(1))

6) def nastroenie():
    a = input("Введите ваше настроение : ")
    if a == int:
        pass

    else:print("Настроение должно быть всегда хорошее")
print(nastroenie())

7) def schetxhik(x,y,z):
    if z == "+":
        print(x + y)
    elif z == "-":
        print(x - y)
    else:print("Ne ponal")
print(schetxhik(1,2,"+"))"""
