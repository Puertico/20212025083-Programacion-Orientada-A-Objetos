# taller 1

a=int(input("ingrese el primer numero que desea sumar  "))

b=int(input("ingrese el segundo numero que desea sumar  "))

suma= a+b

def menor(a,b):
    if a<b:
      return a
    elif a>b:
        return b
    else:
        return print("los numneros son iguales ")
    
    
def imprimir(a,b):
    if a<b:
        for i in range(a+1,b):
            print(i)
    elif a>b:
        for v in range(b+1,a):
            print(v)     
    else:
         return a
        

print(suma)

print(menor(a,b))

print(imprimir(a,b))







