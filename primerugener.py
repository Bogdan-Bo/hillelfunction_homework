#1 List
"""import random
1 ) b = [i + 1 for i in range(7)]
print(b)
2 ) c = [i%4 for i in range(1,20)]
print(c)
3 ) d = [i*2 for i in "hello"]
print(d)
4 ) a = [random.randint(0,30) for i in range(30)]
print(a)
5 ) f = [i for i in a if i % 2 == 0 and i % 3 ==0]
print(f)
#2 dict
1 ) k = {num: num**2 for num in range(10)}
print(k)
2 ) z = {
    "sasha" : 1,
    "bogdan": 2,
    "vika"  : 3,
    "anton" : 4
}
x = {key.upper():values**2 for key,values in z.items()}
print(x)
3 ) g = [
    [1, 3, "hola"],
    [3, 5, "Poka"],
    [8, 9, "Privet"]
]
h = {num[0]:num for num in g}
print(h)
4) x = {key.upper():len("hello") for key in "hello"}
 print(x)
5)x = {
    1 : "kykyshka",
    5 : "golyb",
    2 : "leleka"
}
y = {key: value.title()  for key,value in x.items()}
print(y)
# set
1)my_set = {i for i in range(1, 10)}
print(my_set)
2)my_set = {i for i in [1, 2, 3, 1, 2, 3]}
print(my_set)
3)my_set = {i for i in ["google", "google", "nokia", "nokia", "python", "java"]}
print(my_set)
4)my_set = {i for i in ["google", "google", "nokia", "nokia", "python", "java"] if len(i) > 5}
print(my_set)
5)my_set = {i+y for i in "abc" for y in "xyz"}
print(my_set)"""








