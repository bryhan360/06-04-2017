#!/bin/python
# -*-conding:utf-8-*-

from random import randint

Salir = False

while Salir == False:

	palo1 = randint(1,4)

	if (palo1 == 1):
		palo1 = "Picas"
	if (palo1 == 2):
		palo1 = "Corazones"
	if (palo1 == 3):
		palo1 = "Diamantes"
	if (palo1 == 4):
		palo1 = "Treboles"

	palo2 = randint(1,4)
		
	if (palo2 == 1):
		palo2 = "Picas"
	if (palo2 == 2):
		palo2 = "Corazones"
	if (palo2 == 3):
		palo2 = "Diamantes"
	if (palo2 == 4):
		palo2 = "Treboles"

	J1numero = randint(2,14)

	J2numero = randint(2,14)

		
	if (J1numero == J2numero):
		print "Empate"
		
	else:
		
		if (J1numero > J2numero):
			if (J1numero == 11):
				J1numero = "J"
			if (J1numero == 12):
				J1numero = "Q"
			if (J1numero == 13):
				J1numero = "K"
			if (J1numero == 14):
				J1numero = "AS"
				
			print "J1 saca ", J1numero , " de", palo1
			print "J2 saca ", J2numero , " de", palo2
			print "J1 Gana"	
		
		else:
			
			if (J2numero == 11):
				J2numero = "J"
			if (J2numero == 12):
				J2numero = "Q"
			if (J2numero == 13):
				J2numero = "K"
			if (J2numero == 14):
				J2numero = "AS"
				
			print "J1 saca ", J1numero , " de", palo1
			print "J2 saca ", J2numero , " de", palo2
			print "Eres un malisimo, J2 Gana!"
	
	if (J1numero != J2numero):
		Salir = True
