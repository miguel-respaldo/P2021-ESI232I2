Algoritmo calculadora
	//Realizar 4 operaciones aritm�ticas:
	//suma, resta, multiplicaci�n  y divisi�n,
	//con dos n�meros enteros. 
	//Elegir una de las opciones y realizar el calculo	correspondiente. 
	
	Escribir "Escribe un n�mero: " Sin Saltar
	Leer num1
	Escribir "Escribe otro numero: " Sin Saltar
	Leer num2
	
	Escribir "1. Suma"
	Escribir "2. Resta"
	Escribir "3. Multiplicaci�n"
	Escribir "4. Divisi�n"
	Escribir ""
	Escribir "opci�n: " Sin Saltar
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
