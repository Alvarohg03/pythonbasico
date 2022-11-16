#nota hito individual=30%
#nota hito grupal=20%
#nota hito examen=50%

hito_individual=float(input('Dime la nota del hito individual '))
hito_grupal=float(input('Dime la nota del hito grupal '))
hito_examen=float(input('Dime la nota del examen '))

porcentaje_individual=0.3
porcentaje_grupal=0.2
porcentaje_examen=0.5

nota_individual=hito_individual*porcentaje_individual
nota_grupal=hito_grupal*porcentaje_grupal
nota_examen=hito_examen*porcentaje_examen

nota=round(nota_individual+nota_grupal+nota_examen)
print(nota)
