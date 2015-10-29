#!/usr/bin/env python
#coding: utf-8
from scapy.all import *
from scapy.error import Scapy_Exception

interface_rede = raw_input ("Digite sua interface de rede: ") #wlan, eth..
filter_message=raw_input("Tipo de pacote: ") #ftp, ssh, http, any(para todos os tipos de pacotes)

def sniffer_TCP(snin):
        global count
        if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 21 and snin.haslayer(Raw): #pega a camada/pacotes TCP rodando na porta FTP          
                print snin.getlayer(Raw).load
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 22 and snin.haslayer(Raw): #pega a camada/pacotes TCP rodando na porta SSH
                print snin.getlayer(Raw).load
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 80 and snin.haslayer(Raw): #pega a camada/pacotes TCP rodando na porta HTTP         
                print snin.getlayer(Raw).load
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 25 and snin.haslayer(Raw): #pega a camada/pacotes TCP rodando na porta SMTP         
                print snin.getlayer(Raw).load
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 110 and snin.haslayer(Raw): #pega a camada/pacotes TCP rodando na porta POP3         
                print snin.getlayer(Raw).load
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 143 and snin.haslayer(Raw): #pega a camada/pacotes TCP rodando na porta IMAP        
                print snin.getlayer(Raw).load

sniff(iface=interface_rede, prn=sniffer_TCP, store=0) #sniff(função) / iface = interface de rede / store = 0 nao acumula na memoria 
