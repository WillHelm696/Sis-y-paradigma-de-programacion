"""
Dado una lista de 10 nombres de personas, realice un programa que cargue la
lista, la ordene de forma ascendente y la muestre por pantalla ordenado. Python
nos brinda la función “sorted” para realizar dicho procedimiento, pero la idea es
que el ejercicio se resuelva utilizando algoritmia propia de algún método de
ordenamiento existente.
"""

Nombres=["Michael Scott","Dwight Schrute","Jim Halpert",
         "Pam Beesley","Ryan Howard","Karen Filippelli",
         "Meredith Palmer","Creed Braton","Erin Hannon","Toby Flenderson"]
#Nombres = []

print("Ingrese Los Nombres 0 Para Teminar")

x=input("Nombre: ")
while x != "0":
    Nombres.append(x)
    x=input("Nombre: ")    

print(Nombres)

for i in range(len(Nombres)-1):
    for j in range(len(Nombres)-1-i):

        #print(Nombres[j],"Compara Con", Nombres[j+1] )

        if Nombres[j].lower() > Nombres[j+1].lower():
            aux= Nombres[j]
            Nombres[j]=Nombres[j+1]
            Nombres[j+1]= aux
 
print("Lista de Nombres Ordebados")
print(Nombres)