Algoritmo formula_general
	// Escribo la descripci�n del programa
	Escribir "Programa para calcular la soluci�n de"
	Escribir "una ecuaci�n cuadratica"
	Escribir ""
	// Pido los datos de entrada
	Escribir "Ingresa el valor de a: " Sin Saltar
	Leer a
	Escribir "Ingresa el valor de b: " Sin Saltar
	Leer b
	Escribir "Ingresa el valor de c: " Sin Saltar
	Leer c
	
	// Calculo el discriminante (el que esta dentro de la raiz)
	discriminante <- b^2 - 4*a*c
	
	// Veo si el discriminante es mayor a cero
	si discriminante >= 0 Entonces
		// Si es mayor a cero entonces calulo x1 y x2
		x1 = (-b + rc(discriminante)) / 2*a
		x2 = (-b - rc(discriminante)) / 2*a
		// Muestro el resultado en pantalla
		Escribir "la soluci�n x1 es ", x1
		Escribir "la soluci�n x2 es ", x2
	SiNo
		// Si el discriminante No es mayor a cero
		// entonces es menor a cero y tiene raices negativas
		Escribir "La soluci�n tiene raices negativas"		
	FinSi
	
	
FinAlgoritmo
