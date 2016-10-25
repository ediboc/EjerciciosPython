# ejercicio 2.7
def palindromo(word):
    a = list(word)
    n = len(word)
    m = n/2
    k = n/2.0 -n/2
    ind = 0
    i = 0
    if k == 0 :
	   j = 0
    else:
	   j = 1
    while (ind == 0 and i <= m):
	      i += 1
	      if a[i] == a[m*2-i+j-1] :
		     ind = 0
	      else :
		     ind +=  1
    if ind == 0 :
	   return True
    else: 
	   return False
    