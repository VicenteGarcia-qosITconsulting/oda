### Un texto con 10 espacios
texto="Esto son diez espacios:"
espacios=" "
punto="."
print(texto + espacios*10 + punto)

letras= ["a", "b", "c", "d", "e", "f"]
letras[0:3]
print(letras[0:3])
letras[0:3]= ["A", "B", "C"]
print(letras)

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
r=[a,b,c]
print(r)
print(r[1][1])
print(r[-1][-1])

###Comparar
print(1+1==3) 
print(4>=3)
a=10
b=5
print(a==b*2)
print("Hola" == "Hola")

l1=[0,1,2]
l2=[2,3,4]
print(len(l1)==len(l2))

print(True and True)

c= "Hola mundo"
len(c)>=20 or c[0]=="H"
print(len(c)>=20 or c[0]=="H")

c="Lectura"
print(len(c)=="H" or c[0]=="H")

a=5
a+=2
print(a)

