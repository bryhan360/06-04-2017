#!/bin/python
# -*-conding:utf-8-*-

from random import randint

Salir = False

while Salir == False:

	aleatori1 = randint(1,4)

	if (aleatori1 == 1):
		aleatori1 = "Picas"
	if (aleatori1 == 2):
		aleatori1 = "Corazones"
	if (aleatori1 == 3):
		aleatori1 = "Diamantes"
	if (aleatori1 == 4):
		aleatori1 = "Treboles"

	aleatori2 = randint(1,4)
		
	if (aleatori2 == 1):
		aleatori2 = "Picas"
	if (aleatori2 == 2):
		aleatori2 = "Corazones"
	if (aleatori2 == 3):
		aleatori2 = "Diamantes"
	if (aleatori2 == 4):
		aleatori2 = "Treboles"

	J1 = randint(1,13)

	J2 = randint(1,13)

		
	if (J1 == J2):
		print "Empate"
		
	else:
		
		if (J1 > J2):
			if (J1 == 11):
				J1 = "J"
			if (J1 == 12):
				J1 = "Q"
			if (J1 == 13):
				J1 = "K"
			
			print "J1 saca ", J1 , " de", aleatori1
			print "J2 saca ", J2 , " de", aleatori2
			print "J1 Gana"	
		
		else:
			
			if (J2 == 11):
				J2 = "J"
			if (J2 == 12):
				J2 = "Q"
			if (J2 == 13):
				J2 = "K"
			
			print "J1 saca ", J1 , " de", aleatori1
			print "J2 saca ", J2 , " de", aleatori2
			print "Eres un .... J2 Gana!"
	
	if (J1 != J2):
		Salir = True
