print("¿Cuál sería el número menor del rango que quisiera aplicar?")
a = input()
a = int(a)
print("¿Cuál sería el número mayor del rango que quisiera aplicar?")
b = input()
b = int(b)
print("Su cuenta regresiva sería:")
print(b)
continuee = True

while continuee:
    if(a!=b):
        b-=1
        print(b)
    else:
        continuee = False
