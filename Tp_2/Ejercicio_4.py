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


print(Nombres)

for i in range(1,len(Nombres)-1):
    for j in range(0,len(Nombres)-i):

        #print(Nombres[j],"Compara Con", Nombres[j+1] )

        if Nombres[j].lower() > Nombres[j+1].lower():
            aux= Nombres[j]
            Nombres[j]=Nombres[j+1]
            Nombres[j+1]= aux
 
print("Nombres Ordebados")
print(Nombres)
print(sorted(Nombres))