Algoritmo mayor_de_tres_numeros
	// Pedir los terminos (los 3 numeros)
	Escribir "Escribe el primer n�mero: " Sin Saltar
	Leer num1
	Escribir "Escribe el segundo n�mero: " Sin Saltar
	Leer num2
	Escribir "Escribe el tercer n�mero: " Sin Saltar
	Leer num3
	
	Si num1 > num2 Entonces
		Si num1 > num3 Entonces
			Escribir "El mayor es ", num1
		SiNo
			Escribir "El mayor es ", num3
		FinSi
	SiNo
		Si num2 > num3 Entonces
			Escribir "El mayor es ", num2
		SiNo
			Escribir "El mayor es ", num3
		FinSi
	FinSi
	
	
FinAlgoritmo
