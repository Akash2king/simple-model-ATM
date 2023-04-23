data={"pass":1234,"balance":10000}
from time import sleep
#---------------------------------------
def withdraw():
	print("\tpleace Enter Your Amount\n \t (avalable 100,200,500)")
	amount=int(input("\t"))
	
	if amount>data["balance"]:
		sleep(2)
		print("\tyou have insuffecient balance")
	if (amount%100==0):
		print("\tcash withdrawel succesfully")
		sleep(2)
		data["balance"]-=amount
		print("\tyour currrnt balance is",data["balance"])
		sleep(2)
	if (amount%100!=0):
		print("please enter valid amount... ")
		sleep(2)
		withdraw()
#----------------------------------------
def balance_en():
	print("\tHello your current balance is ",data["balance"])
	print("-"*59)
#---------------------------------------
def change_pin():
	pin=int(input("\tpleace enter your old pin number\n\t")) 
	if pin==data["pass"]:
		data["pass"]=int(input("\tEnter a new pin \n\t"))
		print("\tyour pin number is succesfully changed")
		return
	else:
		print("\tpleace enter a correct pin number")
		change_pin()
		return
#---------------------------------------
def english():
	print("-"*59)
	print("-"*59)
	print("\tcash Withdrawal--(1) ")
	print("\tBalance Enquiry--(2) ")
	print("\tChange pin --(3)")
	print("\tcancel--4")
	pi=int(input("\tPleace enter your choice\n\t"))
	if pi==(1):
		withdraw()
		return
	elif pi==(2):
		balance_en()
		return
	elif pi==(3):
		change_pin()
		return
	elif pi==(4):
		return
	else:
		print("\tpleace enter a correct value")
		tamil()
		