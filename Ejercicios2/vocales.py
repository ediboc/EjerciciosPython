#identificar vocales en palabras, ejercicio 3

def five_vocal(word):
    """ para identificar si una palabra
	    posee las cinco vocales
	"""
    b = list(word)
    n = len(b)
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for j in range(n):
	w = word[j]
	if w == "a" :
	   a = a + 1
	elif w == "e" :
	   e = e + 1
	elif w == "i" :
	   i = i + 1
	elif w == "o" :
	   o = o + 1
	elif w == "u" :
	   u = u + 1
    if a > 0 and e > 0 and i > 0 and o > 0 and u > 0 :
	   result = True
    else :
	   result = False
	
    return result

def five_vocal_nr(word):
    """ para identificar si una palabra
	    posee las cinco vocales una sola vez
	"""
    b = list(word)
    n = len(b)
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for j in range(n):
	w = word[j]
	if w == "a" :
	   a = a + 1
	elif w == "e" :
	   e = e + 1
	elif w == "i" :
	   i = i + 1
	elif w == "o" :
	   o = o + 1
	elif w == "u" :
	   u = u + 1
    if a == 1 and e == 1 and i == 1 and o == 1 and u == 1 :
	   result = True
    else :
	   result = False
	
    return result
