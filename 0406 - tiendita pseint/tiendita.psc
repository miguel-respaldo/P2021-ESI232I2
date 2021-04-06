Algoritmo tiendita
	
	Dimension  lista_productos[5]
	Dimension  lista_precios[5]
	Dimension  carrito_producto[10]
	Dimension  carrito_cantidad[10]
	
	cantidad = 0
	
	lista_productos[1] <- "papas"
	lista_productos[2] <- "refrescos"
	lista_productos[3] <- "tortillas"
	lista_productos[4] <- "jamon"
	lista_productos[5] <- "mazapan"
	
	lista_precios[1] <- 12.0
	lista_precios[2] <- 10.5
	lista_precios[3] <- 20.0
	lista_precios[4] <- 40.0
	lista_precios[5] <-  5.0
	
	
	opcion_menu = 0
	
	Mientras opcion_menu <> 6 Hacer
		Escribir "---------------------"
		Escribir "1. Mostrar productos"
		Escribir "2. Mostrar carrito"
		Escribir "3. Agregar al carrito"
		Escribir "..."
		Escribir "6. Salir"
		Escribir " Opcion: " Sin Saltar
		Leer opcion_menu	
		
		Segun opcion_menu Hacer
			1:
				tamano = 5
				Escribir "No.    Nombre     Precio"
				Para i<-1 Hasta tamano Con Paso 1 Hacer
					Escribir i, "   ", lista_productos[i], "      ",lista_precios[i] 
				Fin Para
				
			2:
				Escribir "--------  Carrito  ----------"
				Escribir "No.    Nombre     Precio    Cantidad"
				Para i<-1 Hasta cantidad Con Paso 1 Hacer
					Escribir i, "   ", lista_productos[ carrito_producto[i] ], "      ",lista_precios[ carrito_producto[i] ], "   ", carrito_cantidad[i] 
				Fin Para
			3:
				tamano = 5
				Escribir "No.    Nombre     Precio"
				Para i<-1 Hasta tamano Con Paso 1 Hacer
					Escribir i, "   ", lista_productos[i], "      ",lista_precios[i] 
				Fin Para
				Escribir "-----------------------------"
				
				
				
				Escribir "Ingresa el número de producto: " Sin Saltar
				leer num_producto
				Escribir "Cuantos articulos quieres de este producto " Sin Saltar
				leer cant_producto
				
				si num_producto > tamano Entonces
					Escribir "No existe el producto"
				SiNo
					cantidad <- cantidad + 1
					carrito_producto[ cantidad ] <- num_producto
					carrito_cantidad[ cantidad ] <- cant_producto					
				FinSi
				
				
			6:
				Escribir "Gracias por usar el programa"
			De Otro Modo:
				Escribir "La opcion no existe"
		Fin Segun
	Fin Mientras
		
FinAlgoritmo
