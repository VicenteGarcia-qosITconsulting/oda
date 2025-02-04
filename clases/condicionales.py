if True:
    print("Hola")
    print("otra linea")

a=2
if a== 2:
    print("a vale 2")
if a== 5:
    print("a vale 5")

n=11
if n%2 :
    print("es par")
else:
    print("El numero es impar")

nota= float(input("Introduce una nota: "))
if nota >=9:
    print("Sobresaliente")
elif nota >=7:
    print("Notable")
elif nota >=6:
    print("Bien")
elif nota >=5:
    print("Suficiente")
else:
    print("Insuficiente")

c=0
while c<=6:
    c+=1
    print("c vale: ", c)

num= int(input("Introduce un numero: ")) 
for i in range(1,11):
    print(f"Tabla del {i}:" , i)
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")

num= int(input("Introduce un numero: ")) 
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

