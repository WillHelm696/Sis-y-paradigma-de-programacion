"""
Cálculo de los salarios mensuales de los empleados de una empresa, sabiendo
que éstos se calculan en base a las horas semanales trabajadas y de acuerdo a un
precio especificado por horas. Si se pasan de cuarenta horas semanales, las horas
extraordinarias se pagarán a razón de 1,5 veces la hora ordinaria
"""
sum=0
num=0
sal=int(input("Cual es el salario por hora:"))
print("Cuantas horas trabajo esta semana ")
cont=0
while cont<7:
    print("Entra",cont)
    match cont:
        case 0:
            num=int(input("Lunes:"))
        case 1:
            num=int(input("Martes:"))
        case 2:
            num=int(input("Miercoles:"))
        case 3:
            num=int(input("Jueves:"))
        case 4:
            num=int(input("Viernes:"))
        case 5:
            num=int(input("Sabado:"))
        case 6:
            num=int(input("Domingo:"))
    if num < 0 or num > 24:
        print("Las horas no son correctas")
    else:
        sum+=num
        cont+=1

if sum > 40:

    print("Trabajo",sum," horas esxtra debe pagarse a razon de 1,5 que es de : $",(sum-40)*(sal*1.5)+(40*sal))

else:
    print("Trabajo",sum," horas esxtra debe pagarse normal",sum*sal)

