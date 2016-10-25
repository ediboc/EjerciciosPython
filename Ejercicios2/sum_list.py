# ejercicio 4 y 5 suma de listas

def sum_list(a,b):
    """ sum of list
	"""
    n = len(a)
    m = len(b)
    k = max(n,m)
    c = [0]*k
    for i in range(k):
	if i > (m-1):
	   c[i] = a[i]
	elif i > (n-1) :
	   c[i] = b[i]
	else:
	   c[i] = a[i]+b[i]
    return c
