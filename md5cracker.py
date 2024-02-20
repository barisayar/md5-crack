#-*- coding: utf-8 -*-
import hashlib
 
print """
###########################
#         Md5 Cracker     #
#         Baris Ayar      #
###########################
"""
 
md5hash = raw_input("Kırılacak Hash: ")
wordlist = open("wordlist.txt", "r").readlines()
 
for kelime in wordlist:
	kelime = kelime.strip()
	kir = hashlib.md5(kelime).hexdigest()
	if kir == md5hash:
		print "MD5 Cracklendi: " + kelime
		break
