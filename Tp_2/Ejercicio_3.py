"""
Dadas 2 listas A y B de igual número de elementos, se desea generar e imprimir
una lista C conteniendo las sumas: A[i] + B[i] = C[i]. También indicar (solo
imprimir por pantalla) aquellos elementos que están en A y no están en B.
"""

print("Lista A y B")
A=[2,4,5,6,7,8]
B=[0,8,1,6,4,3]
print("A:",A," y B:",B)
if len(A)==len(B):
    C=[]
    SubA=[]
    for i,j in enumerate(A):
        C.append(B[i]+j)
        if not (j in B) :
            SubA.append(j)
    print(C)
    print(SubA)

    
