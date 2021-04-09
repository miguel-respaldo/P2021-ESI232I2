Funcion  resultado <- suma (numero1, numero2)
	
	resultado <- numero1 + numero2
	
Fin Funcion

Algoritmo funcion_con_returono_de_valores
	
	Escribir "Escribe un número: " Sin Saltar
	Leer num1
	Escribir "Escribe otro número: " Sin Saltar
	Leer num2
	// invocamos la función con argumentos
	res <- suma(num1, num2)
	
	Escribir "El resultado es ", res

FinAlgoritmo
