#!/usr/bin/python 
#-*- coding: utf-8 -*-
import urllib
import os 
import sys  

def Find_web():
	wordlist = raw_input ("Insert the Wordlist: ")
	URL = raw_input("Insert the URL(HTTP/HTTPS): ")
	wordlist1 = open(wordlist, "r").readlines()
        for w in wordlist1:
                w = w.replace("\n", "").replace("\r", "")
                opn = urllib.urlopen(URL+w)
		if opn.getcode() == 200:
			opn = opn.read()
			if 'login' or 'senha' or 'password' or 'admin' or 'username' in opn:
				print "\033[32m[*] Found "+URL+w+"\033[0;0m"
			else:
				print "\033[31m[*] Not Found: "+URL+w+"\033[0;0m"
		else:
			print "\033[31m[*] Not Found: "+URL+w+"\033[0;0m"

Find_web()
