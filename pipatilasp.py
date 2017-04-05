#!/bin/python
# -*-conding:utf-8-*-


from random import randint

#Jugador huma
J1 = raw_input("Teclea tu jugada (PI/PA/TI/LA/SP): ")

#Jugador2 machine
aleatori=randint(1,5)
if ( aleatori==1 ):
	J2="PI"
	print "Machine juega: " , J2

if ( aleatori==2 ):
	J2="PA"
	print "Machine juega: " , J2

if ( aleatori==3 ):
	J2="TI"
	print "Machine juega: " , J2

if ( aleatori==4 ):
	J2="LA"
	print "Machine juega: " , J2

if ( aleatori==5 ):
	J2="SP"
	print "Machine juega: " , J2

if ( J1 == J2 ):
	print "Empate"

if ( J1 == "PI" and ( J2 == "LA" or J2 == "TI" ) or
 J1 == "PA" and ( J2 == "PI" or J2 == "SP" ) or
 J1 == "TI" and ( J2 =="PA" or J2 == "LA" ) or
 J1 == "LA" and ( J2 == "PA" or J2 == "SP" ) or
 J1 == "SP" and ( J2 == "PI" or J2 == "TI" )):
	print "J1 Gana"
else:
	print "J2 Gana"
