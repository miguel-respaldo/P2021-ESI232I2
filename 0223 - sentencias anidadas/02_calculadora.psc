Algoritmo calculadora
	//Realizar 4 operaciones aritméticas:
	//suma, resta, multiplicación  y división,
	//con dos números enteros. 
	//Elegir una de las opciones y realizar el calculo	correspondiente. 
	
	Escribir "Escribe un número: " Sin Saltar
	Leer num1
	Escribir "Escribe otro numero: " Sin Saltar
	Leer num2
	
	Escribir "1. Suma"
	Escribir "2. Resta"
	Escribir "3. Multiplicación"
	Escribir "4. División"
	Escribir ""
	Escribir "opción: " Sin Saltar
	Leer op
	
	Segun op Hacer
		1:
			Escribir "La suma es ", num1 + num2
		2:
			resultado <- num1 - num2
			Escribir "La resta es ", resultado
		3:
			Escribir "La multiplicacion es ", num1 * num2
		4:
			si num2 = 0 Entonces
				Escribir "No se puede dividir entre 0"
			SiNo
				resultado <- num1 / num2
				Escribir "La division es ", resultado				
			FinSi
		De Otro Modo:
			Escribir "La opcion es invalida"
	Fin Segun

FinAlgoritmo
