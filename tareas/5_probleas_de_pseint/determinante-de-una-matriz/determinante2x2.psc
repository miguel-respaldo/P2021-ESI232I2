Algoritmo determinante2x2
	// Pongo el titulo del programa
	Escribir "Programa para calcular el determinate de una matriz"
	Escribir ""
	// Le pido al usuario los valore de la matriz
	Escribir "Escribe el valor de a11: "
	Leer a11
	Escribir "Escribe el valor de a12: "
	Leer a12
	Escribir "Escribe el valor de a21: "
	Leer a21
	Escribir "Escribe el valor de a22: "
	Leer a22
	
	// Calculo el valor del determinante
	determinante = a11*a22 - a12*a21
	
	// Muestro en pantalla el valor del determinate
	Escribir "El determinante es: ", determinante
	
FinAlgoritmo
