Algoritmo adivina_el_numero
	
	num_comp <- azar(10)
	
	Escribir "Adivina que n�mero estoy pensando: " Sin Saltar
	Leer num
	
	Mientras num_comp <> num 
		Escribir "No, ese no es el n�mero, intentalo de nuevo: "
		Leer num
	FinMientras
	
	Escribir "Felicidades, adivinaste"
	
	
FinAlgoritmo
