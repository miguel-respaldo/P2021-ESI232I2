Algoritmo distancia_de_2_puntos
	// Pido los valores de los puntos (x1,y1) (x2,y2)
	Escribir "Ingresa el valor de x1: " Sin Saltar
	Leer x1
	Escribir "Ingresa el valor de y1: " Sin Saltar
	Leer y1
	Escribir "Ingresa el valor de x2: " Sin Saltar
	Leer x2
	Escribir "Ingresa el valor de y2: " Sin Saltar
	Leer y2
	
	// Calculo la distancia entre esos 2 puntos
	distancia = rc( (x1-x2)^2 + (y1-y2)^2 )
	
	// Muestro el resultado en pantalla
	Escribir "La distancia entre los dos puntos es ", distancia
	
FinAlgoritmo
