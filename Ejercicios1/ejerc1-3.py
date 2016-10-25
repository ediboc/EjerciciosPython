print('** Calculo de horas trabajadas **')
NUM_HORA_TRA = input ('Indique horas trabajadas: ')
VALOR_HORA_PAG = input('Indique pago por hora: ')

if NUM_HORA_TRA<40 :
    PAGO = NUM_HORA_TRA*VALOR_HORA_PAG
	
else:
    PAGO = ((NUM_HORA_TRA-40)*1.5+40)*VALOR_HORA_PAG
	
print 'Monto a pagar: ', PAGO