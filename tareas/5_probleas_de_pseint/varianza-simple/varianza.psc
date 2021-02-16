Algoritmo varianza_de_5_numeros
	
	// Solicitamos al usuario los 5 numeros
	// para sacar el promedio y despues la varianza
	Escribir "Escribe el número 1: " Sin Saltar
	Leer num1
	Escribir "Escribe el número 2: " Sin Saltar
	Leer num2
	Escribir "Escribe el número 3: " Sin Saltar
	Leer num3
	Escribir "Escribe el número 4: " Sin Saltar
	Leer num4
	Escribir "Escribe el número 5: " Sin Saltar
	Leer num5
	
	// Hago el promedio de los 5 números
	promedio = (num1 + num2 + num3 + num4 + num5 ) / 5
	
	// Calculo la varianza
	varianza = ( (num1 - promedio)^2 + (num2 - promedio)^2 + (num3 - promedio)^2 + (num4 - promedio)^2 + (num5 - promedio)^2 ) / 5
	
	// Muestro el resultado de la varianza en la pantalla
	Escribir "La varianza es: ", varianza
	
FinAlgoritmo
