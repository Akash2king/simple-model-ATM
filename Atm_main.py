import atm_mod
import Atm_tam
from time import sleep
lang1="தமிழ் ( 1 )"
lang2="English ( 2 )"
a="-"*59
b="WELCOME"
c="pleace enter your card"
while True:
	print(a)
	print(b.center(59,"-"))
	print(c.center(59,"-")) 
	input()
	print("\tPleace Enter Your 𝟺 ᴅɪɢɪᴛ pin number")
	pin=int(input("\t :"))
	if pin==atm_mod.data["pass"]:
		print("\tselect your language","\n",lang1,"\n",lang2)
		la=int(input("\t"))
		print(a)
		if la==(1):
			Atm_tam.tamil()
			print("Transaction Ended.. ")
			print(".\n.\n.\n.\n.")
			sleep(5)
		elif la==(2):
			atm_mod.english()
			print("Transaction Ended.. ")
			print(".\n.\n.\n.\n.")
			sleep(5)
	else:
		print("\tEntered pin Number is wrong")
		print("\ttransaction Ended")
		pass
		
