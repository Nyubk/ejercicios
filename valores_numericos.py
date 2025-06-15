def limpiar_numVal(x): 

	for x in test.columns[1:]:  # suponiendo que la primera columna es 'Mes'
		test[x] = test[x].replace('[\$\€]', '', regex=True).str.replace(',', '.').astype(float)
	return