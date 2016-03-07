# -*- coding: utf-8 -*-

from lxml import etree

tree = etree.parse("Guardias.xml")
raiz = tree.getroot()
farmaciasfecha = raiz.findall("FARMACIAGUARDIA")
farmacias = []
for farmfecha in farmaciasfecha:
	codigo = farmfecha.find("Cod_FARMACIA").text
	if len(farmacias) == 0:
		farmacias.append(farmfecha)
	encontrado = False
	for farm in farmacias:
		if farm.find("Cod_FARMACIA").text == codigo:
			encontrado = True
			break
	if encontrado == False:
		farmacias.append(farmfecha)

print "LISTA DE FARMACIAS"
#Muestra el nombre de las farmacias, junto a su grupo y localidad
acum = 0
for farm in farmacias:
	acum = acum + 1 
	print " ----------------------------- \nFarmacia de guardia nº" + str(acum)
	print "Nombre de farmacia: " + farm.find("FARMACIA").text
	print "Grupo: " + farm.find("GRUPO").text
	print "Localidad: " + farm.find("LOCALIDAD").text

print "\n -------------------- \nMuestra el numero de farmacias por localidad.\n"
#Muestra el numero de farmacias en guardia por localidad
lista = []
for farm in farmacias:
	encontrado = False
	puntero = 0
	for elem in lista:
		if farm.find("LOCALIDAD").text == elem[0]:
			lista[puntero][1] = elem[1] + 1
			encontrado = True
			break
		puntero = puntero + 1
	if encontrado == False:
		lista.append([farm.find("LOCALIDAD").text,1])
for elem in lista:
	print "En la localidad " + elem[0] + " hay " + str(elem[1]) + " farmacias de guardia."

#Muestra el nombre, el telefono y la direccion de las farmacias que esten de guardia cuyo telefono empiece por unos digitos concretos
digitos = raw_input("\nDame las 4 ultimas cifras del telefono de las farmacias para realizar la busqueda: ")
salidacadena = False
for farm in farmacias:
	if farm.find("TELEFONO").text[-4:] == digitos:
		print "La farmacia " + farm.find("FARMACIA").text + " coincide con la busqueda."
		salidacadena = True
if salidacadena == False:
	print "No se ha encontrado nada"

#Necesitamos ir a una farmacia de urgencia. Introduzca un dia y un mes para mostrar que farmacias estan de guardia en ese momento.
print "\nFarmacias de guardia en fecha concreta"
dia = raw_input("Dime un dia del mes: ")
mes = raw_input("Dime un mes del año: ")
if len(dia) == 1:
	dia = "0" + dia
if len(mes) == 1:
	mes = "0" + mes
fecha = dia + "/" + mes + "/" + "2016"
salidacadena = False
for farm in farmacias:
	if fecha == farm.find("FECHA").text:
		print "La farmacia " + farm.find("FARMACIA").text + " esta de guardia en la fecha indicada y su direccion es: " + farm.find("DIRECCION").text
		salidacadena = True
if salidacadena == False:
	print "No se ha encontrado nada"

#Introduzca  el nombre de una farmacia para mostrar su horario habitual y los dias que ha estado de guardia anteriormente
nombre = raw_input("\nIntroduzca el nombre completo de una farmacia(Primero nombre y despues apellidos): ")
cadena = nombre.split(" ")
nuevonombre = cadena[1] + " " + cadena[2] + ", " + cadena[0]
for farm in farmacias:
	if nuevonombre == farm.find("FARMACIA").text:
		print "La farmacia " + farm.find("FARMACIA").text + " tiene un horario de " + farm.find("DESDE").text + " de la mañana a " + farm.find("HASTA").text + " de la noche."
		codigo = farm.find("Cod_FARMACIA").text
		break

for farm in farmaciasfecha:
	if farm.find("Cod_FARMACIA").text == codigo:
		print "La farmacia estuvo de guardia el dia: " + farm.find("FECHA").text
