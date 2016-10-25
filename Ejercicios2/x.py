# Ejercicio 10

print "**** Codificado de Frases ****"

a = input ("Ingrese palabra: ")
c = list(a)
m = len(a)
d = ""
e = ""
for j in range(0,m):
   if c[j] == "a" :
	  d == "4" 
   elif c[j] == "e" :
	  d == "3"  
   elif c[j] == "i" :
	  d == "1"
   elif c[j] == "o" :
	  d == "0"
   elif c[j] == "u" :
	  d == "#"
   else :
   	  d == c[j]
   e = e + d
print e