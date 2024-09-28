Algoritmo punto_1_a
	Definir op Como Entero
	Definir radio, longi, longi1 Como Real
	Escribir 'Elija la opcion de lo que desea calcular'
	Escribir ' '
	Escribir 'Opción 1: perímetro y área de un círculo dado su radio'
	Escribir 'Opción 2: perímetro y área de un pentágono'
	Escribir 'Opción 3: perímetro y área de un rectángulo'
	Leer op
	Si op==1 Entonces
		Escribir 'Ingrese el radio del circulo: '
		Leer radio
		area <- ((radio)^2)*3.1415
		perimetro <- radio*6.2831
		Escribir 'El perimetro del circulo es: ', perimetro
		Escribir 'El area del circulo es: ', area
	FinSi
	Si op==2 Entonces
		Escribir 'Ingrese la longitud de un lado del pentágono: '
		Leer longi
		perimetro <- longi*5
		area <- (5*longi^2)/(4*0.010966)
		Escribir 'El perímetro del cuadrado es de: ', perimetro
		Escribir 'El área del cuadrado es de: ', area
	FinSi
	Si op==3 Entonces
		Escribir 'Ingrese la longitud del lado mas grande del rectangulo: '
		Leer longi1
		Escribir 'Ingrese la longitud del lado mas pequeño del rectangulo: '
		Leer longi
		perimetro <- 2*(longi1+longi)
		area <- longi*longi1
		Escribir 'El perímetro del rectangulo es de: ', perimetro
		Escribir 'El área del rectangulo es de: ', area
	FinSi
FinAlgoritmo
