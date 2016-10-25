#Sustituir notas por estatus final (ejercicio 1)

def status_notas(a):
    n = len(a)
    for i in range (n):
	j = a[i]
	if j > 6:
	   a[i]='Aprobado'
	elif j > 4:
	   a[i] ='Reparacion'
	else:
         a[i] ='Reprobado'
