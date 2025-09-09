"""
Cree un diccionario con los nombres de 5 personas de su familia y sus edades.
Indicar el integrante más grande y el mas chico.
"""

print("Base de datos FAMILIAR")
family={"bart":10,"lisa":8,"magie":1,"Homer":39,"Marge":34}
mayor=0
nombre_mayor=None
menor=1000
nombre_menor=None
for valor,indice in family.items():
    if mayor<=indice:
        mayor=indice
        nombre_mayor=valor
    if menor >= indice:
        menor = indice
        nombre_menor=valor

#print("El mayor es ",list(family.keys())[list(family.values()).index(mayor)], mayor)
print("El mayor con ",mayor," es ",nombre_mayor)
#print("El menor es ",list(family.keys())[list(family.values()).index(menor)], menor)
print("El menor con ",menor," es ", nombre_menor)
