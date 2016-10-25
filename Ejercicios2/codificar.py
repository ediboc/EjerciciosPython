# Ejercicio 10

print "**** Codificado de Frases ****"

continuar = "S"
while (continuar == "S"):
   a = raw_input ("Ingrese frase: ")
   x = a.lower()
   b = x.split()
   n = len(b)
   e = ""

   for i in range(0,n):
      d = ""
      c = list(b[i])
      m = len(c)
      for j in range(0,m):
         if c[j] == "a" :
	        c[j] = "4" 
         elif c[j] == "e" :
	        c[j] = "3"  
         elif c[j] == "i" :
	        c[j] = "1"
         elif c[j] == "o" :
	        c[j] = "0"
         elif c[j] == "u" :
	        c[j] = "#"
         d = d + c[j]
      b[i] = d
      e = e + b[i] + " "
   print e
   continuar = raw_input ("Desea ingresar otra frase (S/N): ")

	
   
