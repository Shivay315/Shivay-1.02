import time
import os
import socket
from tkinter import messagebox, Tk

login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()

print('''


░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░██╗░░░██╗        ░░███╗░░░░░░█████╗░██████╗░
██╔════╝██║░░██║██║██║░░░██║██╔══██╗╚██╗░██╔╝        ░████║░░░░░██╔══██╗╚════██╗
╚█████╗░███████║██║╚██╗░██╔╝███████║░╚████╔╝░        ██╔██║░░░░░██║░░██║░░███╔═╝
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║░░╚██╔╝░░        ╚═╝██║░░░░░██║░░██║██╔══╝░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░        ███████╗██╗╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░        ╚══════╝╚═╝░╚════╝░╚══════╝
''')


print("Welcome " + l_n)
print("The Date Is: " + time.strftime("%m/%d/%y"))
print("""
[1] To Open Google
[2] To Open Text Editor
[3] To Open File Explorer
[4] To Configure and Open BioS
[5] To Open Terminal
[6] To Open Calculator
[7] To Open Digital Clock
[8] To Open Contact Book
[0] To Close OS Safely
""")

select = input("[?]: ")

if select == '1':
	os.startfile('home.py')
	os.startfile('brows.py')

elif select == '2':
	os.startfile('home.py')
	os.startfile('edit.pyw')

elif select == '3':
	os.startfile('home.py')
	os.startfile('file.pyw')

elif select == '4':
	while True:
		b_login = input(str("Please Enter The Password " + l_n + " To Open BioS: "))
		if b_login == l_p:
			print("Opening BioS")
			host_name = socket.gethostname()
			host_ip = socket.gethostbyname(host_name)
			print("[1] USER NAME: " + l_n)
			print("[2] PASSWORD: " + l_p)
			print("Hostname:", host_name)
			print("LOCAL IPS: " + host_ip)
			print()
			print()
			print("Enter [3] to exit BIOS")
			edit_b = input("Enter [?] to change setting: ")
			if edit_b == '1':
				edit_n = input("Enter New Username: ")
				with open('user/dataname.pass', 'w') as f:
					f.writelines(edit_n)
				print("Username Changed To " + edit_n)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')

			elif edit_b == '2':
				edit_p = input("Enter New Password: ")
				with open('user/password.pass', 'w') as f:
					f.writelines(edit_p)

				print("Password Changed To " + edit_p)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')

			elif edit_b == '3':
				os.startfile('home.py')
				os.system('exit')
		else:
			def alert(title, message, kind='info', hidemain=True):
				if kind not in ('error', 'warning', 'info'):
					raise ValueError('Unsupported alert kind.')

				show_method = getattr(messagebox, 'show{}'.format(kind))
				show_method(title, message)


			if __name__ == '__main__':
				Tk().withdraw()
				alert('Alert', 'Wrong Password!', kind='warning')

elif select == '5':
	os.startfile('home.py')
	os.startfile('terminal.py')

elif select == '6':
	os.startfile('home.py')
	os.startfile('calc.py')

elif select == '7':
	os.startfile('home.py')
	os.startfile('clock.py')

elif select == '8':
	os.startfile('home.py')
	os.startfile('phone.py')

elif select == '0':
	os.system('exit')

else:
	def alert(title, message, kind='info', hidemain=True):
		if kind not in ('error', 'warning', 'info'):
			raise ValueError('Unsupported alert kind.')

		show_method = getattr(messagebox, 'show{}'.format(kind))
		show_method(title, message)


	if __name__ == '__main__':
		Tk().withdraw()
		alert('Alert', 'Please enter an input lying between 1 to 8')
		os.startfile('home.py')