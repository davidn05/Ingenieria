Algoritmo punto_1_b
	Definir edad, sexo Como Entero
	Escribir 'Indique su edad: '
	Leer edad
	Escribir 'Indique su sexo: '
	Escribir 'Hombre = 1'
	Escribir 'Mujer = 2'
	Leer sexo
	Si edad>=16 Entonces
		Si sexo=1 Entonces
			Escribir 'Usted es hombre y puede votar.'
		FinSi
		Si sexo=2 Entonces
			Escribir 'Usted es mujer y puede votar.'
		FinSi
	FinSi
	Si edad<16 Entonces
		Si sexo=1 Entonces
			Escribir 'Usted es hombre y no puede votar.'
		FinSi
		Si sexo=2 Entonces
			Escribir 'Usted es mujer y no puede votar.'
		FinSi
	FinSi
FinAlgoritmo
