data={"pass":1234,"balance":10000}
from time import sleep
#---------------------------------------
def withdraw():
	print("-"*59)
	print("\tதயவுசெய்து உங்கள் தொகையை உள்ளிடவும்")
	amount=int(input("\t"))
	if amount>data["balance"]:
		sleep(2)
		print("\tஉங்களிடம் போதுமான இருப்பு இல்லை")
	elif amount/100==0:
		print("\tபணம் வெற்றிகரமாக எடுக்கப்பட்டது")
		sleep(2)
		data["balance"]-=amount
		print("\tஉங்கள் தற்போதைய இருப்பு",data["balance"])
		sleep(2)
	else:
		print("சரியான என்னை அலக்கவும்")
		sleep(2)
		withdraw()
#----------------------------------------
def balance_en():
	print("-"*59)
	print("\tவணக்கம்உங்கள் தற்போதைய இருப்பு",data["balance"])
	print("-"*59)
#---------------------------------------
def change_pin():
	pin=int(input("\tஉங்கள் பழைய பின் எண்ணை உள்ளிடவும்\n\t")) 
	if pin==data["pass"]:
		data["pass"]=int(input("\tபுதிய பின்னை உள்ளிடவும் \n\t"))
		print("\n\tஉங்கள் பின் எண் வெற்றிகரமாக மாற்றப்பட்டது")
		return
	else:
		print("\tசரியான பின் எண்ணை உள்ளிடவும்")
		change_pin()
		return
#---------------------------------------
def tamil():
	print("-"*59)
	print("-"*59)
	print("\tபணம் எடுத்தல்--(1) ")
	print("\tஇருப்பு விசாரணை--(2) ")
	print("\tபின் எண் மாற்றம்--(3)")
	print("\tரத்து செய்--4")
	pi=int(input("\tதயவுசெய்து உங்கள் விருப்பத்தைத் தேர்ந்தெடுக்கவும்\n\t"))
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
		print("\tதவறான தொடரியல்")
		tamil()
		