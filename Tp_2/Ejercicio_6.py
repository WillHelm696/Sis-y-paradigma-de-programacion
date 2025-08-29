"""
Cree un diccionario con los nombres de 5 personas de su familia y sus edades.
Indicar el integrante más grande y el mas chico.
"""

print("Base de datos FAMILIAR")
family={"bart":10,"lisa":8,"magie":1,"Homer":39,"Marge":34}
mayor=0
for i in family.values():
    if mayor<=i:
        mayor=i
print("El mayor es ",list(family.keys())[list(family.values()).index(mayor)], mayor)
