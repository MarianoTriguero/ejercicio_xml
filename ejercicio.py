# -*- coding: utf-8 -*-

from lxml import etree

tree = etree.parse("Guardias.xml")
raiz = tree.getroot()
farmacias = raiz.findall("FARMACIAGUARDIA")

print "LISTA DE FARMACIAS"
#Muestra el nombre de las farmacias, junto a su grupo y localidad
acum = 0
for farm in farmacias:
	acum = acum + 1
	for dato in farm:
		if dato.tag == "FARMACIA":
			nombre = dato.text
		elif dato.tag == "GRUPO":
			grupo = dato.text
		elif dato.tag == "LOCALIDAD":
			localidad =dato.text
	print " ----------------------------- \nFarmacia de guardia nº" + str(acum)
	print "Nombre de farmacia: " + nombre
	print "Grupo: " + grupo
	print "Localidad: " + localidad

print "\n -------------------- \nMuestra el numero de farmacias por localidad.\n"
#Muestra el numero de farmacias en guardia por localidad
lista = []
for farm in farmacias:
	encontrado = False
	for dato in farm:
		if dato.tag == "LOCALIDAD":
			puntero = 0
			for elem in lista:
				if dato.text == elem[0]:
					lista[puntero][1] = elem[1] + 1
					encontrado = True
					break
				puntero = puntero + 1
			if encontrado == False:
				lista.append([dato.text,1])
for elem in lista:
	print "En la localidad " + elem[0] + " hay " + str(elem[1]) + " farmacias de guardia."

#Muestra el nombre y el telefono de las farmacias que esten de guardia para un dia en concreto
#Nota: Este xml se actualiza a diario y ahora solamente dispone de datos de febrero y marzo
dia = raw_input("Dime un dia del mes: ")
mes = raw_input("Dime un mes del año: ")
if len(dia) == 1:
	dia = "0" + dia
if len(mes) == 1:
	mes = "0" + mes
fecha = dia + "/" + mes + "/" + "2016"

listadeguardia = []
for farm in farmacias:
	for dato in farm:
		if dato.tag == "FECHA":
			if fecha == dato.text:
				listadeguardia.append(farm)

for farm in farmacias:
	print " ------------------- "
	for dato in farm:
		if dato.tag == "FARMACIA":
			nombre = dato.text
		elif dato.tag == "TELEFONO":
			telefono = dato.text
		elif dato.tag == "DIRECCION":
			direccion = dato.text
	print "La farmacia " + nombre + " esta de guardia."
	print "Direccion: " + direccion
	print "Telefono: " + telefono
